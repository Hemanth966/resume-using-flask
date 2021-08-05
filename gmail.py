from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = 'yourid@gmail.com'
app.config['MAIL_PASSWORD'] = '******'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/")
def index():
    msg = Message('Hi', sender='yourid@gmail.com',
                  recipients=['friend@gmail.com'])
    msg.body = "I'm sending this mail to you by using Flask mail."


mail.send(msg)
return 'Sent'
if __name__ == '__main__': app.run(debug=True)


