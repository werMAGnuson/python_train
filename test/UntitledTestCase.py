# -*- coding: utf-8 -*-


import pytest
from fixture.app import Applikation
from model.staff import Staff


@pytest.fixture()
def app(request):
    fixture = Applikation()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_untitled_test_case(app):
    app.session.login(user_email="sprint52stag1msp@yopmail.com", password="!!TEst123")
    app.staff.create(Staff(staff_name="somename", email="somename@yopmail.com", group_name="Admin"))
    app.staff.delite()
    app.session.logout()


def test_untitled_test_case_somenameu(app):
    app.session.login(user_email="sprint52stag1msp@yopmail.com", password="!!TEst123")
    app.staff.create(Staff(staff_name="somenameu", email="somename@yopmail.com", group_name="Admin"))
    app.staff.delite()
    app.session.logout()


