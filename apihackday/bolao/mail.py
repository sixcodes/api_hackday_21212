#encoding: utf-8
import sendgrid
from django.template.loader import render_to_string
from os import environ


def sendmail(subject, to, template, category='alert', **kwargs):
    # make a secure connection to SendGrid
    s = sendgrid.Sendgrid(environ.get("SENDGRID_USER"), environ.get("SENDGRID_PWD"), secure=True)

    body = render_to_string(template, dictionary=kwargs)
    print type(unicode(body))

    # make a message object
    message = sendgrid.Message("bolao@bolao.daltonmatos.com", subject, "", unicode(body).encode("utf-8"))

    # add a recipient
    message.add_to(to)

    message.add_category(category)
    # use the Web API to send your message
    s.web.send(message)