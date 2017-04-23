#!/usr/bin/env python

from distutils.core import setup
import att

setup(
    name="atproject",
    version=att.version,
    author="Chris Markiewicz, Bram Cohen, John Hoffman, Uoti Arpala et. al.",
    author_email="<effigies@gmail.com>",
    url="https://github.com/effigies/att",
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
