import genanki
import requests

def fetch_word_definitions(word):
    word = word.lower()
    url = f"https://api.datamuse.com/words?sp={word}&md=d"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for res in data:
            if res['word'] == word:
                definitions = res['defs']
                break
        return definitions
    return None

def create_anki_deck(file_path):
    # Read words from the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file if line.strip()]

    total_words = len(words)
    count = 0

    # Create a new Anki deck
    deck_model = genanki.Model(
        1607392319,
        'Simple Model',
        fields=[{'name': 'Word'}, {'name': 'Definition'}],
        templates=[{
            'name': 'Card 1',
            'qfmt': '{{Word}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Definition}}',
        }]
    )

    deck = genanki.Deck(2059400110, 'Vocabulary Deck')

    print("Building your Anki Deck... Hang on tight!")

    # Generate Anki notes/cards for each word
    for word in words:
        definitions = fetch_word_definitions(word)

        if definitions:
            # we'll wrap all the word definitions within an ordered list
            final_definition = "<ol>"
            for defi in definitions:
                final_definition += f"<li>{defi}</li>"
            final_definition += "</ol>"

            # make the word bold for better readability
            fmted_word = f"<b>{word}</b>"
        else:
            print(f"Unable to fetch definitions for '{word}'. Skipping...")
            continue

        note = genanki.Note(
            model=deck_model,
            fields=[fmted_word, final_definition]
        )

        deck.add_note(note)

        count += 1
        print(f"{count}/{total_words} words processed...") # keeping track of the progress

    # Create an Anki package and save it as a .apkg file
    package = genanki.Package(deck)
    package.write_to_file('vocabulary_deck.apkg')
    print('Anki deck created successfully.')

# Usage: python ankify.py words.txt
if __name__ == '__main__':
    import sys
    file_path = sys.argv[1]
    create_anki_deck(file_path)
