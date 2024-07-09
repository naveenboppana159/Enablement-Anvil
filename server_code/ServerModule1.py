import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def get_user(email_user, user_password):
    user = app_tables.users.get(email_user=email_user,user_password=user_password)
    if user is not None:
      
      return user
    else:
      return
