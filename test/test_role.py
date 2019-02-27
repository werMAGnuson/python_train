from model.role import Role


def test_create_role(app):
    # app.session.login(user_email="sprint52stag1msp@yopmail.com", password="!!TEst123")
    app.role.open_role_page()
    role = Role(name="somename", definition="Admin")
    old_roles = app.role.get_role_list()
    app.role.create(role)
    new_roles = app.role.get_role_list()
    assert len(old_roles) + 1 == len(new_roles)
    old_roles.append(role)
    assert old_roles == new_roles
    # app.session.logout()


def test_modify_role(app):
    # app.session.login(user_email="sprint52stag1msp@yopmail.com", password="!!TEst123")
    app.role.open_role_page()
    old_roles = app.role.get_role_list()
    role = Role(name="somenamenew", definition="Admin")
    app.role.modify(role, Role(name="somename"))
    new_roles = app.role.get_role_list()
    assert len(old_roles) == len(new_roles)
    old_roles[-1].name=role.name
    assert old_roles == new_roles
    # app.role.delete(Role(name="somename", definition="Admin"))
    # app.session.logout()


def test_delete_role(app):
    # app.session.login(user_email="sprint52stag1msp@yopmail.com", password="!!TEst123")
    app.role.open_role_page()
    role = Role(name="somename", definition="Admin")
    if not app.role.role_is_exists(role):
        app.role.create(role)
    old_roles = app.role.get_role_list()
    # app.role.create(Role(name="somename", definition="Admin"))
    app.role.delete(role)
    new_roles = app.role.get_role_list()
    assert len(old_roles) - 1 == len(new_roles)
    old_roles = old_roles[0:-1]
    assert old_roles == new_roles

    # app.session.logout()
