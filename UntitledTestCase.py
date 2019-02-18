# -*- coding: utf-8 -*-


import pytest
from app import Applikation
from staff import Staff


@pytest.fixture()
def app(request):
    fixture = Applikation()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_untitled_test_case(app):
    app.open_page()
    app.login(user_email="sprint52stag1msp@yopmail.com", password="!!TEst123")
    app.create_staff(Staff(staff_name="somename", email="somename@yopmail.com", group_name="Admin"))
    app.delite_staff()
    app.logout()


def test_untitled_test_case_somenameu(app):
    app.open_page()
    app.login(user_email="sprint52stag1msp@yopmail.com", password="!!TEst123")
    app.create_staff(Staff(staff_name="somenameu", email="somename@yopmail.com", group_name="Admin"))
    app.delite_staff()
    app.logout()


