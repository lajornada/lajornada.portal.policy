# -*- coding: utf-8 -*-

from lajornada.portal.policy.testing import INTEGRATION_TESTING

import unittest


class PortalPropertiesTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.properties = self.portal['portal_properties'].site_properties
        self.navtree = self.portal['portal_properties'].navtree_properties
        self.types = self.portal['portal_types']

    def test_localTimeFormat(self):
        self.assertEqual(self.properties.localTimeFormat, '%d/%m/%Y')

    def test_localLongTimeFormat(self):
        self.assertEqual(self.properties.localLongTimeFormat, '%d/%m/%Y %H:%M')

    def test_enable_link_integrity_checks_enabled(self):
        self.assertTrue(self.properties.enable_link_integrity_checks)

    def test_livesearch_disabled(self):
        self.assertFalse(self.properties.enable_livesearch)

    def test_default_language(self):
        self.assertEqual(self.properties.default_language, 'es')

    def test_default_charset(self):
        self.assertEqual(self.properties.default_charset, 'utf-8')

    def test_types_searched(self):
        all_types = set(self.types.listContentTypes())
        types_not_searched = set(self.properties.types_not_searched)
        types_searched = list(all_types - types_not_searched)
        types_searched.sort()
        types_expected = [
            'collective.nitf.content',
        ]
        self.assertListEqual(types_searched, types_expected)

    def test_metaTypesNotToList(self):
        metaTypesNotToList = list(self.navtree.metaTypesNotToList)
        metaTypesNotToList.sort()
        types_expected = [
            'Discussion Item',
            'Event',
            'File',
            'Image',
            'News Item',
            'Page',
            'collective.nitf.content',
            'collective.polls.poll',
        ]
        self.assertListEqual(metaTypesNotToList, types_expected)
