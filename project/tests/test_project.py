import os

from streamlit.testing.v1 import AppTest

DEVELOPER_KEY = os.getenv('API_KEY_YOUTUBE')


# def test_key_in_env():
#     assert DEVELOPER_KEY is not None

def test_bad_url_input():
    at = AppTest.from_file('project.py', default_timeout=10)
    at.secrets['API_KEY_YOUTUBE'] = DEVELOPER_KEY
    at.run()
    at.sidebar.text_input[0].input('123').run()
    at.sidebar.button[0].click().run()
    assert len(at.sidebar.text_input) == 1
    assert at.warning[0].value == 'URL'
    assert at.success[0].value == 'Готово! Обработано 20 комментариев.'

def test_url_input():
    at = AppTest.from_file('project.py', default_timeout=10)
    at.secrets['API_KEY_YOUTUBE'] = DEVELOPER_KEY
    at.run()
    at.sidebar.text_input[0].input('https://www.youtube.com/watch?v=wDmPgXhlDIg').run()
    at.sidebar.button[0].click().run()
    assert len(at.sidebar.text_input) == 1
    assert at.success[0].value == 'URL'
    assert at.success[1].value == 'Готово! Обработано 100 комментариев.'
