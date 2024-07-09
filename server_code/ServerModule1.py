import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users



@anvil.server.callable
def get_user(email_user, user_password):
    user = app_tables.users.get(email_user=email_user,user_password=user_password)
    if user is not None:
      
      return user
    else:
      return



@anvil.server.callable
def clear_user_session():
    user = anvil.users.get_user()
    if user:
        # Clear any session data for the user
        # Example: app_tables.sessions.delete(user)
        # If you have a sessions table to manage user sessions, clear the relevant data
        pass

    anvil.users.logout()
