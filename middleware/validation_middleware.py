from flask import request, jsonify


def validate_item_data():
    if request.method in ['POST', 'PUT']:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body must be JSON"}), 400
        if 'name' not in data or not data['name']:
            return jsonify({"error": "Name is required"}), 400
    return None
