#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#
# About the site
#
AUTHOR = u'Michael Hanke & Alex Waite'
SITETITLE = u'Psycho&shy;informatics'
SITESUBTITLE = u'at <a href="http://www.ipsy.ovgu.de">OvGU</a>'
SITENAME = u'psychoinformatics.de'
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
MENUITEMS = (('Home', 'index.html'),
             ('People', 'lab-members.html'),
             ('Research', 'research.html'),
             ('Software', 'software.html'),
             ('Publications', 'publications.html'),
             ('Contact', 'contact.html'),
)
#LINKS = ()
SOCIAL = (('github', 'https://github.com/psychoinformatics-de'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# External Jazz
#GOOGLE_ANALYTICS = 'UA-79713963-1'
