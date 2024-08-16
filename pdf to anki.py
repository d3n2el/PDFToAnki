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
    x = create_audio(text)

def create_audio(words):
    tts = gTTS(words, lang="es", tld="es")
    filename = f"{words}.mp3"
    try:
        tts.save(filename)
        print(f"Audio saved as {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

def trans(text):
    translator = Translator()
    translation= translator.translate(text, dest= "it")
    return translation.text

    

main()