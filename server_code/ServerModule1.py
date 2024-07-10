

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def store_user_input(user_name, email, password):
#     app_tables.add_row(Email=email, Name=user_name, Password=password)

import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables

# @anvil.server.callable
# def get_admin_users():
#     return app_tables.admin.search(usertype='admin')
