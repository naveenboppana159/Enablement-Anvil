import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import hashlib
import binascii
import os

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
@anvil.server.callable
def submit(full_name ,email_user,user_phonenumber,user_password,reenter_password):
  app_tables.users.add_row(full_name=full_name, email_user = email_user, user_phonenumber=  user_phonenumber,user_password = user_password,reenter_password = reenter_password,user_type='employee')

def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

@anvil.server.callable
def submit_user(full_name, email_user, user_phonenumber, user_password):
    hashed_password = hash_password(user_password)
    app_tables.users.add_row(
        full_name=full_name,
        email_user=email_user,
        user_phonenumber=user_phonenumber,
        user_password=hashed_password
    )

@anvil.server.callable
def get_users():
    return [{'full_name': row['full_name'], 'email_user': row['email_user'], 'user_phonenumber': row['user_phonenumber'], 'user_password': '•' * 8} for row in app_tables.users.search()]