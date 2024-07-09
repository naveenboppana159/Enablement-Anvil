from ._anvil_designer import AdminTemplate
import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables


class Admin(AdminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    """This method is called when the button is clicked"""

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('clear_user_session')
    open_form('Login')
    




  