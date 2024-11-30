from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MySQL Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root@123',
    'database': 'test'
}

# Test MySQL Connection
def connect_to_db():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    return None

# POST: Add a new record
@app.route('/users', methods=['POST'])
def add_record():
    data = request.json
    name = data.get('name')
    age = data.get('age')

    if not name or not age:
        return jsonify({"error": "Missing name or age"}), 400

    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO users (name, age) VALUES (%s, %s)"
            cursor.execute(query, (name, age))
            connection.commit()
            return jsonify({"message": "Record added successfully"}), 201
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            connection.close()
    return jsonify({"error": "Database connection failed"}), 500

# PUT: Update an existing record
@app.route('/users/<int:id>', methods=['PUT'])
def update_record(id):
    data = request.json
    name = data.get('name')
    age = data.get('age')

    if not name and not age:
        return jsonify({"error": "Nothing to update"}), 400

    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            query = "UPDATE users SET name = %s, age = %s WHERE id = %s"
            cursor.execute(query, (name, age, id))
            connection.commit()
            if cursor.rowcount == 0:
                return jsonify({"error": "Record not found"}), 404
            return jsonify({"message": "Record updated successfully"}), 200
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            connection.close()
    return jsonify({"error": "Database connection failed"}), 500

# DELETE: Delete a record
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_record(id):
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM users WHERE id = %s"
            cursor.execute(query, (id,))
            connection.commit()
            if cursor.rowcount == 0:
                return jsonify({"error": "Record not found"}), 404
            return jsonify({"message": "Record deleted successfully"}), 200
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            connection.close()
    return jsonify({"error": "Database connection failed"}), 500

if __name__ == '__main__':
    app.run(debug=True)
