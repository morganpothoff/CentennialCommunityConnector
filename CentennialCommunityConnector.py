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
def hello_world():
	peanut_butter = "Jelly"
	return render_template("Root.html", peanut_butter=peanut_butter)


app.run(host="localhost", port=80)

