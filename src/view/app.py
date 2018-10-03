import sys

from src.lib.utils import *
import os
from flask import Flask
app = Flask(__name__)
app.config['banana'] = "3"


@app.route("/alarm-status")
def alarm_status():
    # TODO print report from alarm including
    # number of events detected in the past 24 hours
    # free space left on NAS
    return "all is ok"


@app.route("/alarm-on")
def alarm_on():
    # TODO
    # turn on the alarm notification system on the
    # ALARM_CAMERAS_NAME list
    return ""

@app.route("/alarm-off")
def alarm_off():
    # TODO turns the alarm off
    # deactivates the notification system
    return ""



def alarm_test_notification():
    # TODO
    # sends a test notification to USERS
    return ""


@app.route("/")
def isOk():
    return "200"


def init_api():
    # check that directories exist
    if os.path.isdir(Config.REOLINK_PATH) is False\
            or os.path.isdir(Config.QNAP_SM_PATH) is False:
        print("Bad directory path!")
        sys.exit()
    # check comms systems
    # TODO check communication systems

if __name__ == '__main__':
    init_api()
    app.run(host='0.0.0.0', port=8090)
