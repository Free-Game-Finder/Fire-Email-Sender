import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from scripts import steam, db
import os

def main():
    game_store = [steam]


    PASSWORD = os.environ.get("APP_PASS")
    fromaddr = os.environ.get("APP_EMAIL")

    toaddr = [fromaddr]
    cc = []
    bcc = []

    subject = 'FGN - Free Game Notifier'

    db.db_connect()
    print("db connection successful")

    for store in game_store:

        all_emails = store.get_emails()

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = fromaddr
        msg['To'] = ', '.join(toaddr)
        # msg['Cc'] = ', '.join(cc)
        # msg['Bcc'] = ', '.join(bcc)

        # Create the body of the message (an HTML version).
        with open(store.html_path(), 'r') as file:
            html = store.add_to_html(file.read())
            if not html:
                pass
            else:

                # Record the MIME types of both parts - text/plain and text/html.
                body_plain = MIMEText("Check Out Today's Free Games!F", 'plain')
                body_html = MIMEText(html, 'html')

                # Attach parts into message container.
                msg.attach(body_plain)
                msg.attach(body_html)

                # Send the message via local SMTP server.
                s = smtplib.SMTP('smtp.gmail.com', 587)
                # s.set_debuglevel(1)
                s.ehlo()
                s.starttls()
                s.login(fromaddr, PASSWORD)

                for id in range(0, len(all_emails), 400):
                    def sendmail(bcc):
                        s.sendmail(fromaddr, toaddr + cc + bcc, str(msg))
                    sendmail(list(all_emails)[id: id + 400])

                s.quit()
        file.close()
       
main()
