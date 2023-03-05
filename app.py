from flask import Flask, render_template, request
import sqlite3 as sql
import random

app = Flask(__name__)

host = 'http://127.0.0.1:5000/'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/name', methods=['POST', 'GET'])
def name():
    error = None
    if request.method == 'POST':
        result = valid_name(request.form['FirstName'], request.form['LastName'])
        if result:
            return render_template('input.html', error=error, result=result)
        else:
            error = 'invalid input name'
    return render_template('input.html', error=error)


@app.route('/delete', methods=['POST', 'GET'])
def delete_name():
    error = None
    if request.method == 'POST':
        result = valid_name_delete(request.form['FirstName'], request.form['LastName'])
        if result:
            return render_template('delete.html', error=error, result=result)
        else:
            error = 'invalid input name'
    return render_template('delete.html', error=error)


def valid_name(first_name, last_name):
    connection = sql.connect('database.db')
    connection.execute('CREATE TABLE IF NOT EXISTS users(pid integer, firstname TEXT, lastname TEXT);')
    lst = range(0, 1000000)
    pid = random.choice(lst)
    connection.execute('INSERT INTO users (pid, firstname, lastname) VALUES (?,?,?);', (pid, first_name, last_name))
    connection.commit()
    cursor = connection.execute('SELECT * FROM users;')
    return cursor.fetchall()


def valid_name_delete(first_name, last_name):
    connection = sql.connect('database.db')
    connection.execute('CREATE TABLE IF NOT EXISTS users(pid integer, firstname TEXT, lastname TEXT);')
    connection.execute('DELETE FROM users WHERE firstname =  (?) AND lastname = (?);', (first_name, last_name))
    connection.commit()
    cursor = connection.execute('SELECT * FROM users;')
    return cursor.fetchall()


if __name__ == "__main__":
    app.run()
