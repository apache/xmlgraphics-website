#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pelican.readers import MarkdownReader
import os
from markdown import Markdown
from pelican.utils import pelican_open

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
READERS = {'html': None}

fop_current_version = '2.7'
batik_current_version = '1.15'
fop_minimal_java_requirement = '1.7'
fop_current_version_release_date = '20 Jan 2022'

def read(self, source_path):
    self._source_path = source_path
    self._md = Markdown(**self.settings['MARKDOWN'])
    with pelican_open(source_path) as text:
        text = text.replace('{{ fop_current_version }}', fop_current_version).replace('{{ batik_current_version }}', batik_current_version).replace('{{ fop_minimal_java_requirement }}', fop_minimal_java_requirement).replace('{{ fop_current_version_release_date }}', fop_current_version_release_date)
        content = self._md.convert(text)
    if hasattr(self._md, 'Meta'):
        metadata = self._parse_metadata(self._md.Meta)
    else:
        metadata = {}
    return content, metadata
MarkdownReader.read = read    

STATIC_PATHS = ['.']
for root, _, _ in os.walk(PATH):
    for adir in ['css', 'js', 'images', 'fo', 'svg', 'schema', 'stylesets', 'demo', 'javadoc']:
        STATIC_PATHS.append(os.path.join(root, adir).replace(PATH + os.sep, ''))

#MARKDOWN = {
#    'extensions': ['mdx_include']
#}
