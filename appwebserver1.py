from flask import Flask, request
import os
import socket,requests
import psutil
import time
import threading
count = 0
app = Flask(__name__)


def send_cpu():
    while True:
        time.sleep(10)
        cpu_usage = str(psutil.cpu_percent(10))
        # send cpu load to loadbalancer via a post method
        requests.post("http://20.234.99.195:8080/", data={'foo': cpu_usage, 'load':'two'})
       # print(resp.text)
       # print(resp.status_code)

@app.route("/",methods=['GET','POST'])

def hello():
    global count
    html = "<h3>Hello {name}!</h3> <b>Hostname:</b> {hostname}<br/>"
    # run the function that calculates and sends cpu load to loadbalancer as a thread
    t1 = threading.Thread(target=send_cpu)
    t1.start()
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())


if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=4000,debug=True)
    # avoid any delays that sleep(10) may cause by run flask app itself as a thread
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=4000, debug=True, use_reloader=False)).start()

