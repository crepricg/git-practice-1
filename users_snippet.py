from google.appengine.api import users
from google.appengine.ext import ndb
import webapp2

class UserModel(ndb.Model):
    currentUser = ndb.StringProperty(required = True)  # OR not required, or repeated, depends on your app.
    some_text = ndb.TextProperty()
    some_more_text = ndb.TextProperty()
    
class MainHandler(webapp2.RequestHandler):
    def get(self):
        # Try and read who's the current user.
        user = users.get_current_user()
        if user:
            # If there was a user logged in, do stuff.
            self.response.write(user)
            user = UserModel(currentUser = user.user_id(), some_text= "hey")
            user.put()
        else:
            # Send the user to a login page, then come back to this request, this
            # time a user will be present.
            self.redirect(users.create_login_url(self.request.uri))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
