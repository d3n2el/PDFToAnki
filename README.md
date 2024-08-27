
# PDF TO ANKI

This project is a Python-based script that automates the creation of language-learning flashcards using text extracted from a PDF document. The script leverages several powerful libraries, including PyPDF2 for PDF text extraction, googletrans for translation, gtts for text-to-speech conversion, and genanki for generating Anki flashcards. The overall goal is to transform a segment of text from a PDF file into an interactive, multi-language flashcard deck, complete with translations and audio pronunciations, that can be used for language learning in Anki.
## Core Functionality

The script begins by accepting user inputs for the source language, target language, and the name of the Anki deck to be created. It then reads the first page of a PDF file specified as a command-line argument. The extracted text from the PDF is then translated into the desired target language using the Google Translate API via the googletrans library. The text is split into individual lines, creating pairs of the original and translated text.
## Anki Deck Creation

Anki is a popular flashcard application that uses spaced repetition to help users remember information over time. The genanki library allows the script to create a custom Anki deck based on the input text and translations. Each flashcard is composed of a question (the original text), an answer (the translated text), and an audio file that provides the pronunciation of the original text(for better memory retention and proper understanding of the words).

To build this deck, the program first generates a unique model and deck ID, ensuring that each flashcard deck is distinct. It then defines the structure of the flashcards, specifying that each card should display the question (original text) along with an audio file for pronunciation on the front, and the translation on the back.
## Audio Generation

For the audio component, the script uses the gtts (Google Text-to-Speech) library to generate audio files of the original text. Each line of text is converted into speech in the source language and saved as an MP3 file. These audio files are linked to the corresponding flashcards, enhancing the learning experience by providing auditory reinforcement. The filenames of the audio files are sanitized to remove any special characters that might cause issues in file handling which brings me to:
## Error Handling and Execution

The script includes basic error handling to manage exceptions that might occur during translation or audio generation. If an error occurs at any point during the process, an error message is printed, and the script attempts to continue processing the remaining text. I made it so that the script tries to give the end user a description of the problem at hand to try to properly solve it without the need to touch the program itself.

## Final Result
Once all the flashcards are created, the script packages the deck(made of the original text and the translated words) and associated media files (audio files) into an .apkg file, which can be imported directly into Anki. The final product is a comprehensive flashcard deck that allows users to study the original text and its translation, while also listening to the correct pronunciation.