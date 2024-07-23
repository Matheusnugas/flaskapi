from flask import Blueprint
from controllers.item_controller import ItemController

item_bp = Blueprint('item_bp', __name__)

item_bp.route('/items', methods=['POST'])(ItemController.create_item)
item_bp.route('/items', methods=['GET'])(ItemController.get_items)
item_bp.route('/items/<int:id>', methods=['GET'])(ItemController.get_item)
item_bp.route('/items/<int:id>', methods=['PUT'])(ItemController.update_item)
item_bp.route('/items/<int:id>', methods=['DELETE'])(ItemController.delete_item)
