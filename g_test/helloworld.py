import webapp2
from encryp import encryp

form="""
<form action = "/" method = "post">
  <label>
    <b>ROT13</b>
    <br><br>
  <textarea cols = "50" rows = "8" name = "text">%(text)s</textarea>
  <input type = 'submit'>  
  </label>
</form>
"""

class MainPage(webapp2.RequestHandler):

    def get(self):
      #a = ""
      #self.response.headers['Content-Type'] = 'text/html'
      self.response.out.write(form % {"text": ""})
      
    def post(self):
      #r = self.request.get("text")
      #h = encryp(self.request.get("text"))

      self.response.out.write(form % {"text": encryp(self.request.get("text"))})
  

        
application = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)