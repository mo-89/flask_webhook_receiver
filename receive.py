from flask import Flask, request, jsonify

app = Flask(__name__)

SECRET_API_KEY = 'test_key'

@app.route("/")
def hello_world():
    return "<p>Hello, world</p>"

@app.route('/receive', methods=['POST'])
def webhook_receiver():
    received_key = request.headers.get('x-api-key')
    if received_key != SECRET_API_KEY:
        return jsonify({'message': 'Invalid API Key'}), 401
    
    data = request.json
    print("Received Webhook with data:", data)
    return jsonify({'message': 'webhook received'}), 200

if __name__ == '__main__':
    # app.run(port=5050)
    app.run(host='0.0.0.0', port=5050)

# export FLASK_APP=receive
# flask run --port 5050