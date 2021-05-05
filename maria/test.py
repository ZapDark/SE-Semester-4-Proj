import smtplib, ssl

enterorsend = input("Would you like to send emails or enter emails into database? Type 'enter' or 'send': ")


if enterorsend == 'send': 
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "seproj5@gmail.com"  # Enter your address
    receiver_email = "mariatrimborn1@gmail.com"  # Enter receiver address
    password = "Clover125!"
    message = """\
    Subject: yeah

    I can send email with python now. http://localhost"""

    context = ssl.create_default_context()

    print("sending emails to:", receiver_email)
    
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

if enterorsend =='enter':
    import addemail
    
else:
    print("Goodbye")
    exit()


