from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# הגדרת URI של מסד הנתונים, למשל SQLite מקומי
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# יצירת אובייקט SQLAlchemy
db = SQLAlchemy(app)

# דוגמה למודל


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# יצירת מסד הנתונים


@app.before_first_request
def create_tables():
    db.create_all()

# נתיב בסיסי להצגת משתמשים


@app.route('/')
def index():
    users = User.query.all()
    return f"All users: {users}"

# הוספת נתיב להוספת משתמש


@app.route('/add_user/<username>/<email>')
def add_user(username, email):
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return f"Added user {username} with email {email}"


if __name__ == "__main__":
    app.run(debug=True)
