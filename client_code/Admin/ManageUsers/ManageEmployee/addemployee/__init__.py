from ._anvil_designer import addemployeeTemplate
from anvil import *
import anvil.server


class addemployee(addemployeeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    open_form('Admin.ManageUsers.ManageEmployee')

  def button_1_click(self, **event_args):
    full_name=self.text_box_name.text
    email_user=self.text_box_email.text
    user_phonenumber=self.text_box_phonenumber.text
    user_password = self.text_box_password.text
    reenter_password = self.text_box_reenterpassword.text
    
    
# Input validation
    if not (full_name and email_user and user_phonenumber and user_password and reenter_password):
      Notification("Please fill all the fields").show()
      return

    # elif phone.isdigit():
    #   Notification("Phone number must be numeric").show()
    #   return

    elif user_password != reenter_password:
      Notification("Passwords do not match").show()
      return
      
    elif len(str(user_phonenumber)) != 10:  # Check for phone number length
      Notification("Phone number must be exactly 10 digits").show()
      return

    try:
      user_phonenumber = int(user_phonenumber)  # Convert phone to int after validation
    except ValueError:
      Notification("Invalid phone number format").show()
      return

    # Server call from servermodule1_addemployee
    try:
      anvil.server.call('submit', full_name=full_name, email_user = email_user, user_phonenumber= user_phonenumber,user_password = user_password,reenter_password = reenter_password)
      Notification("Your employee details have been saved!!!").show()
    # Clear form fields
      self.text_box_name.text = ""
      self.text_box_email.text = ""
      self.text_box_phonenumber.text = ""
      self.text_box_password.text = ""
      self.text_box_reenterpassword.text = ""
      
    except Exception as e:
      Notification(f"An error occurred: {str(e)}").show()


