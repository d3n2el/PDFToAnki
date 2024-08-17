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
    updated_words_it= words_it.split(" ")
    updated_text= text.split(" ")
    model_id = random.randrange(1 << 30, 1 << 31)
    deck_id = random.randrange(1 << 30, 1 << 31)
    my_model = genanki.Model(
        model_id,
        'Linguistics',
        fields=[
        {'name': 'Spanish'},
        {'name': 'Italian'},                               
    ],
    templates=[
        {
        'name': 'Card 1',
        'qfmt': '{{Spanish}}',              
        'afmt': '{{FrontSide}}<hr id="answer">{{Italian}}',
        },
    ] )
    my_deck = genanki.Deck(
        deck_id,
        'Espanol palabras')
    try:
        q= len(updated_text)
        for i in range(q):
            my_note= genanki.Note(
            model= my_model,
            fields= [text,words_it] 
            )
            my_deck.add_note(my_note)
        genanki.Package(my_deck).write_to_file("output.apkg")  
    except Exception as e:
        print(f"An error occurred: {e}")

def trans(text):
    translator = Translator()
    translation= translator.translate(text, dest= "it")
    return translation.text


#rn it just creates the same card 9 times. i wanna die

main()