import pytest
from lib.models.author import Author
from lib.models.article import Article
from lib.models.magazine import Magazine

class TestMagazine:
    def test_magazine_has_name_and_category(self):
        mag = Magazine("Wired", "Tech")
        assert mag.name == "Wired"
        assert mag.category == "Tech"

    def test_magazine_name_and_category_validation(self):
        with pytest.raises(Exception):
            Magazine("W", "Tech")  # too short name (1 character)
        with pytest.raises(Exception):
            Magazine("Wired", "")   # empty category

    def test_magazine_name_and_category_are_mutable(self):
        mag = Magazine("Wired", "Tech")
        mag.name = "Updated Wired"
        mag.category = "Science"
        assert mag.name == "Updated Wired"
        assert mag.category == "Science"

    def test_magazine_returns_articles(self):
        author = Author("Victor")
        mag = Magazine("Pulse", "Health")
        a1 = Article(author, mag, "Mental Health Matters")
        a2 = Article(author, mag, "Nutrition 101 Basics")
        assert len(mag.articles()) == 2
        assert a1 in mag.articles()
        assert a2 in mag.articles()

    def test_magazine_returns_unique_authors(self):
        author1 = Author("Victor")
        author2 = Author("John")
        mag = Magazine("Pulse", "Health")
        Article(author1, mag, "Valid Title One")
        Article(author2, mag, "Valid Title Two")
        Article(author1, mag, "Valid Title Three")
        contributors = mag.contributors()
        assert len(contributors) == 2
        assert author1 in contributors
        assert author2 in contributors

    def test_magazine_title_list(self):
        author = Author("Victor")
        mag = Magazine("Science Now", "Science")
        Article(author, mag, "First Valid Title")
        Article(author, mag, "Second Valid Title")
        titles = mag.article_titles()
        assert titles == ["First Valid Title", "Second Valid Title"]
