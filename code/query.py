from flask import Flask
from flask_cors import CORS
import sched
import time
from TV1.TV1_dash import DataframeConversion, run_periodically
from TV2.TV2_dash import returnColumn
app = Flask(__name__)
cors = CORS(app)


scheduler = sched.scheduler(time.time, time.sleep)
SCADAinterval = 300

@app.route('/TV1/DUID')
def returnDUID():
    return DataframeConversion('DUID')

@app.route('/TV1/SCADA')
def returnSCADA():
    return run_periodically(scheduler, SCADAinterval)

@app.route('/TV1/CAPACITY')
def returnCAP():
    return DataframeConversion('Generator Capacity (MW)')

@app.route('/FOOTPRINTS/ASSIGNEES')
def returnAssignees():
    return returnColumn('Assignees')

@app.route('/FOOTPRINTS/SUBMITTED')
def returnSubmission():
    return returnColumn('Date Submitted')

@app.route('/FOOTPRINTS/STATUS')
def returnStatus():
    return returnColumn('Status')

@app.route('/FOOTPRINTS/TICKET')
def returnTicketNo():
    return returnColumn('Global Ticket No.')

@app.route('/FOOTPRINTS/ACCOUNT')
def returnAccount():
    return returnColumn('Account')

@app.route('/FOOTPRINTS/PRODUCT')
def returnProduct():
    return returnColumn('Product')

if __name__ == '__main__':
    app.run(port=8080)