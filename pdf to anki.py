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
    audio_path= "audio.mp3"
    x = create_audio(text, audio_path)

def create_audio(words, output_path):
    tts = gTTS(words, lang="es", tld="es")
    try:
        tts.save(output_path)
        print(f"Audio saved as {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def trans(text):
    translator = Translator()
    translation= translator.translate(text, dest= "it")
    return translation.text

#in this version i finally managed to get gtts to create the audio
#now the problem is understanding where is that file(and therefore changing directories) and make a dynamic naming system

main()