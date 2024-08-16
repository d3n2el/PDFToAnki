from PyPDF2 import PdfReader
import sys
from googletrans import Translator
from gtts import gTTS
import genanki
import os
import random
def main():
    file= sys.argv[1]
    reader = PdfReader(f"C:/Users/Danzel/Documents/pdf files/{file}")
    page= reader.pages[0]   
    text = page.extract_text()
    words_it = trans(text)
    audio_path= "audio.mp3"
    create_audio(text, audio_path)
    model_id = random.randrange(1 << 30, 1 << 31)
    deck_id = random.randrange(1 << 30, 1 << 31)
    my_model = genanki.Model(
        model_id,
        'Linguistics',
        fields=[
        {'name': 'Spanish'},
        {'name': 'Italian'},
        {'name': 'AudioFile'}                               
    ],
    templates=[
        {
        'name': 'Card 1',
        'qfmt': '{{Spanish}}<br>{{AudioFile}}',              
        'afmt': '{{FrontSide}}<hr id="answer">{{Italian}}',
        },
    ] )
    my_note= genanki.Note(
        model= my_model,
        fields= [text, words_it,audio_path]
    )
    my_deck = genanki.Deck(
        deck_id,
    'Espanol palabras')
    my_deck.add_note(my_note)
    try:
        my_package = genanki.Package(my_deck)
        my_package.media_files = ['audio.mp3']
        my_package.write_to_file("output.apkg")
    except Exception as e:
        print(f"An error occurred: {e}")


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

#as of rn it doesnt create any problem when i run the program, still dont know where the created files end up but whatever


main()