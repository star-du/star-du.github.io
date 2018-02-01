---
layout: post
teaser:
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
The [sample][ex] we use is a 'Atom feed', and the _root_ element is required to be _feed_ element. 




[xml]:../sourcefile/file-icon-xml.png
[wiki]:https://en.wikipedia.org/wiki/XML
[ex]:../sourcefile/examples.xml
