import email.contentmanager
from email.message import EmailMessage, Message
import string
from os.path import basename

from Clases.Email.EmailsAction import EmailAction
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email(EmailAction):
    __subject: string
    __issuer: string = "no-reply@sgied.com.mx"

    def __init__(self, subject: string):
        self.__subject = subject

    @property
    def get_email_subject(self) -> string:
        return self.__subject

    def send_email(self, arg_mail: {}):
        import smtplib
        to = self.__subject
        user = self.__issuer  # your secureserver mail_id(godaddy)
        pwd = 'Paramore11!*25'
        msg = EmailMessage()
        msg['To'] = to
        msg['From'] = user
        msg['Subject'] = "Testing"
        payloads: [] = [Message().attach("Thank you")]
        msg.set_payload(payloads)
        smtp_server = smtplib.SMTP("smtpout.asia.secureserver.net", 80)
        smtp_server.ehlo()
        smtp_server.login(user, pwd)
        smtp_server.sendmail(user, to, msg)
        smtp_server.close()
        print(arg_mail)
