# I made this file to test if my app works correctly. Here I test:

# I use unittest to run tests and get things I need from my main a
import unittest
from main_app import app
from main_app import user_exists

# This prepares my app for testing - it turns on test mode and sets up test user details
class StrokeAppTests(unittest.TestCase):
    def setUp(self):
       app.config['TESTING'] = True
       self.app = app.test_client()
       self.username = "Jacek"    
       self.email = "jacek@jacek.com" 
        
        # If home page opens
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        
        # If login page opens and works
    def test_login_page(self):
        response = self.app.get('/user_login')
        self.assertEqual(response.status_code, 200)
        
        # If register page opens and works
    def test_register_page(self):
        response = self.app.get('/user_register')
        self.assertEqual(response.status_code, 200)
        
        # If app blocks access to patient list when not logged in
    def test_patient_list_redirect_when_not_logged_in(self):
        response = self.app.get('/patients_list')
        self.assertEqual(response.status_code, 302)
        
        # If app can find existing users in database
    def test_registration(self):
        response = self.app.get('/user_register')
        self.assertEqual(response.status_code, 200)  
        
        # If login endpoint responds correctly
    def test_login(self):
        response = self.app.get('/user_login')
        self.assertEqual(response.status_code, 200)  

        # Tests if user registration works
    def test_user_exists(self):
       self.app.post('/user_register', data={
           'name': self.username,
           'email': self.email,
           'password': 'test123'
       })
       self.assertTrue(user_exists(self.username, self.email))

        # If app correctly says when user doesn't exist
    def test_user_not_exists(self):
       self.assertFalse(user_exists('NonExistenUser', 'nonexistent@example.com'))

# This runs all my tests when I run this file directly
if __name__ == '__main__':
    unittest.main()
