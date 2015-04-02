#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'jcarrasco'
__copyright__ = "Copyright 2015, Teran\TBWA"

from django.template import loader, Context, Template
from django.conf import settings
import mandrill

API_KEY = 'YYqygLRQ5K65kGX7Do32NQ'



def send_mail(data):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        msg = MIMEMultipart('alternative')

        msg['Subject'] = u"STEPHANY Y JOSÉ"
        msg['From'] = settings.EMAIL_SENDER
        msg['To'] = settings.EMAIL_SENDER

        template = loader.get_template('mailing.html')

        html = template.render(Context(data))

        part2 = MIMEText(html.encode('utf-8'), 'html', 'utf-8')

        msg.attach(part2)

        s = smtplib.SMTP('smtp.mandrillapp.com', 587)

        s.login(settings.MAIL_SENDER_USER, settings.MAIL_SENDER_PASSWORD)
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()
