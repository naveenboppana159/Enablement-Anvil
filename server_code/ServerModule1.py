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


# @anvil.server.callable
# def get_admin_users():
#     return app_tables.admin.search(usertype='admin')
#------------------------------------------------------------------
#Encryption code for password and re-enter password
@anvil.server.callable
def submit(full_name, email_user, user_phonenumber, user_password, reenter_password):
    encrypted_password = anvil.secrets.encrypt_with_key('secret_key', user_password)
    encrypted_reenter_password = anvil.secrets.encrypt_with_key('secret_key', reenter_password)
  
    app_tables.users.add_row(
        full_name=full_name,
        email_user=email_user,
        user_phonenumber=user_phonenumber,
        user_password=encrypted_password,
        reenter_password=encrypted_reenter_password,
        user_type='employee'
    )

#Decrypted code
# @anvil.server.callable
# def load_secret_data():
#   row = app_tables.users.get()
#   if row:
#     return anvil.secrets.decrypt_with_key('secret_key', row['user_password'])