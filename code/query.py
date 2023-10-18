from flask import Flask
from flask_cors import CORS
import sched
import time
from TV1.TV1_dash import DataframeConversion, run_periodically

app = Flask(__name__)
cors = CORS(app)


scheduler = sched.scheduler(time.time, time.sleep)
interval = 300

@app.route('/DUID')
def returnDUID():
    return DataframeConversion('DUID')

@app.route('/SCADA')
def returnSCADA():
    return run_periodically(scheduler, interval)

@app.route('/CAPACITY')
def returnCAP():
    return DataframeConversion('Generator Capacity (MW)')


if __name__ == '__main__':
    app.run(port=8080)