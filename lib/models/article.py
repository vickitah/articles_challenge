class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if type(value) is str and 5 <= len(value) <= 50:
            self._title = value
        else:
            raise ValueError("Title must be a string between 5 and 50 characters")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from .author import Author
        if isinstance(value, Author):
            self._author = value
        else:
            raise TypeError("Author must be an instance of Author")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from .magazine import Magazine
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise TypeError("Magazine must be an instance of Magazine")
