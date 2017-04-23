#!/usr/bin/env python

from distutils.core import setup
import atproject

setup(
    name="atproject",
    version=atproject.version,
    author="test",
    author_email="<liuyifei0226@gmail.com>",
    url="https://github.com/atproject/",
    description="John Hoffman's fork of the original bittorrent",
    license="MIT",

    packages=["atproject",
    		"atproject.Application",
              "atproject.Client",
              "atproject.Meta",
              "atproject.Network",
              "atproject.Storage",
              "atproject.Tracker",
              "atproject.Types"],

    scripts=["academictorrents.py"]
)
