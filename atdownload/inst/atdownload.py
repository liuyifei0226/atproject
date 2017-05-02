#!/usr/bin/env python
#coding: utf-8
import sys
import atproject.Download.main as dl


obj = dl.CustomLibrary()
path=str(sys.argv[1])
obj.torrent_path = path
path_to_file = obj.get()

print path_to_file

		


		




