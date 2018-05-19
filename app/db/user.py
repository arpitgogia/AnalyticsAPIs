from app import db
import json
import jwt
import sqlalchemy
import time

def generateToken(install_time):
	id = jwt.encode({'time': time.time()}, 'secret', algorithm='HS256')

	with db.engine.connect() as connection:
		result = connection.execute(sqlalchemy.text("""
				INSERT INTO users (id, install_time) values (:id, to_timestamp(:install_time))
				RETURNING id
			"""), {
			"id": id.decode("utf-8"),
			"install_time": install_time
		})
		return json.dumps({"status": 200, "id": (result.fetchone()["id"])})

def insertEventLog(data):
	id = data["id"]

	with db.engine.connect() as connection:
		checkForUser = connection.execute(sqlalchemy.text("""
				SELECT * from users where id = (:id)
			"""), {
			"id": id
		})

		if checkForUser.rowcount:
			insertStmt = ''
			compatibleData = {}
			compatibleData['id'] = id

			for i in range(len(data["data"])):
				event = data["data"][i]
				insertStmt += '(:id, '

				for key in event:
					print(key)
					if key == 'time':
						insertStmt += 'to_timestamp(:' + str(key) + str(i) + '), '
					else:
						insertStmt += ':' + str(key) + str(i) + ', '
					if isinstance(event[key], dict):
						compatibleData[str(key) + str(i)] = json.dumps(event[key])
					else:
						if key == 'time':
							compatibleData[str(key) + str(i)] = ((int)(event[key])) / 1000
						else:
							compatibleData[str(key) + str(i)] = event[key]

				insertStmt = insertStmt[:-2]
				insertStmt += '),'
				
			insertStmt = insertStmt[:-1]

			result = connection.execute(sqlalchemy.text("""
					INSERT INTO eventLog (id, time, type, data)
					values 
				""" + insertStmt), compatibleData)



	return json.dumps({"status": 200, "id": "Inserted successfully"})