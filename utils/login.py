import yaml
import shutil
from openai import OpenAI
from instabot import Bot

shutil.rmtree('./config', ignore_errors=True)
CREDENTIALS_PATH = './utils/credentials.yml'

def load_credentials(file_path=CREDENTIALS_PATH):
    '''Load credentials'''
    with open(file_path, 'r') as file:
        creds = yaml.safe_load(file)
    return creds

credentials = load_credentials(CREDENTIALS_PATH)
OPENAI_API_KEY = credentials['OPENAI_API_KEY']
INSTA_USER = credentials['INSTA_USER']
INSTA_PASS = credentials['INSTA_PASS']

bot = Bot()
bot.login(username=INSTA_USER, password=INSTA_PASS, force=True)
openai_client = OpenAI(api_key=OPENAI_API_KEY)
