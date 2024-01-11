from flask import Flask, request                                                         
import sys
import os
import socket
import requests

count = 0
load1 = 0
load2 = 0
BACKENDS = ["20.234.100.117:8080", "20.234.101.181:8080"]
app = Flask(_name_)

def choose_server():
    global load1, load2

    # Explicitly choose server1 if load1 < load2, else choose server2
    if load1 < load2:
        return BACKENDS[0]
    elif load2 < load1:
        return BACKENDS[1]
    else:
        # If loads are equal, use round-robin approach
        return BACKENDS[count % len(BACKENDS)]

def get_response(server):
    response = requests.get("http://{}".format(server))
    return response.content, response.status_code

@app.route("/", methods=["GET", "POST"])
def hello():
    global load1, load2
    global count

    if request.method == "GET":
        # Low load condition for both servers
        # Round-robin approach used
        if load1 < 50 and load2 < 50:
            print("load1:", load1, flush=True)
            print("load2:", load2, flush=True)
            response = get_response(BACKENDS[count])
            count = (count + 1) % len(BACKENDS)
            return response[0], response[1]

        # High load condition for at least one server
        server = choose_server()
        print("Selected server:", server, flush=True)
        response = get_response(server)
        return response[0], response[1]

    if request.method == "POST":
        if request.form['load'] == 'one':
            load1 = float(request.form['foo'])
            print("updated load1", load1, flush=True)
        elif request.form['load'] == 'two':
            load2 = float(request.form['foo'])
            print("updated load2:", load2, flush=True)
        return 'Received'

if _name_ == "_main_":
    app.run(host='0.0.0.0', port=4000)
