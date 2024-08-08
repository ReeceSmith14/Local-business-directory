from directory import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    is_owner = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.username

class Business(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.Integer, ForeignKey('categories.id'), nullable=False)
    business_name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    phone_number = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    website = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.business_name
    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return self.name

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, ForeignKey('businesses.id'), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, ForeignKey('businesses.id'), nullable=False)
    url = db.Column(db.String, nullable=False)
    alt_text = db.Column(db.String, nullable=True)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    
