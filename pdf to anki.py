from PyPDF2 import PdfReader
from googletrans import Translator
from fonemas import Transcription
import gtts
import genanki
def main():
    read_pdf("sample.pdf")
    extracted_text= reader.extract_text()
    words_it = trans(extracted_text)

def create_transcription(words):
    object= Transcription(words)
    return object

def trans(text):
    translator = Translator()
    translation= translator.translate(extracted_text, dest= "it")
    return translation


def read_pdf(sample):
    reader= PdfReader(sample)
