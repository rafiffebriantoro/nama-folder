from app import app
from flask import render_template

@app.route('/')
def index():
	return "Hello, World!"

@app.route('/tampil')
def terserah():
	nama = {"panggilan":"wati", "lengkap":"sukowati"}
	return render_template('index.html', a=nama)