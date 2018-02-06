---
layout: post
teaser: About HTTP
title: Dive into python 3 chapter 14
category: coding
tags: [python, note-taking]
---
<span style = "font-family:Lucida Grande; font-size:36px; color:#4286f4"> HTTP </span> web service is a way of exchanging data with remote servers, and it holds the virture of _simplicity_.

Data, usually in the forms of XML or JSON, is built and stored statically or generated dynamically by a server-side script. And each resource in an HTTP web service has a unique URL, which is greatly convenient.

As is described, HTTP clients should support five features:
- caching: `Cache-Control` `publicExpires` headers
  - brower local cache
  - caching proxy
- last-modified checking: `Last-Modified` header
- ETag checking: `ETag` header (it changes every time the data changes)
- compression: client-side includes `Accept-encoding` head to list the compression data algorithms you support, server side includes `Content-encoding`
- Redirects: status-code header
  - 302: temporary redirect
  - 301: permanenet redirect

the http web service use simple lines like `GET`, `POST`,`PUT` and `DELETE`. The `httplib2` supports features like caching and ETag checking etc., and is recommended by the author. For certain reasons, much of the tutorials haven't been fully followed, so I will take down as much as I'm capable of.

To use the `httplib2`, first you should install it,(I achieve this using _Anaconda_), then create an instance of the httplib2.Http class and pass a directory name so you can store the cache. Then retrieving data using `request()` method which will issue an `HTTP GET` request:
~~~python
import httplib2
h = httplib2.Http('.cache')
response, content = h.request('http://www.diveintopython3.net/examples/feed.xml')
~~~
the `request()` returns two objects, the first is an httplib2.Response object, which contains all the HTTP headers the server returned. The content variable contains the actual data that was returned by the HTTP server, and it is __bytes__ object (NOT STRING!).

And cache works when you attempt to request the data again(and the previous 'cache headers' you receive have request things about local cache), this time, you don't need to reach the remote server, and you get your result nicely.
~~~python
>>>response, content = h.request('http://www.diveintopython3.net/examples/feed.xml')
>>>print(response.fromcache)
True
>>>response2, content2 = h.request('http://www.diveintopython3.net/examples/feed.xml', headers={'cache-control':'no-cache'})
>>>print(response2.fromcache)
False
~~~
In fact, the cache headers have demanded that cache should be stored for a certain period of time, `httplib2`understood and respected it, stored the previous response in the .cache directory. And if you wish to bypass the cache, you should add a `nocache`
header in the headers dictionary.

If it passed the cache expiring date (i.e. the local cache is no longer fresh), `httplib2` send the _validators_ with the next request to see if the data has actually changed. And these _validators_ are `Last-Modified` and `Etag` headers.

when trying to reach some sites,the response contains validators headers like
~~~
'last-modified': 'Wed, 12 Oct 2011 19:46:20 GMT', 'etag': '"37f58e288616124be5daa1748f93d916"'
~~~
and when you request the page again, with the same Http object, `httplib2` sends the ETag validator back to the server in the If-None-Match header, also the Last-Modified validator back to the server in the If-Modified-Since header.
~~~
if-none-match: "37f58e288616124be5daa1748f93d916"
if-modified-since: Wed, 12 Oct 2011 19:46:20 GMT
~~~

The server looked at these validators and sends back a `304` status code and no data. So the client just loads the content of the page from its cache.
