# Copyright 2011 Digital Inspiration
# http://www.labnol.org/

import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

class MainHandler(webapp.RequestHandler):
  def get (self, q):
    if q is None:
      q = 'index.html'

    path = os.path.join (os.path.dirname (__file__) + "/templates/", "main.html")
    content = os.path.join (os.path.dirname (__file__) + "/publish/", q)
    self.response.headers ['Content-Type'] = 'text/html'
    ctx = {
            'content': content,
        }

    self.response.out.write (template.render (path, ctx))

def main ():
  application = webapp.WSGIApplication ([('/(.*html)?', MainHandler)], debug=True)
  util.run_wsgi_app (application)

if __name__ == '__main__':
  main ()