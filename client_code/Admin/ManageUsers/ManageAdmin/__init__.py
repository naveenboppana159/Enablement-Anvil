from ._anvil_designer import ManageAdminTemplate
from anvil import *
import anvil.server


class ManageAdmin(ManageAdminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  

  

  def add_admin_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Admin.ManageUsers.ManageAdmin.addadmin')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Admin.ManageUsers')

  def edit_admin_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Admin.ManageUsers.ManageAdmin.editadmin')
    
    

    
