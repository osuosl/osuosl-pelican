#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys

sys.path.append('.')

import customfilters  # noqa

JINJA_FILTERS = {'menu_filter': customfilters.menu_filter,
                 'close_html_tags': customfilters.close_html_tags}

AUTHOR = u'OSU OSL'
SITENAME = u'OSU Open Source Lab'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_DATE_FORMAT = '%B %e, %Y'

DEFAULT_LANG = u'en'

# Address and contact info
NAME_ABBREV = u'OSL'
BUILDING = u'224 Milne Computer Center'
STREET_ADDRESS = u'1800 SW Campus Way'
CITY_ZIP = u'Corvallis, OR 97331'
EMAIL = [{'description': u'General inquiries',
          'address': u'info@osuosl.org'}]
PHONE_NUM = u'541-737-9900'

IS_CASS = False
IS_OSL = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None

DEFAULT_PAGINATION = 5

# use these specific templates from the theme to render these content types
DIRECT_TEMPLATES = ['index', 'search/index', 'tags', 'tag']

# use pagination for these content types
PAGINATED_DIRECT_TEMPLATES = ['blog', 'tags']

DIRECT_TEMPLATE_INFO = [
        {'parent': u'top', 'link': '/blog', 'name': 'Blog', 'weight': 5, 'children': []}]  # noqa

DONATE_LINK = 'http://osuosl.org/donate'

THEME = 'dougfir-pelican-theme'
FONT = 'http://fonts.googleapis.com/css?family=Gudea'
FEATURED = u'featured-stories'
SLIDESHOW_LIMIT = 5
OSL_HOME_EXTRAS = True
FRONTPAGE = u'frontpage'

# Gudea Font
FONT = 'https://fonts.googleapis.com/css?family=Gudea'

# categories live at /blog
CATEGORY_URL = 'blog/{slug}'
CATEGORY_SAVE_AS = 'blog/index.html'

# gather the articles from the blog/posts directory
ARTICLE_PATHS = ['blog/posts/']

# find the articles at SITE_URL/blog/{ slug }
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
ARTICLE_ORDER_BY = 'reversed-date'

# the index of all tags
TAGS_URL = 'tag/'
TAGS_SAVE_AS = 'tag/index.html'

# tagged articles are organized under SITE_URL/tag/
TAG_PREFIX = 'tag'
TAG_URL = TAG_PREFIX + '/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# exclude articles with this tag from the blog
EXCLUDE_TAG = 'no-blog'

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

GOOGLE_ANALYTICS = 'UA-537692-1'

DEP_NAME = 'OSU Open Source Lab'
PARENT_ORG = 'Center for Applied Systems & Software'
PARENT_ORG_URL = 'http://cass.oregonstate.edu/'
OSLLOGO = 'osllogo-web_0.png'
SITELOGO = 'milne_street.png'
SITELOG_URL = 'https://www.google.com/maps/place/Milne+Computer+Center,+1800+SW+Campus+Way,+Corvallis,+OR+97331'  # noqa
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DISABLE_SIDEBAR = True
