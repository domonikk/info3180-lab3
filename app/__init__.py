from flask import Flask 
from flask_mail import Mail 

app = Flask(__name__) 

app.config['SECRET_KEY'] = 'cheesecake' 
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io' 
app.config['MAIL_PORT'] = '2525' 
app.config['MAIL_USERNAME'] = '918a19d90c585f' 
app.config['MAIL_PASSWORD'] = '40f5063dbc9947' 

mail= Mail(app) 
from app import views  