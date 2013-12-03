#!/usr/bin/env python
import sys
try:  f = open(sys.argv[1])
except IndexError: f = sys.stdin

ll=[l.rstrip() for l in f]
del f

import re

def print_zone(name,prefix):
  for l in (l for l in ll if re.match("-\\w %s\\b"%re.escape(name),l)):
    print prefix+l
    m=re.search("-j (\\w+)\\b",l)
    if m:
      print_zone(m.group(1),prefix+"\t")

r = re.compile("-P (\\w+)\\b")
zz = [r.match(l).group(1) for l in ll if r.match(l)]
for z in zz:
  print_zone(z,"")
  print
