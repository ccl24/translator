import translator
from googletrans import Translator

def translate(text):
    translator = Translator()
    translation = translator.translate(text=text, dest='fr')    # translation is an object
    return translation.text

def detect(text):
    translator = Translator()
    language_detected = translator.detect(text=text)
    return language_detected.lang.upper()