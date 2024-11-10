from django.test import TestCase, Client
# TestCase sets up and tears down a test environment, ensuring that the database state is consistent before and after each test
# Client is a test client that simulates a web browser

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('') #make Client class send a get request to the root url
        self.assertEqual(response.status_code, 200) # assert that the HTTP status code returned is 200, aka page loaded successfully

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html') # assert that the template used is main.html

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404) # assert that the page was not found 

