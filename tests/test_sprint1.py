from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # First run: Working Test Cases - 19 . Failed Test Cases 0
    # Second run: Working Test Cases - 18 . Failed Test Cases 1

    # The login page opens successfully
    def test_login_to_role_page(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type="html/text")
        self.assertIn(b'Login Page', response.data)

    # The registeration page opens successfully
    def test_register_to_role_page(self):
        tester = app.test_client(self)
        response = tester.get('/register', content_type="html/text")
        self.assertIn(b'Registration Page', response.data)

    # The Hospital login page opens successfully
    def test_login_Hospital_role(self):
        tester = app.test_client(self)
        response = tester.post(
            '/sign-in', data=dict(roles="Hospital"), follow_redirects=True)
        self.assertIn(b'Hospital\'s Login', response.data)

    # The Agent login page opens successfully
    def test_login_agent_role(self):
        tester = app.test_client(self)
        response = tester.post(
            '/sign-in', data=dict(roles="Agent"), follow_redirects=True)
        self.assertIn(b'Agent\'s Login', response.data)

    # The Visitor registeration page opens successfully
    def test_register_visitor_role(self):
        tester = app.test_client(self)
        response = tester.post(
            '/sign-up', data=dict(roles="Visitor"), follow_redirects=True)
        self.assertIn(b'Visitor\'s Registration', response.data)

    # The Place Owner registeration page opens successfully
    def test_register_place_owner_role(self):
        tester = app.test_client(self)
        response = tester.post(
            '/sign-up', data=dict(roles="Place Owner"), follow_redirects=True)
        self.assertIn(b'Place Owner\'s Registration', response.data)

    def test_login_hospital_account_success(self):
        tester = app.test_client(self)
        response = tester.post(
            '/authenticate', data=dict(hospitalUsername="das", hpass="12345asd"), follow_redirects=True)
        self.assertIn(b'Hospital\'s Home Page', response.data)

    def test_login_agent_account_success(self):
        tester = app.test_client(self)
        response = tester.post(
            '/authenticate', data=dict(agentUsername="asd", apass="asdas1221"), follow_redirects=True)
        self.assertIn(b'Agent\'s Home Page', response.data)

    def test_login_agent_account_unsuccess(self):
        tester = app.test_client(self)
        response = tester.post(
            '/authenticate', data=dict(agentUsername="dfg", apass="asfsw234"), follow_redirects=True)
        self.assertIn(b'Invalid Credentials! Please Try again', response.data)

    # invalid credentials for hospital account login
    def test_login_hospital_account_unsuccess(self):
        tester = app.test_client(self)
        response = tester.post(
            '/authenticate', data=dict(hospitalUsername="sad", hpass="asfdsd5654"), follow_redirects=True)
        self.assertIn(b'Invalid Credentials! Please Try again', response.data)

    def test_register_place_acount_success(self):
        tester = app.test_client(self)
        response = tester.post(
            '/register/owner', data=dict(placeName="something 36", placeAddress="somewhere 83"), follow_redirects=True)
        self.assertIn(b'QR for:', response.data)

    # this test will fail after the first time you run the tests because of duplicate
    def test_register_visitor_acount_success(self):
        tester = app.test_client(self)
        response = tester.post(
            '/register/visitor', data=dict(name="something 6", address="somewhere 8", number="0123223343", email="asd@sd.co"), follow_redirects=True)
        self.assertIn(b'QR Scanner Page', response.data)

    # invalid input for visitor account login
    def test_register_visitor_acount_unsuccess(self):
        tester = app.test_client(self)
        response = tester.post(
            '/register/visitor', data=dict(name="something 6", address="somewhere 8", number="0123223343", email="asd@sd.co"), follow_redirects=True)
        self.assertIn(b'Unable to register! Please Try again.', response.data)

    def test_profile_Agent_role(self):
        with app.test_client() as testClient:
            with testClient.session_transaction() as session:
                session['username'] = "asd"
        response = testClient.get(
            '/profile', content_type="html/text")
        self.assertIn(b'Hello, asd', response.data)

    def test_profile_Hospital_role(self):
        with app.test_client() as testClient:
            with testClient.session_transaction() as session:
                session['username'] = "das"
        response = testClient.get(
            '/profile', content_type="html/text")
        self.assertIn(b'Hello, das', response.data)

    def test_profile_visitor_role(self):
        with app.test_client() as testClient:
            with testClient.session_transaction() as session:
                session["name"] = "John"
                session['email'] = "jhn@gm.co"
                session['number'] = "0123432644"
                session['address'] = "college ring 9"
        response = testClient.get(
            '/profile', content_type="html/text")
        self.assertIn(b'Hello, John', response.data)

    def test_profile_place_role(self):
        with app.test_client() as testClient:
            with testClient.session_transaction() as session:
                session["place_name"] = "Rockies"
        response = testClient.get(
            '/profile', content_type="html/text")
        self.assertIn(b'Hello, Rockies', response.data)

    # visitor profile data update success
    def test_visitor_profile_update_success(self):
        tester = app.test_client(self)
        response = tester.post(
            '/update/profile', data=dict(name="something 6", address="newplace 8", number="01234444445", email="asd@sd.co"), follow_redirects=True)
        self.assertIn(b'Profile Updated!', response.data)

    # logout from the web-app successfully
    def test_logout_from_account_page(self):
        tester = app.test_client(self)
        response = tester.get(
            '/logout', content_type="html/text", follow_redirects=True)
        self.assertIn(b'Login Page', response.data)


if __name__ == '__main__':
    unittest.main()
