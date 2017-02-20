from flask import Flask, render_template, request, jsonify
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/movie')
def enternew():
    return render_template('moviePost.html')

@app.route('/movies', methods = {'POST'})
def newpost():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        name = request.form['name']
        favorite_movie = request.form['favorite']
        cursor.execute('INSERT INTO favorite_movies(name, favorite) VALUES(?,?)', (name, favorite_movie))
        connection.commit()
        message = 'I put in that 2 shits inside the 2 shits.'
    except:
        connection.rollback()
        message = 'Shit didn\'t work out, sorry. Figure it out.'
    finally:
        return render_template('results.html', message = message)
        connection.close()
