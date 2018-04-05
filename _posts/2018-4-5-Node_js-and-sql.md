---
layout: post
teaser: During the development of wechat mini app, Node.js is used and here records some of the experiences
title: Node.js, SQL & others
category: coding
tags: [JavaScript, note-taking]
---
### connect, select and insert
To connect to an SQLite database, you need to:

- First, import the sqlite3 module
- Second, call the Database() function of the sqlite3 module and pass the database information such as database file, opening mode, and a callback function.

e.g.:
~~~JavaScript
const sqlite3 = require('sqlite3').verbose();

// open the database
let db = new sqlite3.Database('./db/chinook.db', sqlite3.OPEN_READWRITE, (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Connected to the chinook database.');
});
...
db.close()
~~~

To insert, use the `run()` method of Database object,
~~~JavaScript
db.run(sql, params, function(err){
  //
});
~~~
The run() method executes an INSERT statement with specified parameters and calls a callback afterwards.

to insert multiple rows, it's possible to use a bit tricks like _map_ the items with placeholders (_'?'_), so that the number can be given. for more see [here][insert].

[insert]:http://www.sqlitetutorial.net/sqlite-nodejs/insert/
