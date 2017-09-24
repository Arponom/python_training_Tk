

def test_edit_address(app):
    app.adress.open_page()
    app.adress.page_auth(login_syss="admin", pass_syss="secret")
    app.adress.click()
    app.adress.edit_address(firstname_='111', middlename_='111', lastname_='111', nickname_='111',
                            title_='111', company_='111', address_='111',
                            home_='111', mobile_='111', work_='111', fax_='111',
                            email_='111')
    app.auth.logout_gr()
