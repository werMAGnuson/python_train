# -*- coding: utf-8 -*-

from model.staff import Staff



def test_create_delite_staff(app):
    #app.session.login(user_email="sprint52stag1msp@yopmail.com", password="!!TEst123")
    app.staff.create(Staff(staff_name="somename", email="somename@yopmail.com", group_name="Admin"))
    app.staff.delite()
    #app.session.logout()


def test_create_delite_staff_somenameu(app):
    #app.session.login(user_email="sprint52stag1msp@yopmail.com", password="!!TEst123")
    app.staff.create(Staff(staff_name="somenameu", email="somename@yopmail.com", group_name="Admin"))
    app.staff.delite()
    #app.session.logout()

