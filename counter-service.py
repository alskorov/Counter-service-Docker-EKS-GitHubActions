from flask import Flask, request

app = Flask(__name__)
counter = 0
get_requests = 0

@app.route('/', methods=["POST", "GET"])
def index():
    global counter, get_requests
    if request.method == "POST":
        counter += 1
        return f"Hmm, Plus 1 please. Total POSTs: {counter}"
    else:
        get_requests += 1
        return f"Our counter is: {counter}. Total GETs: {get_requests}"

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
