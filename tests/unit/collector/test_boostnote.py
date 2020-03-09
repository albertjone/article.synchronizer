from article_synchronizer.collector.boostnote import *


articles_dir = '/Users/xiaojueguan/Boostnote'
articles_dir = '/Users/steveguan/code/Interest/Boostnote'


def test_get_articles():
    boostnote = BoostnoteCollector()
    articles = boostnote.get_article_dict(articles_dir)
    print(articles['0c762b83-9100-4e72-a78a-62a4d49d2864.cson'])



test_get_articles()
