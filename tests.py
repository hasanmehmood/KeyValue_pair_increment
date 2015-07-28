from app import app
from requests import put, get, post, delete
import unittest


class  FlaskTestCase(unittest.TestCase):

	# Ensure that flask has been setup correctly
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/index', content_type='html/text')
		self.assertEqual(response.status_code, 200)


	# Ensure that the new Key Value pair has been created successfully
	def test_post_api(self):

		# Creating a test key value pair
		response = post('http://localhost:5000/api/v1/keyvalue',
			data={'key': 'test_bot', 'value': 101}).json()
		self.assertEqual(response['key'], 'test_bot')

		# deleting test data
		delete('http://localhost:5000/api/v1/keyvalue/test_bot')
		

	# Ensure GET api returns incremented value each time
	def test_get_api(self):
		
		# Creating a test key value pair
		post('http://localhost:5000/api/v1/keyvalue',
			data={'key': 'test_bot', 'value': 101}).json()
		response = get('http://localhost:5000/api/v1/keyvalue/test_bot').json()

		# testing that I have received incremented value
		self.assertEqual(response['value'], 102)

		# deleting test data
		delete('http://localhost:5000/api/v1/keyvalue/test_bot')
	

	# Ensure value is modifying
	def test_put_api(self):
		
		# Creating a key value pair
		post('http://localhost:5000/api/v1/keyvalue',
			data={'key': 'test_bot', 'value': 101}).json()
		response = put('http://localhost:5000/api/v1/keyvalue/test_bot',
			data={ 'value': 100 }).json()

		# testing that if the value has been modified or not
		self.assertEqual(response['value'], 100)

		# deleting test data
		delete('http://localhost:5000/api/v1/keyvalue/test_bot')
		

if __name__ == '__main__':
	unittest.main()
