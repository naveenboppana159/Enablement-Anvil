from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Login(LoginTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Any code you write here will run before the form opens.

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        email_user = self.email_textbox.text.strip()
        user_password = self.password_textbox.text.strip()      
        user = anvil.server.call('get_user', email_user, user_password)
        
        if user:
            user_type = user['user_type']
            if user_type=='Admin':
              open_form('Admin')
            else:
              open_form('Employee')
        else:
          alert('no user found')
          


        
        
    

   
