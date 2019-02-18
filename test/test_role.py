from model.role import Role


def test_create_role(app):
    app.session.login(user_email="sprint52stag1msp@yopmail.com", password="!!TEst123")
    app.role.opan_to_roles()
    app.role.create(Role(name="somename", definition="Admin"))
    #app.role.delite(Role(name="somename", definition="Admin"))
    #app.session.logout()
def test_modify_role(app):
    #app.session.login(user_email="sprint52stag1msp@yopmail.com", password="!!TEst123")
    app.role.opan_to_roles()
    app.role.modify(Role(name="somenamenew", definition="Admin"), Role(name="somename", definition="Admin"))
    #app.role.delite(Role(name="somename", definition="Admin"))
    #app.session.logout()
def test_delite_role(app):
    #app.session.login(user_email="sprint52stag1msp@yopmail.com", password="!!TEst123")
    app.role.opan_to_roles()
    #app.role.create(Role(name="somename", definition="Admin"))
    app.role.delite(Role(name="somename", definition="Admin"))
    #app.session.logout()
