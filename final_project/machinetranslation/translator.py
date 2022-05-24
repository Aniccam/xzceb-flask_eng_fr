import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version='2022-05-24',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')

def english_to_french(english_text):
    """
    The function translates English to French
    """
    en_to_fr = language_translator.translate(
                            text=english_text,   
                            model_id='en-fr').get_result()
    french_text = en_to_fr.get("translations")[0].get("translation")
    return french_text

def french_to_english(french_text):
    """
    The function translates French to English
    """

    fr_to_en = language_translator.translate(
                            text=french_text,
                            model_id='fr-en').get_result()
    english_text = fr_to_en.get("translations")[0].get("translation")
    return english_text
