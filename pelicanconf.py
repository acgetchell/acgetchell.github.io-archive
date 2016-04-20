#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Adam Getchell'
SITENAME = u"Adam's Entropy"
SITESUBTITLE = u"One particular random walk through life"
SITEURL = 'http://adamgetchell.org'

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = 'pelican-themes/pelican-bootstrap3'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['gravatar', 'pelican_gist', 'render_math', 'neighbors',
           'tag_cloud', 'related_posts']

# Blogroll
LINKS = (('Mozilla Science Lab', 'http://mozillascience.org'),
         ('Current CDT papers', 'http://arxiv.org/find/all/1/all:+AND+triangulations+AND+causal+dynamical/0/1/0/all/0/1'),)

# Social widget
SOCIAL = (('AboutMe', 'http://about.me/adamgetchell'),
          ('Twitter', 'https://twitter.com/adamgetchell'),
          ('LinkedIn','http://www.linkedin.com/in/adamgetchell'),
          ('GitHub', 'http://github.com/acgetchell'),
          ('LastFM', 'http://www.last.fm/user/adamgetchell'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 9
TAG_CLOUD_BADGE = True
TAG_CLOUD_SORTING = 'random'
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
SHOW_ARTICLE_CATEGORY = True
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
GITHUB_USER = 'acgetchell'
GITHUB_REPO_COUNT = 4
TWITTER_CARDS = True
TWITTER_USERNAME = 'adamgetchell'
TWITTER_WIDGET_ID = 701556215399194624
AVATAR = 'images/adam_ben.jpg'
# BANNER = 'images/adam_ben.jpg'
ABOUT_ME = 'Physics and computing'
STATIC_PATHS = [
    'images',
    'extra/CNAME',
    'extra/favicon.ico',
    'extra/apple-icon-precomposed.png',
    'extra/apple-icon.png'
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/apple-icon': {'path': 'apple-icon.png'},
    'extra/apple-icon-precomposed': {'path': 'apple-icon-precomposed.png'}
}
RESPONSIVE_IMAGES = True
TYPOGRIFY = True
FAVICON = 'favicon.ico'
