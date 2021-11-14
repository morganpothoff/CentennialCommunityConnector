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


app = Flask(__name__)


@app.route("/")
def root():
	peanut_butter = "Jelly"
	return render_template("Root.html", peanut_butter=peanut_butter)


@app.route("/UpcomingCommunityEvents")
def upcomingCommunityEvents():
	peanut_butter = "Jelly"
	return render_template("Root.html", peanut_butter=peanut_butter)


@app.route("/HostAnEvent")
def hostAnEvent():
	peanut_butter = "Jelly"
	return render_template("Root.html", peanut_butter=peanut_butter)


@app.route("/FindSupportGroupsNearMe")
def findSupportGroupsNearMe():
	peanut_butter = "Jelly"
	return render_template("Root.html", peanut_butter=peanut_butter)


@app.route("/StartASupportGroupOnline")
def startASupportGroupOnline():
	peanut_butter = "Jelly"
	return render_template("Root.html", peanut_butter=peanut_butter)



app.run(host="localhost", port=80)

