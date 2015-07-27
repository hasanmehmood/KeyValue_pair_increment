#Key Value Incremental App

###Introduction
Its a very basic app to store your key value pair, and the main feature of this app is that each time when you try to GET the value of your key, It will be incremented value each time.

For Example if you store a initial value of 1000 with a key "my_counter". Now call GET API for for a value of your Key, You'll get 1001, call it again and you'll get 1002 and so on.

You can also Update or Delete your key value pair.


###API Documentation
You can use curl command to test all these operations.

####Create a Key Value pair
	curl http://localhost:5000/api/v1/keyvalue -d "key=KEY_NAME&value=INITIAL_VALUE" -X POST -v

####GET a value of a Key
	curl http://localhost:5000/api/v1/keyvalue/YOUR_KEY

####Updating a value of a Key
	curl http://localhost:5000/api/v1/keyvalue/YOUR_KEY -X DELETE

####Deleting a key value pair
	curl http://localhost:5000/api/v1/keyvalue/YOUR_KEY -d "value=YOUR_NEW_VALUE" -X PUT