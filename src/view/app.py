from flask import Flask

app = Flask(__name__)


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
    return 200

if __name__ == '__main__':
    #READ CONFIG SOME HOW
    # SETUP ENVIRONMENT VARS

    app.run(host='0.0.0.0', port=8090)
