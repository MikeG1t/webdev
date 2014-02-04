form="""
<form action = "/testing">
  <label>
    <b>ROT13</b>
    <br><br>
  <input type = 'textarea' value = 'test' name = 'q'>
  <input type = 'submit'>  
  </label>
</form>
"""

class MainPage(webapp2.RequestHandler):

    def get(self):
        #self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(form)

class TestClass(webapp2.RequestHandler):
  def get(self):
    q = self.request.get("q")
    self.response.out.write(q)
        
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testing', TestClass)
], debug=True)