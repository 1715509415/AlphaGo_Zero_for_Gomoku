#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
if (sys.version_info > (3, 0)):
  # Python 3 code in this block
  import _pickle as pickle
else:
  import cPickle as pickle

if (len(sys.argv) > 1):
  print pickle.load(open(sys.argv[1], 'rb'))
else:
  print "Usage: {} model_file".format(sys.argv[0])
