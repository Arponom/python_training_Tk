# -*- coding: utf-8 -*-
import pytest

from Help_Class_Group import add_new_group
from fixtura.conftest import configurate


#16.09.17

@pytest.fixture
def app(request):
    fixture = configurate()
    request.addfinalizer(fixture.destroyer)
    return fixture

def test_new(app):
    app.auth.login(login_sys="admin", pass_sys="secret")
    app.group.open_page()
    app.group.create(add_new_group(n_name="date1", h_header="date2", f_footer="date3"))
    app.group.open_page()
    app.auth.logout()
    app.destroyer()


