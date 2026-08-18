'''
Created on May 20, 2025

@author: blue2factor
'''

from datetime import date
import logging
import traceback
from mailjet_rest import Client#@UnresolvedImport
from PythonFiles.Properties import Properties#@UnresolvedImport


class Cookies():
    cookieName = "gstatBMaW"
    def setCookie(self, response, cookieVal):
        try:
            if cookieVal == None:
                cookieVal = ""
            logging.error("setting cookie to '" + str(cookieVal) + "'")
            response.set_cookie(self.cookieName, cookieVal, samesite='Lax', max_age=60*60*24, secure=True)
        except:
            logging.error(traceback.format_exc())
        return response;
    
    def getCookie(self, request):
        return request.cookies.get(self.cookieName)
    
class Email():
    
    def alertKellyOfFormCompletion(self, userName):
        html = ("<strong>" + userName + "</strong> just filled out the intake form. Go to the " +
            "<a href='https://intake.binghamtonmassageandwellness.com/clientList'>list" +
            "</a> to view it.")
        self.sendEmail("kellyweiss27@hotmail.com", "A new intake form was completed", html)
        emilyEnd = date(2026, 8, 28)
        if date.today() < emilyEnd:
            self.sendEmail("forbalmt@gmail.com", "A new intake form was completed", html)
        # self.sendEmail("forbalmt@gmail.com", "A new intake form was completed", html)
    
    def sendEmail(self, email, subject, html):
        emailBody = self.remove_html_markup(html)
        mailjet = Client(auth=(Properties().mailJetApiKey, Properties().mailJetSecret), version='v3.1')
        data = {
        'Messages': [
            {
                "From": {
                    "Email": Properties().fromEmail,
                    "Name": "Binghamton Massage and Wellness"
                 },
                "To": [
                    {
                        "Email": email,
                    },
                    {
                        "Email": "chris.mclain@gmail.com"
                    }
                ],
                "Subject": subject,
                "TextPart": emailBody,
                "HTMLPart": html,
                "CustomID": "AppGettingStartedTest"
            }
          ]
        }
        result = mailjet.send.create(data=data)
        logging.error("sending email to: " + str(email))
        logging.error("sending email code: " + str(result.status_code))
        logging.error(result.json())
        
    def remove_html_markup(self, s):
        tag =False
        quote =False
        out=""
        for c in s:
            if c =='<' and not quote:
                tag =True
            elif c =='>' and not quote:
                tag =False
            elif (c =='"' or c=="'") and tag:
                quote = not quote
            elif not tag:
                out=out+ c
        return out