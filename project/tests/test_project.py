import os

#from dotenv import load_dotenv
from streamlit.testing.v1 import AppTest

# Jast a simple test 
def test_url_input():
    at = AppTest.from_file('project.py', default_timeout=30)    
    at.run()
    at.sidebar.text_input[0].input('https://www.youtube.com/watch?v=wDmPgXhlDIg').run()
    at.sidebar.button[0].click().run()    
    assert at.success[0].value == 'URL' 


'''
load_dotenv()
DEVELOPER_KEY = os.environ.get('API_KEY_YOUTUBE')


def test_key_in_env():
    assert DEVELOPER_KEY is not None

def test_bad_url_input():
    at = AppTest.from_file('project.py', default_timeout=30)
    at.secrets['API_KEY_YOUTUBE'] = DEVELOPER_KEY
    at.run()
    at.sidebar.text_input[0].input('123').run()
    at.sidebar.button[0].click().run()
    assert len(at.sidebar.text_input) == 1
    assert at.warning[0].value == 'URL'
    assert len(at.success) == 1

def test_url_input():
    at = AppTest.from_file('project.py', default_timeout=30)
    at.secrets['API_KEY_YOUTUBE'] = DEVELOPER_KEY
    at.run()
    at.sidebar.text_input[0].input('https://www.youtube.com/watch?v=wDmPgXhlDIg').run()
    at.sidebar.button[0].click().run()
    assert len(at.sidebar.text_input) == 1
    assert at.success[0].value == 'URL'
    assert len(at.success) == 2
'''
