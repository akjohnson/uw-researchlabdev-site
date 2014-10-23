#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Lab Devs'
SITENAME = u'UW Research Lab Devs'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('UW', 'http://www.washington.edu/'),
         ('Software Carpentry', 'http://software-carpentry.org/'))

# Social widget
SOCIAL = (('Mailing List', 'https://mailman1.u.washington.edu/mailman/listinfo/research_lab_devs'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Specify a customized theme, via path relative to the settings file
THEME = "themes/uw-foundation"
