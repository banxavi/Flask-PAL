import pymysql
from app import app
from config import mysql
from flask import jsonify, request


@app.route('/emp', methods=['GET'])
def emp():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, name, email, password ,phone, address, image FROM rest_emp")
		empRows = cursor.fetchall()
		respone = jsonify(empRows)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/emp/<int:id>')
def emp_id(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, name, email, phone, address FROM rest_emp WHERE id =%s", id)
		empRow = cursor.fetchone()
		respone = jsonify(empRow)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

		
@app.route('/add', methods=['POST'])
def add_emp():
	
	_json = request.json
	_name = _json['name']
	_email = _json['email']
	_phone = _json['phone']
	_address = _json['address']	
	_password = _json['password']		
	if _name and _email and _phone and _address and _password and request.method == 'POST':			
		sqlQuery = "INSERT INTO rest_emp(name, email, password, phone, address) VALUES(%s, %s, %s, %s, %s)"
		bindData = (_name, _email, _password, _phone, _address)
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(sqlQuery, bindData)
		conn.commit()
		respone = jsonify('Employee added successfully!')
		respone.status_code = 200
		return respone
	else:
		return not_found()


@app.route('/update', methods=['PUT'])
def update_emp():
	
	_json = request.json
	_id = _json['id']
	_name = _json['name']
	_email = _json['email']
	_phone = _json['phone']
	_address = _json['address']
	# validate the received values
	if _name and _email and _phone and _address and _id and request.method == 'PUT':			
		sqlQuery = "UPDATE rest_emp SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s"
		bindData = (_name, _email, _phone, _address, _id,)
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(sqlQuery, bindData)
		conn.commit()
		respone = jsonify('Employee updated successfully!')
		respone.status_code = 200
		return respone
		

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_emp(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM rest_emp WHERE id =%s", (id,))
		conn.commit()
		respone = jsonify('Employee deleted successfully!')
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
		
if __name__ == "__main__":
    app.run(debug=True)