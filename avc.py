from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def handle_command():
    data = request.json
    command = data.get("command")
    if command == "Routing Action":
        # Example response
        return jsonify({"status": "playing", "component": "Received})
    else:
        return jsonify({"status": "error", "message": "Unknown command"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
