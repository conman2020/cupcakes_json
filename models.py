from flask_sqlalchemy import SQLAlchemy


"""Models for Cupcake app."""
DEFAULT_IMAGE_URL="https://tinyurl.com/demo-cupcake"

db = SQLAlchemy()
DEFAULT_IMAGE_URL="https://tinyurl.com/demo-cupcake"
def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Todo Model"""

    __tablename__ = "cupcakes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)
    def to_dict(self):
        """Returns a dict representation of todo which we can turn into JSON"""
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image_url': self.image_url,

        }

