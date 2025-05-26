## Articles Challenge
This project implements a simple system for managing articles, authors, and magazines, with the following core models:

Author: Represents a writer who can write multiple articles.

Magazine: Represents a publication with a name and category, which can contain many articles.

Article: Represents an article written by an author and published in a magazine.

## Features
Validation of model attributes (e.g., name length, category non-empty, article title length).

Relationships:

Authors can write many articles.

Magazines have many articles.

Articles belong to an author and a magazine.

Methods to retrieve related data such as:

Articles written by an author.

Magazines an author has contributed to.

Contributors of a magazine.

Titles of articles in a magazine.

Authors who have contributed more than twice to a magazine.

## Installation
Clone this repository:


git clone https://github.com/vickitah/articles_challenge.git
cd articles_challenge
 ## Create and activate a virtual environment:

bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies (if any):



## Usage
Run tests to verify everything works:

bash

pytest
Use the models in your Python scripts:

python

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

author = Author("Victor")
magazine = Magazine("Tech Today", "Technology")
article = Article(author, magazine, "Understanding AI and Machine Learning")

print(magazine.contributors())
print(author.articles())
Tests
Tests are written with pytest.

Tests cover model attribute validation, relationship methods, and data retrieval.

## Run tests with:

pytest

## License
MIT License

