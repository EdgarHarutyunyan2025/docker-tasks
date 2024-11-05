from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the User Info Page!"

@app.route('/log-user-agent', methods=['POST'])
def log_user_agent():
    user_agent = request.json.get('userAgent')
    print(f"User-Agent: {user_agent}")  # Логирование в консоль
    return jsonify({"message": "User-Agent logged!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
