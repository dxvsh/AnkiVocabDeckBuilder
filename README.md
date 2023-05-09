# Description
This is a simple Python script that takes a text file containing English words (one on each line) and generates an [Anki](https://apps.ankiweb.net/) 
vocabulary deck out of it such that the front of the card contains the given word and the back contains the meanings/definitions for that word.
That's pretty much it!

# Usage
+ First, install the required dependencies:

	```
	$ pip install genanki requests
	```

+ Run the script:
	
	```
	$ python ankify.py words.txt
	```
	Just replace `words.txt` with the name of your own text file and the script will start working on building your deck. When it's 
	done you should see a `vocabulary_deck.apkg` file in your directory. You can now import your deck into Anki and start improving your vocab!

# Example output card images:
Below are some cards from my vocabulary deck (imported in AnkiDroid) just to demonstrate how the generated cards look like in action:

<p align="left">
  <img src="/images/img1.png" width="350" alt="example-card-1"/>
  <img src="/images/img2.png" width="350" alt="example-card-2"/>
</p>

# Sidenotes:
The script uses the [Datamuse](https://www.datamuse.com/api/) API for fetching the word meanings mainly because its freely available 
to use by anyone without requiring you to register an account unlike most other dictionary APIs which need you to sign up on their platform
just to get their API keys (which are rather rate-limited as well). Also the [genanki](https://github.com/kerrickstaley/genanki) library came in
very handy for programatically generating Anki decks/cards.
