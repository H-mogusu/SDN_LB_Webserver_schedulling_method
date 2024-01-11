from flask import Flask, redirect, request
import os
import requests
import sys
import random

app = Flask(__name__)

web_servers_str = os.environ.get("WEB_SERVERS", "http://20.234.100.117:8080,http://20.234.101.181:8080")
web_servers = web_servers_str.split(',')
weights = [2, 4]  # Adjust weights as needed
threshold_random = 20
threshold_round_robin = 70
counter = 0  # Counter for round-robin
weighted_counter = {server: 0 for server in web_servers}

def is_server_healthy(server):
    try:
        response = requests.get(server)
        return response.status_code == 200
    except requests.RequestException:
        return False

def get_next_server(request_count):
    global counter
    total_requests = request_count + counter

    if total_requests < threshold_random:
        method = "Random"
        selected_server = random.choice(web_servers)
    elif total_requests < threshold_round_robin:
        method = "Round-robin"
        selected_server = web_servers[counter % len(web_servers)]
    else:
        method = "Weighted Round-robin"
        selected_server = weighted_round_robin(request_count)

    counter += request_count
    return selected_server, method

def weighted_round_robin(request_count):
    global weighted_counter
    total_weight = sum(weights)

    for i, server in enumerate(web_servers):
        weighted_counter[server] += int((request_count * weights[i]) / total_weight)

    # Choose the server with the least weighted requests
    selected_server = min(weighted_counter, key=weighted_counter.get)

    return selected_server

# Check the health of all web servers
if all(is_server_healthy(server) for server in web_servers):
    print("ALL WEBSERVERS ARE UP AND HEALTHY.")
elif any(is_server_healthy(server) for server in web_servers):
    print("At least one web server is up.")
    user_input = os.environ.get("CONTINUE", "").lower()
    if user_input != 'y':
        print("Exiting as per user request.")
        sys.exit(0)
else:
    print("ALL WEBSERVERS ARE DOWN. Exiting.")
    sys.exit(1)

@app.route('/')
def load_balancer():
    global counter
    request_count = int(request.args.get('count', 1))  # Assuming each request adds 1 to the count
    selected_server, method = get_next_server(request_count)
    if selected_server:
        print(f"Total Requests: {counter + request_count}")
        print(f"Selected server: {selected_server}")
        print(f"Load Balancing Method: {method}")
        return redirect(selected_server)
    else:
        print("No healthy servers available. Exiting.")
        sys.exit(1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
