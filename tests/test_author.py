import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

class TestAuthor:
    def test_author_has_name(self):
        author = Author("Victor")
        assert author.name == "Victor"

    def test_name_must_be_string(self):
        with pytest.raises(Exception):
            Author(123)

    def test_name_is_read_only(self):
        author = Author("Victor")
        with pytest.raises(AttributeError):
            author.name = "New Name"

    def test_author_articles(self):
        author = Author("Victor")
        mag = Magazine("Vibe", "Lifestyle")
        art1 = Article(author, mag, "Living Free")
        art2 = Article(author, mag, "Chasing Dreams")
        assert art1 in author.articles()
        assert art2 in author.articles()

    def test_author_magazines(self):
        author = Author("Victor")
        mag1 = Magazine("Vibe", "Lifestyle")
        mag2 = Magazine("Buzz", "Culture")
        Article(author, mag1, "Living Free")
        Article(author, mag2, "Chasing Dreams")
        assert mag1 in author.magazines()
        assert mag2 in author.magazines()

    def test_add_article(self):
        author = Author("Victor")
        mag = Magazine("Pulse", "Tech")
        article = author.add_article(mag, "AI Boom")
        assert article in author.articles()
        assert article.title == "AI Boom"

    def test_topic_areas(self):
        author = Author("Victor")
        mag1 = Magazine("Vibe", "Lifestyle")
        mag2 = Magazine("Pulse", "Tech")
        Article(author, mag1, "Article 1")
        Article(author, mag2, "Article 2")
        assert "Lifestyle" in author.topic_areas()
        assert "Tech" in author.topic_areas()
