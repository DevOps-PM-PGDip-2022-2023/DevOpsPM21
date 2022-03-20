#Demonstrating use of feature flags with Launch Darkly
import ldclient
from ldclient.config import Config

from flask import Flask, jsonify

user = {"key": "1234", "email": "paul.greaney@lyit.ie", "groups": ["admins"]}

app = Flask(__name__)

@app.route("/")
def get_feature():
    ldclient.set_config(Config("sdk-510a1093-1a72-4b9a-be3b-4b5a93bf4521"))
    show_feature = ldclient.get().variation("return_userdata", user, "No Data")
    if show_feature == True:
        return jsonify(user)
    else:
        return "Flask app is working"
    
if __name__=='__main__':
    app.run(debug=True)
