from flask import Flask
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(Flask(__name__))
password = input('Input password : ')
password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
print(f'Hashed password is : {password_hash}')