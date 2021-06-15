#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#
# About the site
#
AUTHOR = 'Michael Hanke & Alex Waite'
SITETITLE = 'Psycho&shy;informatics'
SITESUBTITLE = 'at <a href="http://www.fz-juelich.de/inm/inm-7/EN/Home/home_node.html">Jülich</a>'
SITENAME = 'Psychoinformatics'
SITEURL = ''

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'

#
# Configure Pelican a bit
#
PATH = 'content'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [ 'sitemap' ]
SITEMAP = { 'format': 'xml' }

DIRECT_TEMPLATES = ['404']  # unset all templates; add 404
THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None

#
# Configure the site
#
STATIC_PATHS = ['img']
MENUITEMS = (('home', 'index.html'),
             ('people', 'lab-members.html'),
             ('research', 'research.html'),
             ('software', 'software.html'),
             ('teaching', 'teaching.html'),
             ('publications', 'publications.html'),
             ('contact', 'contact.html'),
)

DEFAULT_PAGINATION = False

# We prefer document-relative URLs
RELATIVE_URLS = True
