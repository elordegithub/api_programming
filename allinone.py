from flask import Flask, jsonify, request
from flask_cors import CORS
from flaskext.mysql import MySQL

#Code initializes Flask app and enables Cross-Origin Resource Sharing.
app = Flask(__name__)
CORS(app)

#Configuring MySQL database connection for the app.
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mysqlrootpassword'
app.config['MYSQL_DATABASE_DB'] = 'reservation_db'
mysql = MySQL(app)

#CREATE GUESTS FUNCTION
@app.route('/create', methods=['POST'])
def create_guests():
    try:
        #Parsing JSON request into variables for guest data.
        _json = request.json
        _guest_id = _json['id']
        _guest_firstname = _json['firstname']
        _guest_lastname = _json['lastname']
        _guest_email = _json['email']
        _guest_phone = _json['phone']

        #Checking valid inputs and establishing a database connection.
        if _guest_id and _guest_firstname and _guest_lastname and _guest_email and _guest_phone and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()
        #Executing an SQL query to insert data into the database.
            sqlQuery = "INSERT INTO guests (id, firstname, lastname, email, phone) VALUES (%s, %s, %s, %s, %s)"
            bindData = (_guest_id, _guest_firstname, _guest_lastname, _guest_email, _guest_phone)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
        #Returning a JSON response indicating success or displaying an error.
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


#Defines a route for accessing the "guests" resource.
@app.route('/guests', methods=['GET'])
def guests():
    try:
    #Connects to the database, executes a SELECT query, and retrieves all rows of the "guests" table.
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, firstname, lastname, email, phone FROM guests")
        guestsRows = cursor.fetchall()
    #Returns a JSON response with the fetched "guestsRows" data.
        response = jsonify(guestsRows)
        response.status_code = 200
        return response
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