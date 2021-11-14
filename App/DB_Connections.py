#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2021.11.13                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


import mysql.connector
from datetime import datetime


user = "python_db_user"
password = ""
db_name = "CentennialCommunityConnector"


def DB_CONNECTION():
	cnx = mysql.connector.connect(user=user, password=password, host="localhost", port="3306",  database=db_name);
	return cnx, cnx.cursor(buffered=True);


def INSERT_request(email: str, reason: str, time: datetime, EventTypes_id: int, is_virtual: bool, zip: int) -> bool:
	query =	"""
			INSERT INTO `Requests` (`email`, `reason`, `time`, `EventTypes_id`, `is_virtual`, `zip`) VALUES
			(%s, %s, %s, %s, %s, %s);
			"""

	cnx, cursor = DB_CONNECTION()
	cursor.execute(query, email, reason, time, EventTypes_id, is_virtual, zip);
	cnx.commit();
	return cursor.lastrowid;


def INSERT_events(reason: str, EventType_id: int, address: str, state: str, zip: str, time: datetime) -> bool:
	query =	"""
			INSERT INTO `Events` (`reason`, `EventType_id`, `address`, `state`, `zip`, `time`) VALUES
			(%s, %s, %s, %s, %s, %s);
			"""

	cnx, cursor = DB_CONNECTION()
	cursor.execute(reason, EventType_id, address, state, zip, time);
	cnx.commit();
	return cursor.lastrowid;
	

def SELECT_requests_by_Event_id(Events_id: int) -> list:
	query =	"""
			SELECT * FROM `Requests` WHERE `Events.id` = %s;
			"""

	cnx, cursor = DB_CONNECTION()
	cursor.execute(query, Events_id);
	columns = [column[0] for column in cursor._description]
	return [{column: (row[x] if row[x] else None) for x, column in enumerate(headers)} for row in cursor._rows]


def SELECT_event(Events_id: int) -> dict:
	query =	"""
			SELECT * FROM `Requests` WHERE `id` = %s;
			"""

	cnx, cursor = DB_CONNECTION()
	cursor.execute(query, Events_id);
	columns = [column[0] for column in cursor._description]
	return [{column: (row[x] if row[x] else None) for x, column in enumerate(headers)} for row in cursor._rows]


def SELECT_events_by_zip(zip: str) -> dict:
	query =	"""
			SELECT * FROM `Requests` WHERE `zip` = %s;
			"""

	cnx, cursor = DB_CONNECTION()
	cursor.execute(query, zip);
	columns = [column[0] for column in cursor._description]
	return [{column: (row[x] if row[x] else None) for x, column in enumerate(headers)} for row in cursor._rows]


def SELECT_Counselors_by_Events_id(Events_id: int) -> dict:
	query =	"""
			SELECT * FROM `Counselors`
			JOIN `EventsCounselors` ON `Counselors`.`Counselors.id` = `EventsCounselors`.`Events.id`
			WHERE `EventsCounselors`.`Events.id` = %s;
			"""

	cnx, cursor = DB_CONNECTION()
	cursor.execute(query, Events_id);
	columns = [column[0] for column in cursor._description]
	return [{column: (row[x] if row[x] else None) for x, column in enumerate(headers)} for row in cursor._rows]



