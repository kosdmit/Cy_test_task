import time
from copy import copy

import pytest
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from tests.data import urls, selectors, valid_data_sets, invalid_data_sets, \
    optional_inputs, inputs_without_special_validation, get_invalid_value, \
    required_inputs


class GeneralFixturesMixin:
    def setup(self):
        self.browser = webdriver.Chrome()
        self.browser.get(urls['registration_page'])
        self.wait = WebDriverWait(self.browser, timeout=2)

    def teardown(self):
        self.browser.quit()

    def send_data(self, data_set):
        for text_input_name, selector in selectors['text_inputs'].items():
            input_element = self.browser.find_element(By.CSS_SELECTOR, selector)
            input_element.send_keys(data_set[text_input_name])
            if text_input_name == 'birth_date':
                input_element.click()
                time.sleep(1)

        for select_input_name, selector in selectors['select_inputs'].items():
            input_element = self.browser.find_element(By.CSS_SELECTOR, selector)
            select = Select(input_element)
            select.select_by_value(data_set['country'])

        for checkbox_name, selector in selectors['checkbox_inputs'].items():
            input_element = self.browser.find_element(By.CSS_SELECTOR, selector)
            input_element.click()


class GeneralChecksMixin:
    def check_form_is_valid(self, data_set):
        error_list = self.browser.find_elements(By.CSS_SELECTOR, '.ui-schema-auth-form__error')
        submit_button = self.browser.find_element(By.CSS_SELECTOR, selectors['submit_buttons']['submit'])

        assert len(error_list) == 0
        assert submit_button.is_enabled() is True

        submit_button.click()
        self.browser.implicitly_wait(5)

        success_message = self.browser.find_element(By.CSS_SELECTOR, '.smt-auth-registration-panel__success-message')
        assert data_set['email'] in success_message.text


    def check_form_is_invalid(self):
        error_list = self.browser.find_elements(By.CSS_SELECTOR, '.ui-schema-auth-form__error')
        submit_button = self.browser.find_element(By.CSS_SELECTOR, selectors['submit_buttons']['submit'])

        if not submit_button.is_enabled():
            assert submit_button.is_enabled() is False
        else:
            submit_button.click()
            self.browser.implicitly_wait(5)
            try:
                success_message = self.browser.find_elements(
                    By.CSS_SELECTOR,
                    '.smt-auth-registration-panel__success-message'
                )
            except selenium.common.exceptions.NoSuchElementException:
                success_message = None

            assert not success_message


class TestTextInputs(GeneralChecksMixin, GeneralFixturesMixin):
    def send_invalid_value(self, invalid_input_name, invalid_value):
        invalid_input_selector = selectors['text_inputs'][invalid_input_name]
        invalid_input_element = self.browser.find_element(By.CSS_SELECTOR, invalid_input_selector)
        invalid_input_element.clear()
        invalid_input_element.send_keys(invalid_value)


    @pytest.mark.parametrize('data_set', valid_data_sets.values())
    def test_with_valid_data(self, data_set):
        self.send_data(data_set)
        self.check_form_is_valid(data_set)


    @pytest.mark.xfail  # Expected a validator for name fields to exclude using special characters
    @pytest.mark.parametrize(
        'invalid_input_name, invalid_value',
        invalid_data_sets['nums_in_non_num_fields'].items(),
    )
    def test_with_nums_in_non_num_fields(
            self,
            invalid_input_name,
            invalid_value,
            data_set=valid_data_sets['RU']):

        self.send_data(data_set)
        self.send_invalid_value(invalid_input_name, invalid_value)

        self.check_form_is_invalid()


    @pytest.mark.parametrize('missed_required_field', required_inputs)
    def test_with_missed_required_text_field(self, missed_required_field):
        data_set = copy(valid_data_sets['RU'])
        data_set[missed_required_field] = ''

        self.send_data(data_set)
        self.check_form_is_invalid()


    invalid_data_tests: tuple[str] = ('value_longer_max_length', 'sql_injection')  # TODO: Refactor this


    @pytest.mark.xfail
    @pytest.mark.parametrize('text_input_name', inputs_without_special_validation)
    @pytest.mark.parametrize('test_name', invalid_data_tests)
    def test_text_input_validation(self, test_name, text_input_name, data_set=valid_data_sets['RU']):
        invalid_value = get_invalid_value(test_name, data_set[text_input_name])

        self.send_data(data_set)
        self.send_invalid_value(text_input_name, invalid_value)

        self.check_form_is_invalid()


class TestCheckboxesRadioButtons(GeneralChecksMixin, GeneralFixturesMixin):
    @pytest.mark.parametrize('selector', selectors['radio_inputs'].values())
    def test_radio_buttons_with_valid_data(self, selector,
                                           data_set=valid_data_sets['RU']):
        self.send_data(data_set)
        radio_button = self.browser.find_element(By.CSS_SELECTOR, selector)
        radio_button_text = radio_button.find_element(
            By.CSS_SELECTOR,
            'span.ui-schema-auth-form__enum-input-label'
        ).text
        radio_button.click()

        submit_button = self.browser.find_element(By.CSS_SELECTOR, selectors['submit_buttons']['submit'])
        submit_button.click()
        self.browser.implicitly_wait(5)

        success_page_title = self.browser.find_element(
            By.CSS_SELECTOR,
            '.smt-auth-registration-panel__title'
        ).text

        assert radio_button_text in success_page_title


    @pytest.mark.parametrize('selector', selectors['checkbox_inputs'].values())
    def test_with_missed_required_checkbox(self, selector, data_set=valid_data_sets['RU']):
        self.send_data(data_set)

        missed_checkbox = self.browser.find_element(By.CSS_SELECTOR, selector)
        missed_checkbox.click()

        self.check_form_is_invalid()


class TestSubmit(GeneralFixturesMixin):
    @pytest.mark.xfail
    def test_submit_by_enter_with_valid_data(self, data_set=valid_data_sets['RU']):
        self.send_data(data_set)
        ActionChains(self.browser).key_down(Keys.ENTER).perform()
        self.browser.implicitly_wait(5)

        assert self.browser.find_elements(By.CSS_SELECTOR, '.smt-auth-registration-panel__success-message')


    def test_inactive_submit_is_not_clickable(self, data_set=valid_data_sets['RU']):
        self.send_data(data_set)

        missed_checkbox = self.browser.find_element(By.CSS_SELECTOR, next(iter(selectors['checkbox_inputs'].values())))
        missed_checkbox.click()

        submit_button = self.browser.find_element(By.CSS_SELECTOR, selectors['submit_buttons']['submit'])
        assert submit_button.is_enabled() is False

        try:
            submit_button.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            assert True
        else:
            assert False

