# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

import os

version = '1.0'
long_description = open("README.txt").read() + "\n" + \
    open(os.path.join("docs", "INSTALL.txt")).read() + "\n" + \
    open(os.path.join("docs", "CREDITS.txt")).read() + "\n" + \
    open(os.path.join("docs", "HISTORY.txt")).read()

setup(
    name='lajornada.portal.policy',
    version=version,
    description="Policy package for La Jornada portal.",
    long_description=long_description,
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary",
        "Topic :: Multimedia",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='',
    author='Héctor Velarde',
    author_email='hector.velarde@gmail.com',
    url='https://bitbucket.org/simplesconsultoria/lajornada.portal.policy',
    license='GPLv2',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['lajornada', 'lajornada.portal'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'collective.cover',
        'collective.disqus',
        'collective.googlenews',
        'collective.newsflash',
        'collective.nitf',
        'collective.polls',
        'collective.syndication',
        'collective.upload',
        'five.pt',
        'Pillow',
        'Plone',
        'plone.app.upgrade',
        'Products.PloneFormGen',
        'Products.PloneKeywordManager',
        's17.person',
        'sc.behavior.journalist',
        'sc.collapsible.edit',
        'sc.contentrules.groupbydate',
        'sc.contentrules.metadata',
        'sc.embedder',
        'sc.galleria.support',
        'sc.periodicals',
        'sc.social.like',
        'setuptools',
    ],
    extras_require={'test': ['plone.app.testing']},
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
