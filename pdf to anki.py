from PyPDF2 import PdfReader
import sys
from googletrans import Translator
from gtts import gTTS
import genanki
import os
import random


def main():
    file = sys.argv[1]
    reader = PdfReader(file)
    page = reader.pages[0]
    text = page.extract_text()
    words_it = trans(text)
    updated_words_it = words_it.split("\n")
    updated_text = text.split("\n")
    model_id = random.randrange(1 << 30, 1 << 31)
    deck_id = random.randrange(1 << 30, 1 << 31)
    my_model = genanki.Model(
        model_id,
        "Linguistics",
        fields=[{"name": "Spanish"}, {"name": "Italian"}, {"name": "Audio"}],
        templates=[
            {
                "name": "Card 1",
                "qfmt": "{{Spanish}}<br>{{Audio}}",
                "afmt": '{{FrontSide}}<hr id="answer">{{Italian}}',
            },
        ],
    )
    my_deck = genanki.Deck(deck_id, "Espanol palabras")
    audio_path = "audio.mp3"
    try:
        for i, q in zip(updated_words_it, updated_text, strict=True):
            create_audio(q, audio_path)
            my_note = genanki.Note(model=my_model, fields=[q, i, "[sound:audio.mp3]"])
            my_deck.add_note(my_note)
        package = genanki.Package(my_deck)
        package.media_files = [audio_path]
        package.write_to_file("output.apkg")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_audio(input, output):
    try:
        tts = gTTS(input, lang="es")
        tts.save(output)
    except Exception as e:
        print(f"an error has occured: {e}")
    else:
        print(f"Saved audio as {output}")


def trans(text):
    translator = Translator()
    translation = translator.translate(text, dest="it")
    return translation.text


# audio is generated(at least it tells me so) but cant send it to anki

main()
