from PyPDF2 import PdfReader
import sys
from googletrans import Translator
from fonemas import Transcription
from gtts import gTTS
import genanki
import os
def main():
    file= sys.argv[1]
    reader = PdfReader(f"C:/Users/Danzel/Documents/pdf files/{file}")
    for page in reader.pages():
        text = page.extract_text()
    extracted_text= reader.extract_text()
    print(extracted_text)
    words_it = trans(extracted_text)
    print(words_it)
    pronunciation= create_transcription(extracted_text)
    print(pronunciation)


def create_transcription(words):
    object= Transcription(words)
    return object

def trans(text):
    translator = Translator()
    translation= translator.translate(extracted_text, dest= "it")
    return translation
def send_anki(deck):


main()