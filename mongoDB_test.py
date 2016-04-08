Last login: Fri Apr  8 11:18:39 on ttys002
pyenv-virtualenv: activate sandbox
(sandbox) HP-Photosmart:mongo_test deanfitzgerald$ mongoimport --db test --collection restaurants --drop --file primer-dataset.json
connected to: 127.0.0.1
2016-04-08T13:21:42.823-0400 dropping: test.restaurants
2016-04-08T13:21:44.434-0400 check 9 25359
2016-04-08T13:21:44.449-0400 imported 25359 objects
(sandbox) HP-Photosmart:mongo_test deanfitzgerald$ python
Python 3.4.2 (default, Jan 11 2015, 13:44:13)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.56)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from pymongo import MongoClient
>>> client = MongoClient()
>>> db = client.primer
>>> db.dataset
Collection(Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'primer'), 'dataset')
>>> coll = db.dataset
>>> from datetime import datetime
>>> result = db.restaurants.add_one({
...         "address": {
...             "street": "2 Avenue",
...             "zipcode": "10075",
...             "building": "1480",
...             "coord": [-73.9557413, 40.7720266]
...         },
...         "borough": "Manhattan",
...         "cuisine": "Italian",
...         "grades": [
...             {
...                 "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
...                 "grade": "A",
...                 "score": 11
...             },
...             {
...                 "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
...                 "grade": "B",
...                 "score": 17
...             }
...         ],
...         "name": "Vella",
...         "restaurant_id": "41704620"
...     }
... )
Traceback (most recent call last):
  File "<stdin>", line 23, in <module>
  File "/Users/deanfitzgerald/.pyenv/versions/sandbox/lib/python3.4/site-packages/pymongo/collection.py", line 2353, in __call__
    self.__name.split(".")[-1])
TypeError: 'Collection' object is not callable. If you meant to call the 'add_one' method on a 'Collection' object it is failing because no such method exists.
>>> result = db.restaurant.insert_one({
...         "address": {
...             "street": "2 Avenue",
...             "zipcode": "10075",
...             "building": "1480",
...             "coord": [-73.9557413, 40.7720266]
...         },
...         "borough": "Manhattan",
...         "cuisine": "Italian",
...         "grades": [
...             {
...                 "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
...                 "grade": "A",
...                 "score": 11
...             },
...             {
...                 "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
...                 "grade": "B",
...                 "score": 17
...             }
...         ],
...         "name": "Vella",
...         "restaurant_id": "41704620"
...     }
... )
>>> result.inserted_id
ObjectId('5707e9bea7d0e0717c143eb5')
>>> cursor = db.restaurants.find()
>>> for document in cursor:
...   print(document)
...   retunr
...   return
... end
  File "<stdin>", line 5
    end
      ^
SyntaxError: invalid syntax
>>> print(document for _ in cursor)
<generator object <genexpr> at 0x1071c25e8>
>>> cursor = db.restaurants.find({"borough": "Manhattan"})
>>> print(cursor)
<pymongo.cursor.Cursor object at 0x1070c49e8>
>>> print (_ for _ in cursor)
<generator object <genexpr> at 0x1071c24c8>
>>> doc = [_ for _ in cursor]
>>> print (doc)
[]
>>> cursor
<pymongo.cursor.Cursor object at 0x1070c49e8>
>>> type(curso)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'curso' is not defined
>>> type(cursor)
<class 'pymongo.cursor.Cursor'>
>>> cursor.__str__
<method-wrapper '__str__' of Cursor object at 0x1070c49e8>
>>> print(cursor.__str__)
<method-wrapper '__str__' of Cursor object at 0x1070c49e8>
>>> cursor = db.restaurants.find({"address.zipcode": "10075"})
>>> print(document) for document in cursor
  File "<stdin>", line 1
    print(document) for document in cursor
                      ^
SyntaxError: invalid syntax
>>> for doc in cursor:
...    print (document)
...
>>>
