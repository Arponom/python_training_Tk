# -*- coding: utf-8 -*-
from fixtura import testing
from add_new_group import add_new_group
import pytest


@pytest.fixture
def app(request):
    fixture = testing()
    request.addfinalizer(fixture.teardown1)
    return fixture

def test_new(app):
    app.go_on_page()
    app.auth_on_sys(login_sys="admin", pass_sys="secret")
    app.go_on_group()
    app.create_new_group(add_new_group(n_name="date1", h_header="date2", f_footer="date3"))
    app.go_on_group()
    app.log_off()


