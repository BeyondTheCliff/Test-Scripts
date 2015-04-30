#!/usr/bin/env python
import HTML
import cgi
import cgitb
cgitb.enable()

print "Hello World"

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
say  = html.escape(form["say"].value);
to   = html.escape(form["to"].value);

print(say, " ", to)