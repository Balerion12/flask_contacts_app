from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL conexion
app.config['MYSQL_HOST'] = 'den1.mysql2.gear.host'
app.config['MYSQL_USER'] = 'flaskcontacts'
app.config['MYSQL_PASSWORD'] = 'Ei9__DMKafe1'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

# settings
app.secret_key = 'mysecretkey'

@app.route('/', methods=["GET"])
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contactos')
    data = cur.fetchall() 
    return render_template('index.html', contactos = data)

@app.route('/add_contact', methods=["POST"])
def add_contact():
    if request.method == "POST":
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contactos (fullname, phone, email) VALUES (%s, %s, %s)',
        (fullname, phone, email))
        mysql.connection.commit()
        flash('Contacto agregado')
        return redirect(url_for('Index'))

@app.route('/edit')
def edit_contact():
    return 'edit contact'

@app.route('/delete')
def delete_contact():
    return 'delete contact'

if __name__ == '__main__':
    app.run(debug = True)