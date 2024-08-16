from PyPDF2 import PdfReader
from googletrans import Translator
from fonemas import Transcription
from gtts import gTTS
import genanki
import os
print(os.getcwd())
def main():
    reader = PdfReader("example.pdf")
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


def read_pdf(sample):
    reader= PdfReader(sample)

main()