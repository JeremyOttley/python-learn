#!/usr/bin/env python2.7

import urllib2

req urllib2.Request('http://www.voidspace.org.uk')
response = urllib2.urlopen(req)
the_page = response.read()

f = open("void.html", "w")

for i in the_page:
  f.write(the_page)

f.close()
