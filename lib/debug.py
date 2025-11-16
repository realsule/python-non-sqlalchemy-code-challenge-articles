#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Article, Author, Magazine

if __name__ == '__main__':
    print("HELLO! :) Let's debug :vibing_potato:")

    # ---------- Sample Data for Testing ----------
    # Create authors
    author1 = Author("Sule")
    author2 = Author("Jane")

    # Create magazines
    mag1 = Magazine("UrbanMag", "Lifestyle")
    mag2 = Magazine("TechToday", "Technology")

    # Create articles
    art1 = Article(author1, mag1, "How To Build A Clothing Brand")
    art2 = Article(author1, mag2, "Python for Beginners")
    art3 = Article(author2, mag1, "Street Style Trends 2025")
    art4 = Article(author2, mag1, "Urban Photography Tips")

    # ---------- Example Checks ----------
    print("\nAll articles by Sule:")
    print([a.title for a in author1.articles()])

    print("\nMagazines Jane contributed to:")
    print([m.name for m in author2.magazines()])

    print("\nAll articles in UrbanMag:")
    print([a.title for a in mag1.articles()])

    print("\nContributors to UrbanMag:")
    print([a.name for a in mag1.contributors()])

    # ---------- Start debugger ----------
    ipdb.set_trace()

