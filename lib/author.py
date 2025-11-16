from .article import Article

class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters.")
        
        # name should not change after initialization
        if hasattr(self, "_name"):
            raise AttributeError("Name cannot be changed.")
        
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        mags = {article.magazine for article in self.articles()}
        return list(mags)
