from flask import Flask, request
from flask_cors import CORS
import sched
import time
from TV1.TV1_dash import DataframeConversion, run_periodically
from TV2.TV2_dash import returnColumn
from TV3.TV3_dash import returnFootprintsData
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
    return returnColumn('Ticket Number')

@app.route('/FOOTPRINTS/ACCOUNT')
def returnAccount():
    return returnColumn('Account')

@app.route('/FOOTPRINTS/PRODUCT')
def returnProduct():
    return returnColumn('Title')

@app.route('/KPI/TOP_TICKET_SITES')
def returnTopTicketSites():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    return f'Returning ticket per site from {start_date} to {end_date}'

@app.route('/KPI/TICKET_PER_SITE')
def returnTicketPerSite():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    return f'Returning ticket per site from {start_date} to {end_date}'
    

@app.route('/KPI/TICKET_PER_PRODUCT')
def returnTicketPerProduct():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    return f'Returning ticket per site from {start_date} to {end_date}'

if __name__ == '__main__':
    app.run(port=8080)