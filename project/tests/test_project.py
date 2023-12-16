import os

from streamlit.testing.v1 import AppTest


def test_key_in_env():
    assert os.getenv('API_KEY_YOUTUBE') is not None

def test_bad_url_input():
    at = AppTest.from_file('project.py', default_timeout=10)
    at.secrets['API_KEY_YOUTUBE'] = os.getenv('API_KEY_YOUTUBE')
    at.run()
    at.sidebar.text_input[0].input('123').run()
    at.sidebar.button[0].click().run()
    assert len(at.sidebar.text_input) == 1
    assert at.warning[0].value == 'URL'
    assert at.success[0].value == 'Готово! Обработано 20 комментариев.'

def test_url_input():
    at = AppTest.from_file('project.py', default_timeout=10)
    at.secrets['API_KEY_YOUTUBE'] = os.getenv('API_KEY_YOUTUBE')
    at.run()
    at.sidebar.text_input[0].input('https://www.youtube.com/watch?v=wDmPgXhlDIg').run()
    at.sidebar.button[0].click().run()
    assert len(at.sidebar.text_input) == 1
    assert at.success[0].value == 'URL'
    assert at.success[1].value == 'Готово! Обработано 100 комментариев.'
