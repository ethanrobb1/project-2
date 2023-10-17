"""
Ethan Robb's Flask API.
"""

from flask import Flask, send_from_directory, abort
import config

app = Flask(__name__)

#config logic/ file pulled from project 1
cred = config.configuration()

@app.route("/")
def hello():
    return "UOCIS docker demo!\n"

@app.route("/<string:filename>")
def serve(filename):
    if "~" in filename or ".." in filename:
        abort(403) #forbidden
    try:
        return send_from_directory("pages/", filename), 200
    except:
        abort(404) #file not found

#error handlers
@app.errorhandler(403)
def forbidden(e):
    return send_from_directory('pages/', '403.html'), 403

@app.errorhandler(404)
def notFound(e):
    return send_from_directory('pages/', '404.html'), 404
     
if __name__ == "__main__":
    app.run(debug=cred.DEBUG, host='0.0.0.0', port=cred.PORT)
    
