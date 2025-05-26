class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not (isinstance(value, str) and 2 <= len(value) <= 16):
          print(f"Invalid name detected: {value}")  # debug line
          raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value


    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not (isinstance(value, str) and len(value.strip()) > 0):
            raise ValueError("Category must be a non-empty string.")
        self._category = value.strip()

    def articles(self):
        from .article import Article
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1
        return [author for author, count in author_count.items() if count > 2] or None
