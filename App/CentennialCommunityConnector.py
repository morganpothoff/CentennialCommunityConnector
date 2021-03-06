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


from flask import *
from datetime import datetime

import DB_Connections


app = Flask(__name__, static_url_path="/static")


@app.route("/")
def root():
	return render_template("Root.html")


@app.route("/UpcomingCommunityEvents")
def upcomingCommunityEvents():
	zip = request.args.get("zip_code", "")
	if(zip):
		events = DB_Connections.SELECT_events_by_zip(zip)
		for event in events:
			event["counselors"] = DB_Connections.SELECT_Counselors_by_Events_id(event["id"])

		return render_template("UpcomingCommunityEvents.html", events=events, zip_code=zip)
	
	zip_codes = DB_Connections.SELECT_unique_zip_codes()
	return render_template("UpcomingCommunityEvents.html", zip_code=zip, zip_codes=zip_codes)


@app.route("/HostAnEvent", methods=["GET", "POST"])
def hostAnEvent():
	if(request.method == "POST"):
		try:
			print(request.form.get("date"), request.form.get("time"))
			email = request.form.get("email")
			reason = request.form.get("description")
			time = datetime.strptime(request.form.get("date")+" "+request.form.get("time"), "%Y-%m-%d %H:%M")
			EventTypes_id = request.form.get("event_type")
			is_virtual = request.form.get("is_virtual")
			zip = request.form.get("zip")

			DB_Connections.INSERT_request(email, reason, time, EventTypes_id, is_virtual, zip)

			return "<p>Successfully Submitted</p><a href='/'>Return to home</a>"
		except Exception as error:
			return f"<p>ERROR: {str(error)}</p><a href='/'>Return to home</a>"
	# GET method
	else:
		event_types = DB_Connections.SELECT_eventsTypes()
		event_types = [{**e, **{"label": (e["LABEL"] if "LABEL" in e else e["label"])}} for e in event_types]
		return render_template("HostAnEvent.html", event_types=event_types)


@app.route("/FindSupportGroupsNearMe")
def findSupportGroupsNearMe():
	return render_template("SupportGroupNearMe.html")


@app.route("/StartASupportGroupOnline")
def startASupportGroupOnline():
	return render_template("NewSupportGroup.html")


@app.route("/login")
def login():
	return "<p>login is a work in progress</p>"



app.run(host="localhost", port=8000, debug=True)

