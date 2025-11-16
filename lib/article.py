class Article:
    all = []

    def __init__(self, author, magazine, title):

        # validate title
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        if not 5 <= len(title) <= 50:
            raise ValueError("Title must be between 5 and 50 chars.")

        # title should not change
        if hasattr(self, "_title"):
            raise AttributeError("Cannot modify title.")
        self._title = title

        # validate relationships
        self.author = author
        self.magazine = magazine

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        from .author import Author
        if not isinstance(value, Author):
            raise ValueError("Author must be an Author instance.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        from .magazine import Magazine
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be a Magazine instance.")
        self._magazine = value
