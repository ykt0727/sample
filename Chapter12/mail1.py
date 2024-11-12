import smtplib
from email.mime.text import MIMEText

SERVER = 'smtp-mail.outlook.com'
FROM = 'ymg2365039@stu.o-hara.ac.jp'
TO = 'ymg2365039@stu.o-hara.ac.jp'
PASS = '2003ykt07270'

mail = MIMEText('The disk is full.')
mail['Subject'] = 'System Report'
mail['From'] = FROM
mail['To'] = TO

with smtplib.SMTP('SERVER', 587) as smtp:
    smtp.ehlo()
    try:
        smtp.starttls()
        smtp.ehlo()
    except smtplib.SMTPNotSupportedError:
        pass
    smtp.login(FROM, PASS)
    smtp.sendmail(FROM, TO, mail.as_string())