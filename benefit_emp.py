import pymysql
from app import app
from config import mysql
from flask import jsonify, request

@app.route('/benefit', methods=['GET'])
def benefit():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT rest_emp.id, name, position, experiences, insuarance,last_salary,PA_Toeic, PA_Perform ,current_salary FROM rest_emp, bnf_emp where rest_emp.id = bnf_emp.id ORDER BY rest_emp.id desc")
		empRows = cursor.fetchall()
		respone = jsonify(empRows)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/search/benefit/<string:input>')
def benefit_search(input):
	try:
		sqlQuery = "SELECT name, position, experiences, insuarance,last_salary,PA_Toeic, PA_Perform ,current_salary FROM \
        rest_emp, bnf_emp where rest_emp.id = bnf_emp.id and (name like %s or position like %s or experiences like %s or insuarance like %s \
        or last_salary like %s or PA_Toeic like %s or PA_Perform like %s or current_salary like %s)" # Query Mysql
		bindData = (input+'%', input+'%', input+'%', input+'%', input+'%', input+'%', input+'%', input+'%') # Data input (tuple)
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute(sqlQuery, bindData)
		empRow = cursor.fetchall()
		respone = jsonify(empRow)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/benefit/edit/<int:id>')
def benefit_edit(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT name, position, experiences, insuarance,last_salary,PA_Toeic, PA_Perform ,current_salary \
			FROM rest_emp, bnf_emp where rest_emp.id = bnf_emp.id and rest_emp.id = %s", id)
		empRow = cursor.fetchone()
		respone = jsonify(empRow)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/update/benefit/<int:id>', methods=['PUT'])
def update_emp_benefit(id):
	_json = request.json
	
	_json = request.json
	_experiences = _json['experiences']
	_insuarance = _json['insuarance']
	_last_salary = _json['last_salary']
	_current_salary = _json['current_salary']
	_PA_Toeic = _json['PA_Toeic']
	_PA_Perform = _json['PA_Perform']

	# validate the received values
	# if _experiences  and _insuarance and _last_salary and _current_salary and _PA_Toeic and _PA_Perform and id and request.method == 'PUT':			
	sqlQuery = "UPDATE bnf_emp SET experiences=%s, insuarance=%s, last_salary=%s, current_salary=%s, PA_Toeic=%s, PA_Perform=%s WHERE bnf_emp.id=%s"
	bindData = (_experiences, _insuarance, _last_salary, _current_salary, _PA_Toeic, _PA_Perform, id,)
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute(sqlQuery, bindData)
	conn.commit()
	respone = jsonify('Benefit updated successfully!')
	respone.status_code = 200
	return respone
	# else:
	# 	return not_found()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone