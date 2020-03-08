from article_synchronizer.collector.boostnote import *


def test_get_articles():
    articles_dir = '/Users/xiaojueguan/Boostnote'
    boostnote = BoostnoteCollector()
    articles = boostnote.get_articles(articles_dir)
    print(articles['0c762b83-9100-4e72-a78a-62a4d49d2864.cson'])



test_get_articles()