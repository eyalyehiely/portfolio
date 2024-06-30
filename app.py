from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
# app.secret_key = 'fghdfghdfefbgrgbrgbdfgbndfgndfnrhwrglwehg;qeorghpoeuhrg9q3h39t3y355723yt3giuerhiefvbiaefbgh'

# Configuration for mail server
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'eyalwork0@gmail.com'
app.config['MAIL_PASSWORD'] = 'ealm iwla hxih sgfm'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('/index.html')



@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        msg = Message(subject=f" קיבלת הודעה חדשה מ:  {name}",
                      sender=('portfolio', 'eyalwork0@gmail.com'),
                      recipients=["eyalwork0@gmail.com"])
        msg.body = f"Message from: {email}\n\n{message}"

        mail.send(msg)
        return "Email sent successfully! thank you"
    except Exception as e:
        app.logger.error(f"Error sending email: {e}")
        return "Error, please try again"


if __name__ == '__main__':
    app.run(debug=False)
