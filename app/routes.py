import os
import secrets

from flask import \
    (render_template, send_from_directory, session, request, redirect, url_for, flash, abort)
from flask_login import \
    (login_required, login_user, current_user, logout_user)
from app import (app, bcrypt)


@app.route("/robots.txt")
def robots(): return send_from_directory(app.static_folder, "robots.txt")


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    return render_template('survey.html')


@app.route('/survey/school-health-program/demographics', methods=['GET', 'POST'])
def demographics():
    return render_template('survey/school_health_program/demographics.html')


@app.route('/survey/school-health-program/referral', methods=['GET', 'POST'])
def referral():
    return render_template('survey/school_health_program/referral.html')


@app.route('/survey/school-health-program/vital-signs', methods=['GET', 'POST'])
def vital_signs():
    return render_template('survey/school_health_program/vital_signs.html')


@app.route('/survey/school-health-program/family', methods=['GET', 'POST'])
def family():
    return render_template('survey/school_health_program/family.html')


@app.route('/survey/school-health-program/physical-examination', methods=['GET', 'POST'])
def physical_examination():
    return render_template('survey/school_health_program/physical_examination.html')


@app.route('/survey/school-health-program/hearing', methods=['GET', 'POST'])
def hearing():
    return render_template('survey/school_health_program/hearing.html')


@app.route('/survey/school-health-program/dental', methods=['GET', 'POST'])
def dental():
    return render_template('survey/school_health_program/dental.html')


@app.route('/survey/school-health-program/psychosocial', methods=['GET', 'POST'])
def psychosocial():
    return render_template('survey/school_health_program/psychosocial.html')


