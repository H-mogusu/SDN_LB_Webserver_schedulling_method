from flask import Flask, redirect, request
import os
import sys

app = Flask(__name__)

web_servers_str = os.environ.get("WEB_SERVERS", "http://20.234.100.117:8080,http://20.234.101.181:8080")
web_servers = web_servers_str.split(',')
url_weights = {'http://20.234.100.117:8080': 7, 'http://20.234.101.181:8080': 8}  # Adjust weights as needed
counter = 0  # Counter for round-robin

def get_next_server(request_count):
    global counter
    requests_remaining = request_count

    while requests_remaining > 0:
        selected_server = weighted_round_robin(requests_remaining)
        requests_to_assign = min(requests_remaining, url_weights[selected_server])
        counter += requests_to_assign
        requests_remaining -= requests_to_assign

        if requests_remaining > 0:
            yield selected_server, requests_to_assign
        else:
            yield selected_server, requests_to_assign + requests_remaining

def weighted_round_robin(requests_remaining):
    global counter
    total_weight = sum(url_weights.values())
    selected_index = counter % total_weight

    for server, weight in url_weights.items():
        if selected_index < weight:
            return server
        selected_index -= weight

@app.route('/')
def load_balancer():
    global counter
    request_count = int(request.args.get('count', 1))  # Assuming each request adds 1 to the count

    for selected_server, assigned_requests in get_next_server(request_count):
        print(f"Total Requests: {counter}")
        print(f"Selected server: {selected_server}")
        print(f"Load Balancing Method: Weighted Round-robin")
        return redirect(selected_server)

    print("No servers available. Exiting.")
    sys.exit(1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)

