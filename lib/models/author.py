class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            raise AttributeError("Cannot change author's name")
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Author name must be a non-empty string")
        self._name = value.strip()

    def articles(self):
        from .article import Article
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        from .article import Article
        
        return Article(self, magazine, title)

    def topic_areas(self):
       
        return list({mag.category for mag in self.magazines()})
