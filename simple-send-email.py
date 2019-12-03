import smtplib
 
def send_email():
    """
    Send email from gmail account

    Parameters to change:
    YOUR_EMAIL@GMAIL.COM
    SOMEONE_EMAIL@DOMAIN.COM
    YOUR_GMAIL_APP_PASSWORD
    """
    fromaddr = "YOUR_EMAIL@GMAIL.COM"
    toaddr = "SOMEONE_EMAIL@DOMAIN.COM"
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(fromaddr, "YOUR_GMAIL_APP_PASSWORD")
    SUBJECT = "SUBJECT"
    TEXT = "TEXT"
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    server.sendmail(fromaddr, toaddr, message)
    server.quit()
