#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys
sys.path.append('.')

import customfilters

JINJA_FILTERS = {'menu_filter':customfilters.menu_filter,
                 'close_html_tags':customfilters.close_html_tags }

AUTHOR = u'OSUOSL'
SITENAME = u'OSU Open Source Lab'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_DATE_FORMAT = '%B %e, %Y'

DEFAULT_LANG = u'en'

# Address and contact info
NAME_ABBREV = u'OSL'
ROOM = u'B211'
BUILDING = u'Kerr Admin'
STREET_ADDRESS = u'1500 SW Jefferson Avenue'
EMAIL = [{'description': u'General inquiries',
          'address': u'info@osuosl.org'},
         {'description': u'Support for project infrastructure',
          'address': u'support@osuosl.org'},
         {'description': u'Questions about donations',
          'address': u'donations@osuosl.org'}]
PHONE_NUM = u'541-737-9900'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None

DEFAULT_PAGINATION = 5

DIRECT_TEMPLATES = ['index', 'search/index']
PAGINATED_DIRECT_TEMPLATES = ['blog']

DIRECT_TEMPLATE_INFO = [
        {'parent': u'top', 'link': '/blog', 'name': 'Blog', 'weight': 5, 'children': []}]

THEME = 'dougfir-pelican-theme'

CATEGORY_URL = 'blog/{slug}'
CATEGORY_SAVE_AS = 'blog/index.html'
ARTICLE_PATHS = ['blog/posts/']
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
ARTICLE_ORDER_BY = 'reversed-date'
PAGE_PATHS = ['about', 'services', 'donate', 'blog', 'forms']
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}'
DEFAULT_DATE = 'fs'
USE_FOLDER_AS_CATEGORY = True

# Social media
TWITTERURL = 'http://twitter.com/osuosl'
FACEBOOKURL = 'http://facebook.com/osuosl'
GITHUBURL = 'https://github.com/osuosl'
YOUTUBEURL = 'http://youtube.com/osuopensourcelab'
GPLUSURL = 'https://plus.google.com/107361178205293595706?rel=author'

DEP_NAME = 'OSU Open Source Lab'
PARENT_ORG = 'Center for Applied Systems & Software'
PARENT_ORG_URL = 'http://cass.oregonstate.edu/'
SITELOGO = 'osllogo-web_0.png'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISABLE_SIDEBAR = True
