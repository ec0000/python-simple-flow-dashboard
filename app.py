from flask import Flask, jsonify, render_template, request
from datetime import datetime
import json

app = Flask(__name__)

flow_states = ['Order-Book', 'Check-Order', 'Check-Inventory', 'Process-Payment', 'Deliver-Book']
flow_state = ''  # default to the first state

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/time')
def get_current_time():
    return jsonify(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@app.route('/flowstate')
def get_flow_state():
    return jsonify(state=flow_state)

@app.route('/setflowstate/<flowstate>', methods=['POST'])
def set_flow_state(flowstate):
    global flow_state
    payload = request.get_json()  # get the JSON payload
    print(json.dumps(payload, indent=4))  # pretty-print the payload to the server console

    if flowstate in flow_states:
        flow_state = flowstate
        return jsonify(success=True, state=flow_state)
    else:
        return jsonify(success=False, error="Invalid flow state"), 400  # return a 400 Bad Request status code

if __name__ == '__main__':
    app.run(debug=True)
