from flask import Flask, jsonify

app = Flask(__name__)

# Sample user data
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"},
    {"id": 3, "name": "Alice Brown", "email": "alice@example.com"}
]

@app.route('/users', methods=['GET'])
def get_users():
    """Return the list of all users in JSON format."""
    return jsonify({"users": users})

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    """Return user data for a specific user ID."""
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
