# -*- coding: utf-8 -*-

from lajornada.portal.policy.testing import INTEGRATION_TESTING
from collective.cover.controlpanel import ICoverSettings
from collective.googlenews.interfaces import GoogleNewsSettings
from collective.nitf.controlpanel import INITFSettings
from collective.upload.interfaces import IUploadSettings
from plone.app.discussion.interfaces import IDiscussionSettings
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

import unittest


class AddonsSettingsTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.types = self.portal.portal_types
        self.registry = getUtility(IRegistry)
        self.nitf_settings = self.registry.forInterface(INITFSettings)
        self.wt = self.portal['portal_workflow']
        self.pm = self.portal['portal_membership']

    def test_plone_app_discussion_settings(self):
        """Comments must be enabled globally.
        """
        settings = self.registry.forInterface(IDiscussionSettings)
        self.assertTrue(settings.globally_enabled)

    def test_collective_cover_settings(self):
        """Searchable content types on cover.
        """
        settings = self.registry.forInterface(ICoverSettings)
        allowed_types = [
            u'collective.nitf.content',
            u'collective.polls.poll',
            u'Collection',
        ]
        self.assertListEqual(settings.searchable_content_types, allowed_types)

    def test_collective_googlenews_settings(self):
        """Google news settings on News Articles only.
        """
        settings = self.registry.forInterface(GoogleNewsSettings)
        self.assertListEqual(
            settings.portal_types, ['collective.nitf.content'])

    def test_collective_nitf_available_genres(self):
        """Genres used portal wide.
        """
        available_genres = list(self.nitf_settings.available_genres)
        available_genres.sort()
        expected_genres = [
            u'Analysis',
            u'Archive material',
            u'Current',
            u'Exclusive',
            u'From the Scene',
            u'Interview',
            u'Obituary',
            u'Opinion',
            u'Polls and Surveys',
            u'Press Release',
            u'Profile',
            u'Retrospective',
            u'Review',
            u'Special Report',
            u'Summary',
            u'Wrap',
        ]
        self.assertListEqual(available_genres, expected_genres)

    def test_collective_nitf_available_sections(self):
        """News sections defined.
        """
        available_sections = list(self.nitf_settings.available_sections)
        available_sections.sort()
        expected = [
            u'Capital',
            u'Ciencias',
            u'Cultura',
            u'Deportes',
            u'Economía',
            u'Espectáculos',
            u'Estados',
            u'Mundo',
            u'Política',
            u'Sociedad y Justicia',
        ]
        self.assertListEqual(available_sections, expected)

    def test_collective_nitf_default_section(self):
        self.assertEqual(self.nitf_settings.default_section, u'Política')

    def test_allow_discussion_on_news_articles(self):
        ct = 'collective.nitf.content'
        allow_discussion = self.types[ct].allow_discussion
        self.assertTrue(allow_discussion)

    def test_allow_discussion_on_polls(self):
        ct = 'collective.polls.poll'
        allow_discussion = self.types[ct].allow_discussion
        self.assertTrue(allow_discussion)

    def test_collective_upload_settings(self):
        """Images uploaded must be smaller than 1024x1024.
        """
        settings = self.registry.forInterface(IUploadSettings)
        self.assertEqual(settings.resize_max_width, 1024)
        self.assertEqual(settings.resize_max_height, 1024)
        self.assertEqual(settings.upload_extensions,
                         u'gif, jpeg, jpg, png, pdf, doc, txt, docx')

    def test_sc_social_likes_settings(self):
        likes = self.portal['portal_properties'].sc_social_likes_properties
        enabled_portal_types = list(likes.enabled_portal_types)
        enabled_portal_types.sort()
        types_expected = [
            u'collective.nitf.content',
            u'collective.polls.poll',
        ]
        self.assertListEqual(enabled_portal_types, types_expected)
