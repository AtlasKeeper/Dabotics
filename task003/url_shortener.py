from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url_shortener.db'
db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.String(6), primary_key=True)
    original_url = db.Column(db.String(200), nullable=False, unique=True)

# Create the tables within the Flask application context
with app.app_context():
    db.create_all()

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']

    # Validate URL
    if not original_url.startswith(('http://', 'https://')):
        return render_template('error.html', message='Invalid URL. Please include http:// or https://')

    # Check if the URL is already in the database
    existing_entry = URL.query.filter_by(original_url=original_url).first()
    if existing_entry:
        short_url = existing_entry.id
    else:
        # Generate a new short URL
        short_url = generate_short_code()
        new_url_entry = URL(id=short_url, original_url=original_url)
        db.session.add(new_url_entry)
        db.session.commit()

    return render_template('result.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_original(short_url):
    url_entry = URL.query.get(short_url)
    if url_entry:
        original_url = url_entry.original_url
        return redirect(original_url)
    else:
        return render_template('error.html', message='Short URL not found'), 404

if __name__ == '__main__':
    app.run(debug=True)
