# -*- coding: utf-8 -*-

from lajornada.portal.policy.config import PROJECTNAME
from lajornada.portal.policy.testing import INTEGRATION_TESTING

import unittest

DEPENDENCIES = [
    'collective.cover',
    'collective.disqus',
    'collective.googlenews',
    'collective.newsflash',
    'collective.nitf',
    'collective.polls',
    'collective.syndication',
    'collective.upload',
    'PloneFormGen',
    'PloneKeywordManager',
    's17.person',
    'sc.collapsible.edit',
    'sc.embedder',
    'sc.galleria.support',
    'sc.periodicals',
    'sc.social.like',
]


class InstallTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']

    def test_installed(self):
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME),
                        '%s not installed' % PROJECTNAME)

    def test_dependencies_installed(self):
        expected = set(DEPENDENCIES)
        installed = set(name for name, product in self.qi.items()
                        if product.isInstalled())
        result = sorted(expected - installed)

        self.assertFalse(result,
            "These dependencies are not installed: " + ", ".join(result))
