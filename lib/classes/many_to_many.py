class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")

        self.author = author
        self.magazine = magazine
        self._title = title

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # Title is immutable; ignore reassignment
        pass


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Name is immutable; ignore reassignment
        pass

    def articles(self):
        return [a for a in Article.all if a.author == self]

    def magazines(self):
        return list({a.magazine for a in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        return list({m.category for m in mags})


class Magazine:
    all = []

    def __init__(self, name, category):
        self._name = None
        self._category = None

        self.name = name
        self.category = category

        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if isinstance(val, str) and 2 <= len(val) <= 16:
            self._name = val

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, val):
        if isinstance(val, str) and len(val) > 0:
            self._category = val

    def articles(self):
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        return list({a.author for a in self.articles()})

    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [a.title for a in arts]

    def contributing_authors(self):
        arts = self.articles()
        if not arts:
            return None

        authors = [a.author for a in arts]
        result = [auth for auth in set(authors) if authors.count(auth) > 2]

        return result if result else None
