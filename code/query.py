from flask import Flask, request
from flask_cors import CORS
import sched
import time
from TV1.TV1_dash import DataframeConversion, run_periodically
from TV2.TV2_dash import returnColumn, footprints_run_periodically
from TV3.TV3_dash import topSites, ticketPerSite, ticketByPriority, ticketByProduct
app = Flask(__name__)
cors = CORS(app)


scheduler = sched.scheduler(time.time, time.sleep)
SCADAinterval = 300
footprintInterval = 86400

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
    return footprints_run_periodically(scheduler, footprintInterval, 'Assignees')

@app.route('/FOOTPRINTS/SUBMITTED')
def returnSubmission():
    return footprints_run_periodically(scheduler, footprintInterval, 'Date Submitted')

@app.route('/FOOTPRINTS/STATUS')
def returnStatus():
    return footprints_run_periodically(scheduler, footprintInterval, 'Status')

@app.route('/FOOTPRINTS/TICKET')
def returnTicketNo():
    return footprints_run_periodically(scheduler, footprintInterval, 'Ticket Number')

@app.route('/FOOTPRINTS/ACCOUNT')
def returnAccount():
    return footprints_run_periodically(scheduler, footprintInterval, 'Account')

@app.route('/FOOTPRINTS/PRODUCT')
def returnProduct():
    return footprints_run_periodically(scheduler, footprintInterval, 'Title')

@app.route('/KPI/TOP_TICKET_SITES')
def returnTopTicketSites():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    return topSites(start_date, end_date)

@app.route('/KPI/TICKET_BY_PRIORITY')
def returnTicketByPriority():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    return ticketByPriority(start_date, end_date)
    

@app.route('/KPI/TICKET_PER_PRODUCT')
def returnTicketPerProduct():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    return ticketByProduct(start_date, end_date)

@app.route('/KPI/TICKET_PER_SITE')
def returnTicketPerSite():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    return ticketPerSite(start_date, end_date)


if __name__ == '__main__':
    app.run(port=8080)