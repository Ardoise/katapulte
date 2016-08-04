#!/usr/bin/env python
import sys

for arg in sys.argv:
  if arg in ("-h"):
    print("help");
  elif arg == '-1':
    print("usage 1");
  elif arg == '-2':
    print("usage 2");
