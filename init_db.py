from app import create_app
from extensions import db

app = create_app()

with app.app_context():
    db.drop_all()  # Opcional: Remove todas as tabelas existentes
    db.create_all()
    print("Database reset and initialized successfully.")
