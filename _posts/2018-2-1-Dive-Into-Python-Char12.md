---
layout: post
teaser: using python to deal with XML files
title: Dive into python 3 chapter 12
category: coding
tags: [python, note-taking]
---
![xml]{: height="40px" width="40px} is not something we're that familiar with, with our warm helper [Wikipedia][wiki], it appears to me that XML is a set of markup language for data storing and processing. It shares similarity with _html_ to me at first glance, so maybe it's not that scary?...

XML is a generalized way of describing hierarchical structured data. It contains elements that are delimited by _start and end tags_.
here follows a example:
~~~xml
<?xml version='1.0' encoding='utf-8'?>
<feed xmlns='http://www.w3.org/2005/Atom' xml:lang='en'>
  <title>dive into mark</title>
  ...
  <link rel='self' type='application/atom+xml' href='http://diveintomark.org/feed/'/>
  <entry>
    <author>
    <name>Mark</name>
    ...
  </entry>
  ...
</feed>
~~~
note that the `xmlns` is important, it declares that the feed element plus all its child elements are in the http://www.w3.org/2005/Atom namespace.

### parsing and generating with ElementTree API #
The [sample][ex] we use is a 'Atom feed', and the _root_ element is required to be _feed_ element. We can parse the xml with the `ElementTree` library. See **MANUAL** [HERE][man].
~~~python
>>>import xml.etree.ElementTree as etree
>>>tree = etree.parse('sourcefile/examples.xml')
>>>root = tree.getroot()
>>>root
<Element '{http://www.w3.org/2005/Atom}feed' at 0x04934A20>
~~~
The `parse` function serves as the main entry point, it parses the entire document and returns an object which represents the entire file (or _file-like_ object), then we use `getroot()` to get the root element.

As said above, the namespace is http://www.w3.org/2005/Atom, so the element, the combination of its namespace and tag name (local name) writes this way.

As an Element, root has a tag and a dictionary of attributes, it also has children nodes over which we can iterate
~~~python
print(root.tag)
for child in root:
    print(child)
~~~
I believe more useful methods maybe `findall()`,`find()`, `get()` and the relatively new one `iter()`

Note that `findall` only finds elements that are direct children (sorry, not _grandchildren_), but `iter()` iterates recursively over its subtrees:
~~~python
ns = '{http://www.w3.org/2005/Atom}'
for link in root.iter('{}link'.format(ns)):
    print(link.attrib)

for category in root.findall('{}link'.format(ns)):
    print(category.get('href'))

for entry in root.findall('{}entry'.format(ns)):
    print(entry.find('{}title'.format(ns)).text)
~~~
`find` and `findall` gets its child element, while `get` gets the attributes

After consulting the manual, I found that:
>A better way to search the namespaced XML example is to create a dictionary with your own prefixes and use those in the search functions.

So, it turns out in this way[^1]
~~~python
ns = { 'default': 'http://www.w3.org/2005/Atom' }
for entry in root.findall('default:entry',ns):
    print(entry.find('default:title',ns).text)
~~~

When you try to generate new xml file, the ElementTree can also help:
~~~python
>>> import xml.etree.ElementTree as etree
>>> new_feed = etree.Element('{http://www.w3.org/2005/Atom}feed',
... attrib={'{http://www.w3.org/XML/1998/namespace}lang': 'en'})
>>> print(etree.tostring(new_feed))
<ns0:feed xmlns:ns0='http://www.w3.org/2005/Atom' xml:lang='en'/>
~~~
You can also use `SubElement` to create child element of an existing element.

But the built-in library is somewhat insufficient to handle full `XPath` and the it employs “draconian error handling.” as required by specification. The author suggests using `lxml` library to enjoy a fuller support and can use _custom XMl parser_ to make up some of the `wellformedness error`.

[^1]:   it's because the `find` and `findall` function can take an optional namespace function, which maps from namespace prefix to full name

[xml]:../sourcefile/file-icon-xml.png
[wiki]:https://en.wikipedia.org/wiki/XML
[ex]:../sourcefile/examples.xml
[man]:https://docs.python.org/3/library/xml.etree.elementtree.html
