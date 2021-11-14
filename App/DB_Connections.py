#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "MorganPothoff"

########################################################################################################################
#                                                                                                                      #
#   created by: MorganPothoff                                                                                          #
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


def INSERT_request(email: str, reason: str, time: datetime, EventsTypes_id: int, is_virtual: bool, zip: int) -> bool:
	query =	"""
			INSERT INTO `Requests` (`email`, `reason`, `time`, `EventsTypes.id`, `is_virtual`, `zip`) VALUES
			(%s, %s, %s, %s, %s, %s);
			"""

	cnx, cursor = DB_CONNECTION()
	cursor.execute(query, (email, reason, time, EventsTypes_id, is_virtual, zip,));
	cnx.commit();
	return cursor.lastrowid;


def INSERT_events(reason: str, EventsTypes_id: int, address: str, state: str, zip: str, time: datetime) -> bool:
	query =	"""
			INSERT INTO `Events` (`reason`, `EventsTypes.id`, `address`, `state`, `zip`, `time`) VALUES
			(%s, %s, %s, %s, %s, %s);
			"""

	cnx, cursor = DB_CONNECTION()
	cursor.execute(query, (reason, EventsTypes_id, address, state, zip, time,));
	cnx.commit();
	return cursor.lastrowid;
	

def SELECT_eventsTypes() -> list:
	query =	"""
			SELECT * FROM `EventsTypes`;
			"""

	cnx, cursor = DB_CONNECTION()
	cursor.execute(query);
	columns = [column[0] for column in cursor._description]
	return [{column: (row[x] if row[x] else None) for x, column in enumerate(columns)} for row in cursor._rows]


def SELECT_requests_by_Event_id(Events_id: int) -> list:
	query =	"""
			SELECT * FROM `Requests` WHERE `Events.id` = %s;
			"""

	cnx, cursor = DB_CONNECTION()
	cursor.execute(query, (Events_id,));
	columns = [column[0] for column in cursor._description]
	return [{column: (row[x] if row[x] else None) for x, column in enumerate(columns)} for row in cursor._rows]


def SELECT_event(Events_id: int) -> dict:
	query =	"""
			SELECT * FROM `Requests` WHERE `id` = %s;
			"""

	cnx, cursor = DB_CONNECTION()
	cursor.execute(query, (Events_id,));
	columns = [column[0] for column in cursor._description]
	return [{column: (row[x] if row[x] else None) for x, column in enumerate(columns)} for row in cursor._rows]


def SELECT_events_by_zip(zip: str) -> dict:
	query =	"""
			SELECT * FROM `Events` WHERE `zip` = %s;
			"""

	cnx, cursor = DB_CONNECTION()
	cursor.execute(query, (str(zip),));
	columns = [column[0] for column in cursor._description]
	return [{column: (row[x] if row[x] else None) for x, column in enumerate(columns)} for row in cursor._rows]


def SELECT_Counselors_by_Events_id(Events_id: int) -> dict:
	query =	"""
			SELECT * FROM `Counselors`
			JOIN `EventsCounselors` ON `Counselors`.`id` = `EventsCounselors`.`Counselors.id`
			WHERE `EventsCounselors`.`Events.id` = %s;
			"""

	cnx, cursor = DB_CONNECTION()
	cursor.execute(query, (Events_id,));
	columns = [column[0] for column in cursor._description]
	return [{column: (row[x] if row[x] else None) for x, column in enumerate(columns)} for row in cursor._rows]


def SELECT_unique_zip_codes() -> list:
	query =	"""
			SELECT `zip` FROM `Events` GROUP BY `zip`;
			"""

	cnx, cursor = DB_CONNECTION()
	cursor.execute(query);
	return [row[0] for row in cursor._rows]



