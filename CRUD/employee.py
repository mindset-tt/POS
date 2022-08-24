from Config_Database import config
from Error import error
from flask import jsonify, request
import pymysql

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

@config.app.route('/create_employee', methods=['POST'])
def create_emp():
    try:

        _json = request.json
        _emp_id = _json['emp_id']
        _name = _json['emp_name']
        _surname = _json['emp_surname']
        _tel = _json['emp_tel']
        _village = _json['village']
        _district = _json['district']
        _pos_ID = _json['pos_ID']
        _dep_ID = _json['dep_ID']
        _provID = _json['prov_ID']
        _emp_profilepic = _json['emp_profilepic']
        if _emp_id and _name and _surname and _tel and _village and _district and _pos_ID and _dep_ID and _provID and _emp_profilepic:
            conn = config.conp
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO test.employee(emp_id, emp_name, emp_surname, emp_tel, village, district, pos_ID, dep_ID, prov_ID, emp_profilepic) VALUES(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            _emp_profilepic = convertToBinaryData(_emp_profilepic)
            bindData = (_emp_id, _name, _surname, _tel, _village,
                        _district, _pos_ID, _dep_ID, _provID, _emp_profilepic)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Employee added successfully!')
            respone.status_code = 200
            return respone
        else:
            return error.not_found()
    except Exception as e:
        print(e)


@config.app.route('/employee')
def emp():
    try:
        conn = config.conp
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM employee")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)

@config.app.route('/employee/<string:emp_id>')
def emp_details(emp_id):
    try:
        conn = config.conp
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT * FROM employee WHERE id = %s", emp_id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)

@config.app.route('/update_employee', methods=['PUT'])
def update_emp():
    try:
        _json = request.json
        _name = _json['emp_name']
        _surname = _json['emp_surname']
        _tel = _json['emp_tel']
        _village = _json['village']
        _district = _json['district']
        _pos_ID = _json['pos_ID']
        _dep_ID = _json['dep_ID']
        _provID = _json['prov_ID']
        _emp_profilepic = _json['emp_profilepic']
        if _name and _surname and _tel and _village and _district and _pos_ID and _dep_ID and _provID and _emp_profilepic and request.method == 'PUT':
            conn = config.conp
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "UPDATE employee SET emp_name = %s, emp_surname = %s, emp_tel = %s, village = %s, district = %s, pos_ID = %s, dep_ID = %s, prov_ID = %s, emp_profilepic = %s WHERE id = %s"
            _emp_profilepic = convertToBinaryData(_emp_profilepic)
            bindData = (_name, _surname, _tel, _village, _district,
                        _pos_ID, _dep_ID, _provID, _emp_profilepic, _json['id'])
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Employee updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return error.not_found()
    except Exception as e:
        print(e)

@config.app.route('/delete_employee/<string:id>', methods=['DELETE'])
def delete_emp(id):
    try:
        conn = config.conp
        cursor = conn.cursor()
        cursor.execute("DELETE FROM test.employee WHERE id =%s", (id,))
        conn.commit()
        respone = jsonify('Employee deleted successfully!')
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)