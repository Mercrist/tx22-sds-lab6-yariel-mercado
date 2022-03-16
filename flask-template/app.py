# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ---- YOUR APP STARTS HERE ----
# -- Import section --

"""
Collaborators
------------
Yariel Mercado
Victor Akpan
Pradeep Lamichhane
"""
from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
from model import validate_user_response


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'GET': #if the user tries to directly reach the answers url, redirect
        return redirect(url_for('index'))

    answers = {"New York": request.form['New York'], "California": request.form['California'], 
                "Texas": request.form['Texas'], "Colorado": request.form['Colorado'], "Hawaii": request.form['Hawaii']}

    for state in answers.keys():
        if not answers.get(state):
            return "Fill out each state entry with a valid input!" 

    graded_answ = validate_user_response(answers)
    return render_template("results.html", graded_answ = graded_answ, user_anws = answers)


