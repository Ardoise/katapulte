#!/usr/bin/env python
import sys
import getopt

def main(argv):           
  print("un");
  try:               
    opts, args = getopt.getopt(argv, "hg:d", ["help", "grammar="])
  except getopt.GetoptError:
    print("help");
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      print("help detect: usage()");
      sys.exit()
    elif opt == '-d':
      print("debug detect");
      global _debug
      _debug = 1
    elif opt in ("-g", "--grammar"):
      grammar = arg

if __name__ == "__main__":
  #main(sys.argv[1:])
  main(sys.argv[1:])