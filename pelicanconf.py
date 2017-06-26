#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mike Hughes'
SITENAME = u'Machine Learning for Health'
SITEURL = 'https://ml4health.github.io/2017'

OUTPUT_PATH = '2017/'
PATH = 'content_2017/'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/customized-pelican-alchemy/alchemy'

SITEIMAGE = '/images/logo.png'

STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# Theme-specific settings
SITESUBTITLE = 'Workshop at NIPS 2017'
DISPLAY_ARCHIVES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

DESCRIPTION = 'TODO'
# Links
LINKS = []
#LINKS = ()
#        ('somedates', 'call-for-papers.html#dates'),
#        ('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#        )
ICONS = ()
SOCIAL = ()
HIDE_AUTHORS = True

