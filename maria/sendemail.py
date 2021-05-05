import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import smtplib, ssl
from firebase import firebase
import smtplib, ssl
# Fetch the service account key JSON file contents
cred = credentials.Certificate('email-48310-firebase-adminsdk-1w2m5-a78b953bdb.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://email-48310-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('email-48310-default-rtdb/emailstosend/')


snapshot = ref.order_by_child('address').get()
emailaddress = []

for key, val in snapshot.items():
    unparsed = ('{1}'.format(key, val))
    x = (unparsed.replace('}', '').replace('{', '').replace('address','').replace(':', '').replace("'", "").replace('"', "").replace(' ',''))
    emailaddress.append(x)


print(emailaddress)

print("Would you like to send emails or enter emails into database?")
enterorsend = input("Type 'enter', 'send', or any other key to exit: ")


if enterorsend == 'send':
    for y in emailaddress:
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "seproj5@gmail.com"  # Enter your address
        receiver_email = y  # Enter receiver address
        password = "Clover125!"
        message = """\
        Subject: yeah

        I can send email with python now. http://localhost"""

        context = ssl.create_default_context()

        print("sending emails to:", receiver_email)
        
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

if enterorsend == 'enter':
    import addemail    

else:
    print("Goodbye")
    exit()


