'''
Created on May 16, 2025

@author: blue2factor
'''
import logging
import random
import string
import time
import traceback
from datetime import datetime
from google.cloud import datastore #@UnresolvedImport
from google.oauth2 import id_token #@UnresolvedImport
from google.auth.transport import requests #@UnresolvedImport
from markupsafe import escape #@UnresolvedImport
from PythonFiles.Properties import Properties #@UnresolvedImport
from PythonFiles import Utilities


class IntakeForm():
    cookieVal = ""
    
    def isValidToken(self, request, util):
        success = False
        token = None
        try:
            token = util.getCookie(request)
            if token is None or token == "":
                logging.error("cookie was not found")
                token = request.form["credential"]
            else:
                logging.error("cookie was found")
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), Properties().WEB_CLIENT_ID)
            logging.error(idinfo)
            email = idinfo["email"]
            
            if email in Properties().allowedEmails:
                expire = idinfo["exp"]
                if expire > int(time.time()):
                    success = True
                else:
                    logging.error("token was expired")
                    token = ""
            else:
                logging.error("bad email: " + str(email))
                token = ""
        except:
            logging.error("invalid or no token")
            logging.error(traceback.format_exc())
            token = ""
        return success, token
    
    def showIntakeForm(self, request):
        
        try:
            datastore_client = datastore.Client()
            query = datastore_client.query(kind="appointments")
            query.order = ["-createDate"]
            appts = list(query.fetch())
            previousDate = None
            for appt in appts:
                createDateString = appt['createDate'].strftime("%-m/%-d/%Y")
                if createDateString != previousDate and previousDate != None:
                    appt['newDay'] = True
                else:
                    appt['newDay'] = False
                appt["createDateString"] = createDateString
                previousDate = createDateString
                
        except:
            logging.error("probable error: " + traceback.format_exc() + "\n")
        return appts
    
    def saveIntakeForm(self, request):
        try:
            logging.warn("request: " + str(request.form))
            firstName = request.form["first_name"]
            if (firstName == firstName.lower() or firstName == firstName.upper()):
                firstName = self.capitalizeFirstLetter(firstName)
                
            lastName = request.form["last_name"]
            if (lastName == lastName.lower() or lastName == lastName.upper()):
                lastName = self.capitalizeFirstLetter(lastName)
            dob = request.form["date_of_birth"]
            email = request.form["email"]
            phone = request.form["phone"]
            primaryPhysician = request.form["primary_physician"]
            medicalConditions = request.form["medical_conditions"]
            medications = request.form["medications"]
            try:
                pregnant = request.form["pregnant"]
            except:
                pregnant = "no response"
            pregnancyLength = request.form["pregnancy_length"]
            try:
                previousMassage = request.form["previous_massage"]
            except:
                previousMassage = "no response"
            massageFrequency = request.form["frequency"]
            emergencyName = request.form["emergency_name"]
            emergencyPhone = request.form["emergency_phone"]
            massageType = request.form.getlist("massage_type")
            massageTypeOther = request.form["massage_type_other_explain"]
            painLocations = request.form.getlist("pain_location")
            painLocationsOther = request.form["pain_type_other_explain"]
            try:
                pressureType = request.form["pressure_type"]
            except:
                pressureType = "no response"
            visitReason = request.form["reason"]
            dontMassage = request.form["dont_massage"]
            goals = request.form["goals"]
            source = request.form["source"]
            addOns = request.form.getlist("extras")
            signature = request.form["signature_data"]
            date = request.form["date"]
            datastore_client = datastore.Client()
            kind = "appointments"
            name = self.getRandomId()
            appt_key = datastore_client.key(kind, name)
            appt = datastore.Entity(key=appt_key, exclude_from_indexes=("signatureData",))
            appt["firstName"] = firstName
            appt["lastName"] = lastName
            appt["dob"] = dob
            appt["email"] = email
            appt["phone"] = phone
            appt["emergencyName"] = emergencyName
            appt["emergencyPhone"] = emergencyPhone
            appt["primaryPhysician"] = primaryPhysician
            appt["medicalConditions"] = medicalConditions
            appt["medications"] = medications
            appt["pregnant"] = pregnant
            appt["pregnancyLength"] = pregnancyLength
            appt["previousMassage"] = previousMassage
            appt["massageFrequency"] = massageFrequency
            appt["massageType"] = str(massageType)
            appt["massageTypeOther"] = massageTypeOther
            appt["painLocations"] = str(painLocations)
            appt["painLocationsOther"] = painLocationsOther
            appt["pressureType"] = pressureType
            appt["visitReason"] = visitReason
            appt["dontMassage"] = dontMassage
            appt["goals"] = goals
            appt["addOns"] = str(addOns)
            appt["source"] = str(source)
            appt["signatureDate"] = date
            appt["createDate"] = datetime.now()
            appt["signatureData"] = signature
            datastore_client.put(appt)
            if (lastName != "Delete"):
                Utilities.Email().alertKellyOfFormCompletion(firstName + " " + lastName)
        except:
            logging.error("error: " + traceback.format_exc() + "\n")
    
    def saveSoapNotes(self, request):
        try:
            datastore_client = datastore.Client()
            kind = "soap_notes"
            name = self.getRandomId()
            soap_notes_key = datastore_client.key(kind, name)
            soap_notes = datastore.Entity(key=soap_notes_key)
            soap_notes["subjective"] = request.form["new_subjective"]
            soap_notes["objective"] = request.form["new_objective"]
            soap_notes["assessment"] = request.form["new_assessment"]
            soap_notes["plan"] = request.form["new_plan"]
            soap_notes["soap_dt"] = datetime.now()
            soap_notes["client_id"] = request.form["client_id"]
            datastore_client.put(soap_notes)
        except:
            logging.error("error: " + traceback.format_exc() + "\n")
        
            
    def isSameIntakeFormAsLast(self, request):
        same = False
        try:
            datastore_client = datastore.Client()
            query = datastore_client.query(kind="appointments")
            query.order = ["-createDate"]
            appts = list(query.fetch())
            for appt in appts:
                if request.form["email"] == appt["email"]:
                    if request.form["signature_data"] == appt["signatureData"]:
                        if request.form["first_name"] == appt["firstName"]:
                            if request.form["last_name"] == appt["lastName"]:
                                if request.form["emergency_phone"] == appt["emergencyPhone"]:
                                    same = True
                break
        except:
            logging.error("error: " + traceback.format_exc() + "\n")
        return same
            
    def showOneClient(self, tableId):
        datastore_client = datastore.Client()
        kind = "appointments"
        appt_key = datastore_client.key(kind, tableId)
        clientRecord = datastore_client.get(appt_key)
        clientRecord["bmawId"] = tableId
        clientRecord['massageTypeString'] = self.arrayToStringWithCommas(clientRecord["massageType"])
        painString = self.arrayToStringWithCommas(clientRecord["painLocations"])
        clientRecord['massageFrequency'] = self.replaceDashesWithSpaces(clientRecord['massageFrequency'])
        if clientRecord["painLocationsOther"] != "":
            painString = painString + ", " + clientRecord["painLocationsOther"]
        clientRecord['painLocationsString'] = painString
        clientRecord['addOnsString'] = self.arrayToStringWithCommas(clientRecord["addOns"])
        
        kind = "soap_notes"
        soap_query = datastore_client.query(kind=kind)
        soap_query.add_filter(filter=datastore.query.PropertyFilter("client_id", "=", tableId))
        # soap_query.order = ["-soap_dt"]
        results = list(soap_query.fetch())
        soap_records = []
        for result in results:
            result["formatted_date"] = result["soap_dt"].strftime("%-m/%-d/%Y")
            if result["subjective"] != "":
                result["subjective_exists"] = True
                result["subjective_array"] = result["subjective"].split('\n')
            else:
                result["subjective_exists"] = False
            if result["objective"] != "":
                result["objective_exists"] = True
                result["objective_array"] = result["objective"].split('\n')
            else:
                result["objective_exists"] = False
            if result["assessment"] != "":
                result["assessment_exists"] = True
                result["assessment_array"] = result["assessment"].split('\n')
            else:
                result["assessment_exists"] = False
            if result["plan"] != "":
                result["plan_exists"] = True
                result["plan_array"] = result["plan"].split('\n')
            else:
                result["plan_exists"] = False
            result["subjective"] = escape(result["subjective"]).replace('\n', "\<br\>")
            soap_records.append(result)
            
        clientRecord["soap_notes"] = soap_records
        
        clientRecord["soap_notes_count"] = len(results)
        return clientRecord
    
    def deleteRecord(self, bmawId):
        datastore_client = datastore.Client()
        kind = "appointments"
        appt_key = datastore_client.key(kind, bmawId)
        datastore_client.delete(appt_key)
    
    def replaceDashesWithSpaces(self, stringWithDashes):
        return stringWithDashes.replace("-", " ")
    
    def arrayToStringWithCommas(self, pArray):
        resultStr = ""
        for item in pArray:
            if item != "'" and item != "[" and item != "]":
                if item == "-":
                    resultStr = resultStr + " "
                else:
                    resultStr = resultStr + item
        return resultStr
    
    def getRandomId(self):
        return self.randomString(15)
    
    def randomString(self, length, characters=string.ascii_letters + string.digits):
        return ''.join(random.choice(characters) for _ in range(length))
    
    def capitalizeFirstLetter(self, string):
        return string.capitalize()
        