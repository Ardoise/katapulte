#!/usr/bin/env python

print('cd dirname $0');

import sys
  #ARG0=sys.argv[0];
  #print(ARG0);
print(sys.argv[0]);
  #print(sys.argv[1]);

## for arg in $@; do
##  print($arg);
## done
print(str(sys.argv));
print(len(sys.argv));
for arg in sys.argv:
  print(arg);


import os.path
  #bn=os.path.basename(ARG0);
  #dn=os.path.dirname(ARG0);
  #print(bn);
  #print(dn);
# print(__file__);
# print(__main__);

print(os.path.basename(sys.argv[0]));
print(os.path.dirname(sys.argv[0]));

print(os.getcwd());
os.chdir(os.path.dirname(sys.argv[0]));
print(os.getcwd());
