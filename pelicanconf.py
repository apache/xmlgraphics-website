#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pelican.readers import MarkdownReader
import os

AUTHOR = u'XMLGRAPHICS'
SITENAME = u'XMLGRAPHICS'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS=['./theme/plugins']
PLUGINS=[]

PATH_METADATA = '(?P<path_no_ext>.*)\..*'
ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = '{path_no_ext}.html'
MarkdownReader.file_extensions.append('mdtext')
THEME = 'theme'
PAGE_PATHS = ['.']
INDEX_SAVE_AS = 'articlesignore.html'

STATIC_PATHS = []
for root, _, _ in os.walk(PATH):
    basepath = root.replace(PATH + os.sep, '')
    for adir in ['css', 'js', 'images', 'fo', 'svg', 'schema', 'stylesets']:
        STATIC_PATHS.append(os.path.join(basepath, adir))

#MARKDOWN = {
#    'extensions': ['mdx_include']
#}
