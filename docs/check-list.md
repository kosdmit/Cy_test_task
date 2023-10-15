# Чек лист тестирования формы регистрации

*\*Галочкой отмечены реализованные проверки*

*\*В данный чек лист не включены проверки специальных валидаторов полей (например для номера телефона или email)*

## 1 Проверки текстовых полей

[Test Case](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/test_registration_page.py#L80-L129)

### 1.1 Проверки допустимого количества символов в поле

#### Параметры:

_Позитивные_

- [x] Среднее количество символов в поле для кириллицы и латиницы: Иванов (RU) | Parker (EN)

  [test method](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/test_registration_page.py#L88-L91)
| [data](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/data.py#L54-L88)

- [x] Минимальное количество символов в поле: И

  [test method](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/test_registration_page.py#L88-L91)
| [data](https://github.com/kosdmit/Cy_test_task/blob/5ac5f0c11c8c15c6e55ef5457fdc85adc3df9a13/tests/data.py#L98-L101)

- [x] Большое количество символов в поле: Ивановпертровсидоргончаровпушкинлермонтов

  [test method](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/test_registration_page.py#L88-L91)
| [data](https://github.com/kosdmit/Cy_test_task/blob/5ac5f0c11c8c15c6e55ef5457fdc85adc3df9a13/tests/data.py#L103-L106)

- [x] Ноль символов: если поле необязательно для заполнения.

  [test method](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/test_registration_page.py#L88-L91)
| [data](https://github.com/kosdmit/Cy_test_task/blob/5ac5f0c11c8c15c6e55ef5457fdc85adc3df9a13/tests/data.py#L108-L112)

- [x] Поле содержит дефис: Иванова-Ильина

  [test method](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/test_registration_page.py#L88-L91)
| [data](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/data.py#L114-L118)

  
_Негативные_

- [x] Количество символов меньше минимального (обязательные поля пустые)

  [test method](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/test_registration_page.py#L111-L117)
| [data](https://github.com/kosdmit/Cy_test_task/blob/5ac5f0c11c8c15c6e55ef5457fdc85adc3df9a13/tests/data.py#L108-L112)

- [x] Количество символов больше максимального (можно ввести очень большой текст и нарушить работу системы. Используются строки длинной более 500 символов, тест помечен как **expected failed**)

  [test method](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/test_registration_page.py#L120-L129)
| [data](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/data.py#L132)

- [x] Числа и другие спец. символы в исключительно текстовом поле (предполагается что имена не могут содержать числа и другие спец. символы, тест помечен как **expected failed**)

  [test method](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/test_registration_page.py#L94-L108)
| [data](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/data.py#L121-L128)

  
### 1.2 Проверки ввода допустимых символов

Позитивные проверки

- [ ] Буквы, цифры, специальные символы
- [ ] Текст с пробелом: в начале строки, в середине и в конце
- [ ] Можно вставить в поле скопированный текст
- [ ] Перенос строки внутри поля через Enter.

Негативные проверки:

- [ ] Символы, ввод которых требованиями не предусмотрен
- [ ] Текст с пробелом: в начале строки, в середине и в конце
- [ ] Только пробел
- [ ] Символы не ASCII (например, эмоджи) — ♣☺♂
- [x] SQL инъекции, XSS, html-теги

  [test method](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/test_registration_page.py#L120-L129)
| [data](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/data.py#L133-L135)

  
## 2 Проверки чек-боксов и радиокнопок

[Test Case](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/test_registration_page.py#L132-L163)

### 2.1 Проверки чек-боксов


  [test method](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/test_registration_page.py#L156-L163)
| [data](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/data.py#L42-L46)


- [x] Любой чек-бокс может быть в состоянии «Включен»
- [x] Любой чек-бокс может быть в состоянии «Выключен»
- [x] Можно включить все чек-боксы одновременно.
- [x] Нельзя оставить выключенным обязательный для заполнения чек-бокс


### 2.2 Проверки радиокнопок

  [test method](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/test_registration_page.py#L133-L153)
| [data](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/data.py#L37-L40)


- [x] Выбрать только один вариант
- [x] Выбрать любой вариант из списка
- [x] Не выбирать ни одного варианта.
- [x] Нельзя не выбирать ни одного варианта если выбор обязателен по требованиям
- [x] Нельзя выбрать несколько вариантов одновременно
- [x] Выбранные опции корректно передаются на сервер

## 3 Проверки кнопки отправки формы

[Test Case](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/test_registration_page.py#L166-L190)

### 3.1 Проверки неактивного состояния

- [x] В неактивном состоянии кнопка не отправляет форму

  [test method](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/test_registration_page.py#L176-L190)


### 3.2 Проверки активного состояния

- [x] В активном состоянии кнопка корректно отправляет форму
- [x] Возможность отправить форму нажав клавишу Enter (тест помечен как **expected failed**)

  [test method](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/test_registration_page.py#L167-L173)


## 4 Проверки страницы подтверждения отправки письма

### 4.1 Проверки контента страницы

- [x] Страница соответствует выбранным опциям (Основная/Дополнительная олимпиада)

  [test method](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/test_registration_page.py#L133-L153)

- [x] Страница содержит указанный пользователем email

  [test method](https://github.com/kosdmit/Cy_test_task/blob/db9c1bd1dd2cff190610bc40f7c5ab513afbcf23/tests/test_registration_page.py#L46-L57)


## 5 Дополнительные проверки 
(для реализации в будущем)

- [ ] Проверить сообщения об ошибках (например, "Пароль слишком короткий" или "Этот email уже зарегистрирован").
- [ ] Проверить работоспособность в разных браузерах.
- [ ] Проверить на возможность CSRF атаки.
- [ ] Проверить функционал интернационализации.
