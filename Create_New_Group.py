# -*- coding: utf-8 -*-
from Create_Group_Fixtura import testing
from Help_Class_Group import add_new_group
import pytest
#16.09.17

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


