from flask import Flask 
from flask_mail import Mail 

app = Flask(__name__) 

app.config['SECRET_KEY'] = 'enter some pass key' 
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io' 
app.config['MAIL_PORT'] = '2525' 
app.config['MAIL_USERNAME'] = 'enter username' 
app.config['MAIL_PASSWORD'] = 'enter password' 

mail= Mail(app) 
from app import views  