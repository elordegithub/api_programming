from flask import Flask, jsonify, request
from flask_cors import CORS
from flaskext.mysql import MySQL
#first commit para sa pag import ng mga modules

app = Flask(__name__)
CORS(app)
#Code initializes Flask app and enables Cross-Origin Resource Sharing.

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mysqlrootpassword'
app.config['MYSQL_DATABASE_DB'] = 'reservation_db'

mysql = MySQL(app)

#CREATE GUESTS FUNCTION
@app.route('/create', methods=['POST'])
def create_guests():
    try:
        _json = request.json
        _guest_id = _json['id']
        _guest_firstname = _json['firstname']
        _guest_lastname = _json['lastname']
        _guest_email = _json['email']
        _guest_phone = _json['phone']

        if _guest_id and _guest_firstname and _guest_lastname and _guest_email and _guest_phone and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()
            sqlQuery = "INSERT INTO guests (id, firstname, lastname, email, phone) VALUES (%s, %s, %s, %s, %s)"
            bindData = (_guest_id, _guest_firstname, _guest_lastname, _guest_email, _guest_phone)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Guest added successfully!')
            response.status_code = 200
            return response
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#ERROR HANDLER FUNCTION
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run()