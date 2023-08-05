from functions.CreateNewUser import CreateNewUser


visit_url = CreateNewUser()

if __name__ == "__main__":
    visit_url.visit_page()
    visit_url.register_btn()
    visit_url.register_form()
    visit_url.profile_details()
    visit_url.logout_user()
    visit_url.login_btn()
    visit_url.login_form()
