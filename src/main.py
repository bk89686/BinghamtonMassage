from flask.globals import request #@UnresolvedImport
from flask.app import Flask #@UnresolvedImport
from flask.helpers import make_response #@UnresolvedImport
from flask import render_template  #@UnresolvedImport
from PythonFiles.IntakeForm import IntakeForm
import logging
from PythonFiles import Utilities
import traceback


app = Flask(__name__)
util = Utilities.Cookies()
cookieVal = ""

@app.route('/', methods=['GET'])
def loadForm():
    return render_template('intakeForm.html')


@app.route('/save', methods=['POST'])
def saveForm():
    main = IntakeForm()
    main.saveIntakeForm(request)
    return render_template('submitted.html')

@app.route('/clientList', methods=['GET', 'POST'])
def showClientList():
    main = IntakeForm()
    valid, token = main.isValidToken(request, util)
    if valid:
        appts = main.showIntakeForm(request)
    else:
        appts = None
    request.form = None
    response = make_response(render_template("client_list.html", appts=appts))
    response = Utilities.Cookies().setCookie(response, token)
    return response

@app.route('/delete', methods=['POST'])
def delete():
    try:
        bmawId = request.form.get("bmaw_id")
        logging.error("deleting: " + str(bmawId))
        IntakeForm().deleteRecord(bmawId)
    except:
        logging.error("delete failed")
        logging.error(traceback.format_exc())
    return showClientList()

@app.route('/clientData', methods=['GET','POST'])
def showClientForm():
    main = IntakeForm()
    client = None
    valid, _ = main.isValidToken(request, util)
    if valid:
        client = main.showOneClient(request.args.get("tid"))
    if client != None:
        rendered = render_template('client_data.html', client=client)
    else:
        rendered = render_template("client_list.html", appts=None)
    return rendered

@app.route('/hidden', methods=['GET'])
def showHidden():
    return render_template('hidden.html')

@app.route('/signout', methods=['GET'])
def signout():
    util = Utilities.Cookies()
    response = make_response(render_template("signout.html"))
    util.setCookie(response, "")
    return response


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)