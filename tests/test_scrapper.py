# -*- coding: utf-8 -*-

from .context import textprocessor
from .context import scrapper
from lxml import etree

import unittest
import responses

class ScrapperTestSuite(unittest.TestCase):
    """Test cases for scrapping methods"""

    @responses.activate
    def test_get_articles_by_date_clean(self):
        """Test good articles for a given date"""

        responses.add(responses.GET, 'http://elpais.com/tag/fecha/20170530', body='<html><head><meta charset="utf-8"><title>Foo bar test</title></head><body><h2 class="articulo-titulo"><a href="//google.com/">Sample title</a></h2><h2 class="articulo-titulo"><a href="//github.com/">FooBarFuckSystemd</a></h2></body></html>', status=200, content_type='text/html')

        expected_result = [{u"title": u"Sample title", u"url": u"http://google.com/"}, {u"title": u"FooBarFuckSystemd", u"url": u"http://github.com/"}]

        res = scrapper.get_articles_by_date("30/05/2017")
        self.assertItemsEqual(res, expected_result, "Different lists found")


    @responses.activate
    def test_get_articles_by_date_bad_status_code(self):
        """Test bad status_code when trying to get articles by date"""

        responses.add(responses.GET, 'http://elpais.com/tag/fecha/20170530', body='', status=500, content_type='text/plain')

        with self.assertRaises(Exception) as cm:
            res = scrapper.get_articles_by_date("30/05/2017")

        self.assertEqual("something went wrong, status code != 200 OK. Status code: 500", str(cm.exception), "No exception raised")

    @responses.activate
    def test_get_articles_by_date_bad_body(self):
        """Test bad body when trying to get articles by date"""

        responses.add(responses.GET, 'http://elpais.com/tag/fecha/20170530', body='', status=200, content_type='text/html')

        with self.assertRaises(Exception) as cm:
            res = scrapper.get_articles_by_date("30/05/2017")

        self.assertEqual("body doesn't contain valid HTML", str(cm.exception), "No exception raised")

    @responses.activate
    def test_get_articles_by_date_valid_html_no_articles(self):
        """Test valid HTML response but no articles found"""

        responses.add(responses.GET, 'http://elpais.com/tag/fecha/20170530', body='<html><head><title>Si lees esto ponme un 10 porfaplis</title></head><body><!--Para que quiero enfermedades si ya tengo jQuery--><h1>?</h1></body>', status=200, content_type='text/html')

        res = scrapper.get_articles_by_date("30/05/2017")
        self.assertItemsEqual([], res, "Different lists found")

    def test_invalid_date_format(self):
        """Test get_articles_by_date with an invalid date"""

        with self.assertRaises(Exception) as cm:
            res = scrapper.get_articles_by_date("foobar foo/")

        self.assertEqual("invalid date format", str(cm.exception), "No exception raised")

    @responses.activate
    def test_get_article_body_good_response(self):
        """Test get article body good response"""

        responses.add(responses.GET, 'http://deportes.elpais.com/deportes/2017/05/30/actualidad/1496168226_303249.html', body='<div id="articulo-introduccion"><p>Ejemplo <span>prueba</span></p></div><div class="articulo-cuerpo" id="cuerpo_noticia" itemprop="articleBody"><p>texto de ejemplo</p></div>', status=200, content_type='text/html')

        res = scrapper.get_article_body("http://deportes.elpais.com/deportes/2017/05/30/actualidad/1496168226_303249.html")
        self.assertEqual(res, "texto de ejemplo prueba Ejemplo  ", "Articles content do not match "+res)

    @responses.activate
    def test_get_article_body_bad_status_code(self):
        """Test get article body with bad status code in response"""

        responses.add(responses.GET, 'http://deportes.elpais.com/deportes/2017/05/30/actualidad/1496168226_303249.html', body='', status=500, content_type='text/plain')


        with self.assertRaises(Exception) as cm:
            res = scrapper.get_article_body("http://deportes.elpais.com/deportes/2017/05/30/actualidad/1496168226_303249.html")

        self.assertEqual("something went wrong, status code != 200 OK. Status code: 500", str(cm.exception), "No exception raised")


    @responses.activate
    def test_get_article_body_no_valid_contents(self):
        """Test get article by id when response doesn't contain expected HTML elements"""

        responses.add(responses.GET, 'http://deportes.elpais.com/deportes/2017/05/30/actualidad/1496168226_303249.html', body='<html><head>foo</head><body><div id="jue">aaa</div></body>', status=200, content_type='text/html')

        res = scrapper.get_article_body("http://deportes.elpais.com/deportes/2017/05/30/actualidad/1496168226_303249.html")

        self.assertEqual("", res, "Unexpected return found")

    def test_recursive_get_text_without_children(self):
        root=etree.Element("root")
        root.text="viva cabify"

        expected="viva cabify "

        res=scrapper.recursive_get_text(root)
        self.assertEqual(res,expected, type(root))

    def test_recursive_get_text_with_children(self):
        root=etree.Element("root")
        root.text="viva cabify"

        child=etree.SubElement(root,"child")
        child.text="por supuesto"

        child=etree.SubElement(root,"child2")
        child.text="por supuesto2"

        child=etree.SubElement(child,"child3")
        child.text="por supuesto3"

        expected="por supuesto por supuesto3 por supuesto2 viva cabify "

        res=scrapper.recursive_get_text(root)
        self.assertEqual(res,expected, type(root))

    def test_recursive_get_text_TypeError(self):
        root=1

        with self.assertRaises(TypeError):
            scrapper.recursive_get_text(root)


if __name__ == '__main__':
    unittest.main()
