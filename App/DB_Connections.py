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
	query = """
			INSERT INTO `Requests` (`email`, `reason`, `time`, `EventTypes_id`, `is_virtual`, `zip`) VALUES
			(%s, %s, %s, %s, %s, %s);
			"""

	cnx, cursor = DB_CONNECTION()
	cursor.execute(query, email, reason, time, EventTypes_id, is_virtual, zip);
	cnx.commit();
	return cursor.lastrowid;


