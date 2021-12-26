import json
import dateutil.parser as dp
from queue import PriorityQueue
from flask import Flask,jsonify,request


app = Flask(__name__)
# creating a priority queque(min heap) to store all the transactions
queue = PriorityQueue()
# dictionary to store the balance 
balancedict=dict()
# totalpoints: the totalpoints a user has in their account
totalpoints=0

# REST endpoint to add transactions for a specific payer and date  
@app.route('/addpoints', methods=['POST'])
def addpoints():

    input_data = request.get_json()
    payer = str(input_data["payer"])
    points = int(input_data["points"])
    timestamp = str(input_data["timestamp"])
    # converting the time stamp from ISO 8601 to Unix timestamp
    parsed_time=dp.parse(timestamp)
    time_in_seconds=parsed_time.timestamp() 
    #  Adding the timstamp, payer and points to the Queue
    queue.put((time_in_seconds,payer,points))
    
    if(payer not in balancedict):
        balancedict[payer]=points
    else:
        balancedict[payer]=balancedict[payer]+points
        
    global totalpoints
    totalpoints+=points

    return jsonify(input_data)

# REST endpoint to spend points from oldest to latest based on timestamp 
# Assumption : the spend points are always >0
@app.route('/spendpoints', methods=['POST'])
def spendpoints():
    data = request.get_json()
    # spendpoints: the points user wants to spend
    spendpoints = int(data["points"])
    spenddict={}
    global totalpoints
    # If a User tries to spend more points then they have.
    if spendpoints>totalpoints:
        return { totalpoints: "Points are available to Spend only!" } 
    
    while spendpoints>0 and spendpoints<=totalpoints and not queue.empty():
        # gets the oldest transaction based on timestamp
        transaction = queue.get()
        payer=transaction[1]
        queuepoints=transaction[2]
        pointsspent=min(queuepoints,spendpoints)
        if payer not in spenddict and balancedict[payer] >= queuepoints:
            spenddict[payer]=-abs(pointsspent)
            balancedict[payer]-= pointsspent
        elif payer in spenddict and balancedict[payer] >= queuepoints:
            spenddict[payer]-=pointsspent
            balancedict[payer]-=pointsspent
        if queuepoints>spendpoints:
            queue.put((transaction[0],payer,queuepoints-spendpoints))
        spendpoints-=pointsspent
        totalpoints-=pointsspent

    # return the number of points deducted from each payer
    return json.dumps(spenddict)

# REST endpoint to display the balance after adding/spending the points
@app.route('/balance', methods=['GET'])
def balance():
    # returns all payer point balances
    return json.dumps(balancedict)

# Default View
@app.route('/', methods=['GET'])
def index():
    return "Welcome to Fetch Rewards Coding Exercise!"

if __name__ =="__main__":
    app.run(debug=True)
