"""Wikipedia-API is easy to use Python wrapper for Wikipedias' API. It supports extracting texts, sections, links,
categories, translations, etc from Wikipedia. Documentation provides code snippets for the most common use cases.

More details: https://github.com/martin-majlis/Wikipedia-API/blob/master/README.rst
"""
import wikipediaapi
from wikipediaapi import PagesDict
import pandas as pd


alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ"
df = pd.DataFrame(columns=["Count"], index=[i for i in alphabet]).fillna(0)


def count_categorymembers(categorymembers: PagesDict):
        """Count category members
        Args:
            categorymembers (PagesDict): 
        Returns:
            None
        """
        for c in categorymembers.values():
            if c.title[0] in alphabet and c.title[0:5] != "Категория":
                df.loc[c.title[0], "Count"] += 1


wiki_wiki = wikipediaapi.Wikipedia('Animals (kripmrx@gmail.com)', 'ru')
page = wiki_wiki.page("Категория:Животные по алфавиту")
count_categorymembers(page.categorymembers)

df.to_csv('beasts.csv', index=True)
