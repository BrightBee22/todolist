from application import db
from datetime import datetime

class Tasks(db.model):
    id = db.column(db.Integer, primary_key=True)
    description = db.column(db.String(100), nullable=False)
    completed = db.column(db.Boolean, nullable=False, default=False)
    date_created = db.column(db.DateTime, nullable=False, default=datetime=datetime.now())