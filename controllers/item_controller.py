from flask import request, jsonify
from services.item_service import ItemService


class ItemController:
    @staticmethod
    def create_item():
        data = request.json
        new_item = ItemService.create_item(data)
        return jsonify(new_item.to_dict()), 201

    @staticmethod
    def get_items():
        items = ItemService.get_all_items()
        return jsonify([item.to_dict() for item in items])

    @staticmethod
    def get_item(id):
        item = ItemService.get_item_by_id(id)
        return jsonify(item.to_dict())

    @staticmethod
    def update_item(id):
        data = request.json
        item = ItemService.update_item(id, data)
        return jsonify(item.to_dict())

    @staticmethod
    def delete_item(id):
        ItemService.delete_item(id)
        return '', 204
