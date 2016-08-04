#!/usr/bin/env python
import os

def testd(path):
  if not os.path.exists(path):
    os.makedirs(path)

def testf(path):
  if not os.path.exists(path):
    print("#WARN: file '%s' not found" % path);

testd("/tmp");
testf("/tmp/toto");
  # print(os.path.isdir('/tmp'))
  # print(os.path.isfile('/tmp'))
  # print(os.path.exists('/tmp'))

print(os.getcwd());
os.chdir("/tmp");
print(os.getcwd());


