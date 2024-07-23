from models.item import Item
from extensions import db


class ItemService:
    @staticmethod
    def create_item(data):
        new_item = Item(name=data['name'], description=data.get('description'))
        db.session.add(new_item)
        db.session.commit()
        return new_item

    @staticmethod
    def get_all_items():
        return Item.query.all()

    @staticmethod
    def get_item_by_id(item_id):
        return Item.query.get_or_404(item_id)

    @staticmethod
    def update_item(item_id, data):
        item = Item.query.get_or_404(item_id)
        item.name = data['name']
        item.description = data.get('description')
        db.session.commit()
        return item

    @staticmethod
    def delete_item(item_id):
        item = Item.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return item
