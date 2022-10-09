import smtplib
import json
import os
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

project_path = os.path.dirname(os.path.dirname(os.path.abspath(os.curdir)))
with open(os.path.join(project_path, "secret.json")) as info_file:
    info = json.load(info_file)
server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.starttls()
server.login(user=info['mail_client_id'], password=info['mail_client_pwd'])

msg = MIMEMultipart()
msg['From'] = 'Kelly'
msg['To'] = f'{info["mail_client_receiver"]}'
msg['Subject'] = "mail_client.py test"


with open('message.txt', 'r') as msg_file:
    message = msg_file.read()

msg.attach(MIMEText(message, 'plain'))
filename = 'la.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()

server.sendmail(from_addr=info['mail_client_id'], to_addrs=info["mail_client_receiver"], msg=text)