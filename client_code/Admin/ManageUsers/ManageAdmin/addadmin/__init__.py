from ._anvil_designer import addadminTemplate
from anvil import *
import anvil.server


class addadmin(addadminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Admin.ManageUsers.ManageAdmin')

  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    full_name = self.text_box_name.text
    email_user = self.text_box_email.text
    user_phonenumber = self.text_box_phone_number.text
    user_password = self.text_box_password.text
    reenter_password = self.text_box_reenter_password.text
    
    # Input validation
    if not (full_name and email_user and user_phonenumber and user_password and reenter_password):
      Notification("Please fill all the fields").show()
      return

    # if not phone.isdigit():
    #   Notification("Phone number must be numeric").show()
    #   return
    
    elif len(str(user_phonenumber)) != 10:  # Check for phone number length
      Notification("Phone number must be exactly 10 digits").show()
      return
      
    elif user_password != reenter_password:
      Notification("Passwords do not match").show()
      return

    try:
      user_phonenumber = int(user_phonenumber)  # Convert phone to int after validation
    except ValueError:
      Notification("Invalid phone number format").show()
      return

    # Server call
    try:
      anvil.server.call('submit', full_name=full_name, email_user = email_user, user_phonenumber=  user_phonenumber,user_password = user_password,reenter_password = reenter_password)
      Notification("Your Admin details have been saved!!!").show()
      # Clear form fields
      self.text_box_name.text = ""
      self.text_box_email.text = ""
      self.text_box_phone_number.text = ""
      self.text_box_password.text = ""
      self.text_box_reenter_password.text = ""
      
    except Exception as e:
      Notification(f"An error occurred: {str(e)}").show()
      
  