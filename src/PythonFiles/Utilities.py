'''
Created on May 20, 2025

@author: blue2factor
'''

import logging
import traceback

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