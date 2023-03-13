from . import db


class Properties(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(5000))
    roomnum = db.Column(db.Integer)
    bathnum = db.Column(db.Integer)
    price = db.Column(db.String(15))
    propertytype = db.Column(db.String(255))
    location = db.Column(db.String(255))
    photo = db.Column(db.String(255))

    def __init__(self, title, description, roomnum, bathnum, price, propertytype, location, photo):
        self.title = title
        self.description = description
        self.roomnum = roomnum
        self.bathnum = bathnum
        self.price = price
        self.propertytype = propertytype
        self.location = location
        self.photo = photo

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support