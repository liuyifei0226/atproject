#!/usr/bin/env python

from distutils.core import setup
import atproject

setup(
    name="atproject",
    version=0.01,
    author="test",
    author_email="<liuyifei0226@gmail.com>",
    url="https://github.com/atproject/",
    description="John Hoffman's fork of the original bittorrent",
    license="MIT",
    py_modules=['academictorrents'],
    package_data={'atproject':['atproject.icons/*']},
    packages=["atproject",
    		  "atproject.Application",
              "atproject.Client",
              "atproject.Meta",
              "atproject.Network",
              "atproject.Storage",
              "atproject.Tracker",
              "atproject.Download"
             ],

    scripts=["academictorrents.py"]
)
