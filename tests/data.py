import random
from copy import copy

from mimesis import Generic
from mimesis.builtins import RussiaSpecProvider
from mimesis.locales import Locale


urls = {
    'registration_page': 'https://uts.sirius.online//#/auth/register/qainternship',
}


selectors = {
    'text_inputs': {
        'last_name': '.test-locator-sf-lastName input',
        'first_name': '.test-locator-sf-firstName input',
        'patronymic': '.test-locator-sf-patronymic input',
        'birth_date': '.test-locator-sf-birth-date input',
        'email': '.test-locator-sf-email input',
        'vosh_login': '.test-locator-sf-vosh-login-optional input',
        'phone': '.test-locator-sf-phone input',
        'snils': '.test-locator-sf-snils-opt input',
        'profession': '.test-locator-sf-profession input',

        # School information
        'city': '.test-locator-sf-school-city input',
        'organization': '.test-locator-sf-school-organization input',
        'school': '.test-locator-sf-school-school input',
        'grade': '.test-locator-sf-school-grade input',
    },

    'select_inputs': {
        'country': '.test-locator-sf-school-country select',
    },

    'radio_inputs': {
        'main_contest': '.test-locator-sf-switch ul li:first-child',
        'additional_contest': '.test-locator-sf-switch ul li:nth-child(2)',
    },

    'checkbox_inputs': {
        'veracity': '.test-locator-sf-confirmation-of-veracity input',
        'agreement': '.test-locator-sf-users-agreement-and-personal-data input',
        'rules': '.test-locator-sf-familiarized-with-the-rules input',
    },

    'submit_buttons': {
        'submit': 'button.smt-register-form__register-btn',
    }
}


data_generators = [
    (Generic(locale=Locale.RU), 'RU'),
    (Generic(locale=Locale.EN), 'US'),
    # (Generic(locale=Locale.TR), 'TR'),  # TODO: test crushed with TR locale
]
data_generators[0][0].add_provider(RussiaSpecProvider)


valid_data_sets = {}
for data_generator, locale in data_generators:
    valid_data_sets[locale] = {
        'last_name': data_generator.person.last_name(),
        'first_name': data_generator.person.name(),
        'patronymic':
            data_generator.russia_provider.patronymic()
            if data_generator.locale == Locale.RU
            else data_generator.person.surname(),

        'birth_date': data_generator.datetime.formatted_date(fmt='%d.%m.%Y', start=1923, end=2004),
        'email': 'kosdmit@hotmail.com',
        'vosh_login': 'v00.000.000',
        'phone': data_generator.person.phone_number(),
        'snils':
            data_generator.russia_provider.snils()
            if data_generator.locale == Locale.RU
            else '',

        'profession': data_generator.person.occupation(),

        'country': locale,
        'city': data_generator.address.city(),
        'organization': data_generator.finance.company(),
        'school': data_generator.address.prefecture(),
        'grade': str(random.randrange(start=1, stop=12, step=1)),
    }


inputs_without_special_validation = ('last_name', 'first_name', 'patronymic',
                                     'profession', 'city', 'organization',
                                     'school', 'grade')

optional_inputs = ('patronymic', 'vosh_login', 'phone', 'snils', )
required_inputs = (input_name for input_name in selectors['text_inputs'].keys() if input_name not in optional_inputs)

# Test minimum signs in field
valid_data_sets['short_values'] = copy(valid_data_sets['RU'])
for input_name in inputs_without_special_validation:
    valid_data_sets['short_values'][input_name] = valid_data_sets['short_values'][input_name][:1]

# Test maximum signs in field
valid_data_sets['long_values'] = copy(valid_data_sets['RU'])
for input_name in inputs_without_special_validation:
    valid_data_sets['long_values'][input_name] = valid_data_sets['long_values'][input_name]*10

# Test only required fields
valid_data_sets['required_inputs'] = copy(valid_data_sets['RU'])
for input_name in valid_data_sets['required_inputs'].keys():
    if input_name in optional_inputs:
        valid_data_sets['required_inputs'][input_name] = ''

# Test hyphen sign is acceptable
valid_data_sets['hyphen_sign'] = copy(valid_data_sets['RU'])
for input_name in inputs_without_special_validation:
    valid_data_sets['hyphen_sign'][input_name] = \
        valid_data_sets['hyphen_sign'][input_name] + '-' + valid_data_sets['hyphen_sign'][input_name]


invalid_data_sets = {
    'nums_in_non_num_fields':
        {
            'last_name': valid_data_sets['RU']['last_name'] + str(random.randint(0, 99)),
            'first_name': valid_data_sets['RU']['first_name'] + str(random.randint(0, 99)),
            'patronymic': valid_data_sets['RU']['patronymic'] + str(random.randint(0, 99)),
        }
}


def get_invalid_value(test_name: str, value) -> str:
    map_dict = {
        'value_longer_max_length': lambda x: x*100,
        'sql_injection': lambda x: "SELECT * FROM news WHERE user='$user'",
        'xss_injection': lambda x: "<script>alert(123)</script>",
        'html_injection': lambda x: "<h1>Hello world</h1>",


    }

    return map_dict[test_name](value)

