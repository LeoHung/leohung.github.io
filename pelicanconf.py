#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'leohung'
SITENAME = u'LeoHung.self()'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
MENUITEMS = (('Education', '#education'),
         ('Experience', '#experience'),
         ('Projects', '#projects'),
         ('Skills', '#skills'),
         ('Publication', '#publication'),
         ('Blog', 'archives.html')
         )

# Social widget
SOCIAL = (('github', 'https://github.com/LeoHung'),
          )

DEFAULT_PAGINATION = 10

STATIC = ["images", "publication", "CNAME"]
STATIC_PATHS = ["images", "publication", "CNAME"]

COVER_IMG_URL = "/images/cover.jpg"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
