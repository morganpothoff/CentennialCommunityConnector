#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by:                                                                                                        #
#   on 2021.11.13                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


from flask import *
import DB_Connections


app = Flask(__name__)


@app.route("/")
def root():
	peanut_butter = "Jelly"
	return render_template("Root.html", peanut_butter=peanut_butter)


@app.route("/UpcomingCommunityEvents")
def upcomingCommunityEvents():
	zip_code = request.args.get("zip_code", "")
	if(zip_code):
		print(f"Your zip code is {zip_code}")
		# events = DB_Connections.SELECT_events_by_zip(zip_code)
		events = []
		return render_template("UpcomingCommunityEvents.html", events=events, zip_code=zip_code)
	
	return render_template("UpcomingCommunityEvents.html", zip_code=zip_code)


@app.route("/HostAnEvent")
def hostAnEvent():
	event_type = [{"label": "asdfg", "id": 1}, {"label": "qwerty", "id": 2}, {"label": "zxcvb", "id": 3}]
	return render_template("HostAnEvent.html", event_type=event_type)


@app.route("/FindSupportGroupsNearMe")
def findSupportGroupsNearMe():
	peanut_butter = "Jelly"
	return render_template("Root.html", peanut_butter=peanut_butter)


@app.route("/StartASupportGroupOnline")
def startASupportGroupOnline():
	peanut_butter = "Jelly"
	return render_template("Root.html", peanut_butter=peanut_butter)



app.run(host="localhost", port=80)

