#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#
# About the site
#
AUTHOR = u'Michael Hanke & Alex Waite'
SITETITLE = u'Psyschoinformatics'
SITESUBTITLE = u'at OvGU'
SITEURL = ''

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = u'en'
LOCALE = u'en_US.UTF-8'

#
# Configure Pelican a bit
#
PLUGIN_PATHS = ['pelican-plugins']
#PLUGINS = []

THEME = 'pelican-theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#
# Configure the site
#
STATIC_PATHS = ['img']
MENUITEMS = (('Home', '/'),
             ('Research', '/research.html'),
             ('Software', '/software.html'),
             ('Members', '/lab-members.html'),
             ('Publications', '/publications.html'),
             ('Contact', '/contact.html'),
)
#LINKS = ()
SOCIAL = (('github', 'https://github.com/psychoinformatics-de'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
