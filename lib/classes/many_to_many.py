class Article:
    all = []

    def __init__(self, author, magazine, title):
        # Validate input 
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be string 5-50 chars")
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self.name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        Article(self, magazine, title)

    def topic_areas(self):
        return list({mag.category for mag in self.magazines()})


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be 2-16 chars")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be non-empty string")
        self.name = name
        self.category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        # Authors who have more than 1 article
        authors = [article.author for article in self.articles()]
        return list({author for author in authors if authors.count(author) > 1})
