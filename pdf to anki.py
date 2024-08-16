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
    page= reader.pages[0]   
    text = page.extract_text()
    words_it = trans(text)
    print(words_it)
    pronunciation= create_transcription(text)
    print(pronunciation)


def create_transcription(words):
    transcription= Transcription(words)
    return transcription

def trans(text):
    translator = Translator()
    translation= translator.translate(text, dest= "it")
    return translation.text

    

main()