from model.role import Role


def test_create_role(app):
    # app.session.login(user_email="sprint52stag1msp@yopmail.com", password="!!TEst123")
    app.role.open_role_page()
    old_roles = app.role.get_role_list()
    app.role.create(Role(name="somename", definition="Admin"))
    new_roles = app.role.get_role_list()
    assert len(old_roles) + 1 == len(new_roles)
    # app.session.logout()


def test_modify_role(app):
    # app.session.login(user_email="sprint52stag1msp@yopmail.com", password="!!TEst123")
    app.role.open_role_page()
    app.role.modify(Role(name="somenamenew", definition="Admin"), Role(name="somename"))
    # app.role.delete(Role(name="somename", definition="Admin"))
    # app.session.logout()


def test_delete_role(app):
    # app.session.login(user_email="sprint52stag1msp@yopmail.com", password="!!TEst123")
    app.role.open_role_page()
    if not app.role.role_is_exists((Role(name="somename", definition="Admin"))):
        app.role.create(Role(name="somename", definition="Admin"))
    old_roles = app.role.get_role_list()
    # app.role.create(Role(name="somename", definition="Admin"))
    app.role.delete(Role(name="somename", definition="Admin"))
    new_roles = app.role.get_role_list()
    assert len(old_roles) - 1 == len(new_roles)
    # app.session.logout()
