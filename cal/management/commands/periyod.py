import datetime
import smtplib
import ssl
from cal.models import Event
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Command(BaseCommand):
    def handle(self, *args, **options):
        today = datetime.date.today()
        next_sprint = today + datetime.timedelta(days=14)
        events = Event.objects.filter(is_weekend = False, start_time__gte = today, start_time__lt = next_sprint)
        
        events = Event.objects.all()

        sender_email = "dopigosprint@gmail.com"
        receiver_email = "canerkurtcephe@outlook.com"
        password = "dopigoizmir35"

        message = MIMEMultipart("alternative")
        message["Subject"] = "Sprint"
        message["From"] = sender_email
        message["To"] = receiver_email

        text = """\
        Önümüzdeki Sprint içerisinde yer alan eventlerin listesi aşağıdaki gibidir.
        """

        html = render_to_string("cal/mail_template.html", context={'events': events})

        part = MIMEText(html, "html")

        message.body = text
        message.attach(part)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())