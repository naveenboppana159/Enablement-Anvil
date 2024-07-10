from ._anvil_designer import editadminTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class editadmin(editadminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.users.search(user_type='admin')

    # Any code you write here will run before the form opens.
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Admin.ManageUsers.ManageAdmin')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert('Your Details Has Been Saved')
    

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.item.delete()
    self.remove_from_parent()

  
  
    
    