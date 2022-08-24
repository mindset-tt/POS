from Config_Database import config
from Error import error
from flask import jsonify, request
import pymysql

@config.app.route('/create_department', methods=['POST'])
def create_department():
    try:
        _json = request.json
        _dep_name = _json['dep_name']
        # _dep_created_date = _json['dep_created_date']
        _dep_level = _json['dep_level']
        if _dep_name and _dep_level and request.method == 'POST':
            conn = config.conp
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO test.department(dep_name, dep_level) VALUES(%s, %s)"
            bindData = (_dep_name, _dep_level)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Department added successfully!')
            respone.status_code = 200
            return respone
        else:
            return error.not_found()
    except Exception as e:
        print(e)

@config.app.route('/department', methods=['GET'])
def department():
    try:
        conn = config.conp
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM department")
        depRows = cursor.fetchall()
        respone = jsonify(depRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)

@config.app.route('/department/<int:dep_id>', methods=['GET'])
def department_details(dep_id):
    try:
        conn = config.conp
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM department WHERE dep_ID = %s", dep_id)
        depRow = cursor.fetchone()
        respone = jsonify(depRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)

@config.app.route('/update_department', methods=['PUT'])
def update_department():
    try:
        _json = request.json
        _dep_ID = _json['dep_ID']
        _dep_name = _json['dep_name']
        _dep_level = _json['dep_level']
        if _dep_ID and _dep_name and _dep_level and request.method == 'PUT':
            conn = config.conp
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "UPDATE department SET dep_name = %s, dep_level = %s WHERE dep_ID = %s"
            bindData = (_dep_name, _dep_level, _dep_ID)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Department updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return error.not_found()
    except Exception as e:
        print(e)

@config.app.route('/delete_department/<string:dep_id>', methods=['DELETE'])
def delete_department(dep_id):
    try:
        conn = config.conp
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "DELETE FROM department WHERE dep_ID =%s", (dep_id,))
        conn.commit()
        respone = jsonify('Department deleted successfully!')
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)