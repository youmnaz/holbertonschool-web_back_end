#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify
from auth import Auth

app = Flask(__name__)
AUTH = Auth()

@app.route('/', methods=['GET'], strict_slashes=False)
def hello() -> str:
    """welcome msg"""
    return jsonify({"message": "Bienvenue"}), 200

@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """registering the user"""
    email = request.form('email')
    password = request.form('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({{"email": {email}, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
