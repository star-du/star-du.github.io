---
layout: post
teaser: Using pickle and json to save your progress. (You don't wanna quit your game and lose your progress ever since!)
title: Dive into python 3 chapter 13
category: coding
tags: [python, note-taking]
---
`pickle` and `json` are both data structures that capture “your
progress so far” needs to be stored on disk when you quit, then loaded from disk when you relaunch.

`pickle` can store All the native datatypes and Lists, tuples, dictionaries, and sets containing them. But pickle is python-specific, while json is "explicitly designed to be usable across multiple programming languages". (BTW, the full name of JSON is _JavaScript Object Notation_). In contrast, json can not serialize tuple [^1] and _bytes_, that's because JSON data format is text-based, such difference will be further explored when we try to store and read from pickle and json files.

### dump and load of each
`dump` is a frequently-used function for storing things, for example, if we get such a dictionary named `entry`:
~~~python
>>>entry
{'title': "A lesson about 'pickle' module",
  'article_link': None,
  'internal_id': b'\xde\xd5\xb4\xf8',
  'tags': ('diveintopython', 'docbook', 'module'),
  'published': True,
  'published_date': time.struct_time(tm_year=2018, tm_mon=2, tm_mday=2, tm_hour=14, tm_min=11, tm_sec=20, tm_wday=4, tm_yday=33, tm_isdst=-1)}
~~~  
we can dump the entry dictionary into a pickle file
~~~python
>>> import pickle
>>> with open('entry.pickle', 'wb') as f:
... pickle.dump(entry, f)
~~~  
The module serializes the data structure using a data format called “the pickle protocol” and the latest pickle protocol is a binary format, so we use `wb`.
~~~python
>>> with open('entry.pickle', 'rb') as f:
... entry = pickle.load(f)
~~~  
...and we can easily load it using the same fashion.

The pickle.dump() / pickle.load() cycle results in a new data structure that is equal to the original data structure. However, when you test it with `is`, it is still two different object.

we can also serialize to a bytes object in memory:
~~~python
>>> b = pickle.dumps(entry)
>>> type(b)
<class 'bytes'>
>>> entry3 = pickle.loads(b)
>>> entry3 == entry
True
~~~
For pickle has different versions of protocols, you can find out the versions with `pickletools.dis()` function in pickle module.

Nearly same stories for json module
~~~python
>>> import json
>>> with open('basic.json', mode='w', encoding='utf-8') as f:
... json.dump(basic_entry, f)
~~~
just to notice that JSON is text-based, so you have to specify a character encoding.

When you 'cat' the json file, it looks neat, and you can makes it even better by giving a `indent` parameter when you use the `dump()` function. Python [documentation][diff] describes that:
>JSON is human-readable, while pickle is not

However, json has some ugly parts ...
### dealing with datatypes unsupported by json #
For JSON cannot encode bytes, when trying to serialize the `entry` object mentioned at the beginning, it raises a `TypeError` exception. As a alternative, we can keep this bytes object using some custom serializer, i.e. convert the object to a JSON-supported
datatype
~~~python
def to_json(python_object):
    if isinstance(python_object, bytes):
        return {'__class__' : 'bytes', '__value__': list(python_object)}
    raise TypeError(repr(python_object) + 'is not JSON serializable')
~~~
we use `list()` function to convert the bytes object into a list of integers

And when dumping, we pass a parameter to `default`, and that parameter is the `to_json` function you defined. It is required that _default should be a function that gets called for objects that can’t otherwise be serialized_.

one of the values in the `entry` dictionary, the 'published_date' is a [time.struct_time][sttime] object returned by a function named strptime() (the function parses a string representing time in a certain format). `time.struct_time` is a class object with a named tuple interface, and cannot be properly serialized either as described by author.

 But it seems that in Python3.6.4, such object is serialized as an array of integers
~~~json
{"title":"A lesson about 'pickle' module",
...
"published_date": [2018, 2, 2, 14, 11, 20, 4, 33, -1]}
~~~
It's kind of a mystery to me.

When we want to load it, we want to get back the original data, so we need another function to take a custom-converted JSON object and convert it back to the original Python datatype.
~~~python
def from_json(json_object):
    if '__class__' in json_object:
        if json_object['__class__'] == 'bytes':
            return bytes(json_object['__value__'])
    return json_object
~~~

To hook the from_json() function into the deserialization process, pass it as the object_hook parameter to the json.load() function.
~~~python
>>> import customserializer
>>> with open('entry.json', 'r', encoding='utf-8') as f:
... entry = json.load(f, object_hook=customserializer.from_json)
~~~
The return value of object_hook will be used instead of the default conversion, so you will have to return the original one if is not a custom-converted object.

Note also that the deserialized one have a _list_ of `tags`, instead of a _tuple_.[^1]

FULL customserializer file [here][src]

**Bonus**: pickel can serialize class as well, [here][picl] is the official guidance.

[^1]: in fact, `json` will convert a tuple to a JSON array, and when we use `load` to deserialize, it will be converted to a list instead of a tuple. see [**manual**][jsload].

[jsload]:https://docs.python.org/3/library/json.html#json.load
[diff]:https://docs.python.org/3/library/pickle.html#comparison-with-json
[sttime]:https://docs.python.org/3/library/time.html#time.struct_time
[picl]:https://docs.python.org/3/library/pickle.html#pickling-class-instances
[src]:https://github.com/star-du/star-du.github.io/blob/master/sourcefile/customserializer.py
