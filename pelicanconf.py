#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'OSUOSL'
SITENAME = u'OSU Open Source Lab'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_DATE_FORMAT = '%B %e, %Y'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None

DEFAULT_PAGINATION = 5

DIRECT_TEMPLATES = ['index', 'request-hosting/index']
PAGINATED_DIRECT_TEMPLATES = ['blog']

THEME = 'osuosl-theme'

STATIC_PATHS = ['img']
STATIC_SAVE_AS = ['theme/img']
CATEGORY_URL = 'blog/{slug}'
CATEGORY_SAVE_AS = 'blog/index.html'
ARTICLE_PATHS = ['blog/posts/']
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
ARTICLE_ORDER_BY = 'date'
PAGE_PATHS = ['about', 'services', 'donate', 'blog']
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}'
DEFAULT_DATE = 'fs'
USE_FOLDER_AS_CATEGORY = True


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
