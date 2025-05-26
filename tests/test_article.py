import pytest
from lib.models.author import Author
from lib.models.article import Article
from lib.models.magazine import Magazine

class TestArticle:
    def test_article_has_author_magazine_and_title(self):
        author = Author("Victor")
        magazine = Magazine("Tech Today", "Technology")
        article = Article(author, magazine, "The Rise of AI")

        assert article.author == author
        assert article.magazine == magazine
        assert article.title == "The Rise of AI"

    def test_article_title_validation(self):
        author = Author("Victor")
        magazine = Magazine("Tech Today", "Technology")
        with pytest.raises(Exception):
            Article(author, magazine, "")  # empty title

    def test_article_title_is_mutable(self):
        author = Author("Victor")
        magazine = Magazine("Tech Today", "Technology")
        article = Article(author, magazine, "Old Title")
        article.title = "New Title"
        assert article.title == "New Title"
