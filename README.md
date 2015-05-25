About
=====

HTTPLang is a scripting language that makes writing HTTP request routines simpler.

Why?
====

Here's the thing, I've always HATED working with HTTP cookies and requests and what not in Python with urllib, urllib2, or requests. Needless to say it isn't fun, and I get lazy when it comes to certan things. HTTPLang is hopefully the solution to that problem. It takes out all of the complicated stuff and just let's me do what I need to do when simulating a browser, and I hope it will do the same for you. HTTPLang allows you to make GET requests, make POST requests, and handle sessions with ease. It is made to be simplistic.

Documentation
=============

Important Note
--------------

HTTPLang is very strict about things like spaces. Make sure that your code matches the spacing and what not exactly as shown in the examples. If not there will be errors.

Examples
--------

```

set URL http://google.com
do GET /
show $HTML

``` 

```

set URL http://somesite.com
set POSTDATA username=myUsername,password=myPassword is this
do POST /login
set COOKIE $TMPCOOKIE
do GET /usercp

```


Commands
--------

#### set

Gives the ability to set the variables available in the language.

- URL
- POSTDATA
- COOKIE
- USERAGENT
- HTML \*
- TMPCOOKIE \*

(\* for the varables that are altered after each `do`)


`POSTDATA` is special here, when setting the POSTDATA you must use this format ```fieldname=value,fieldtwo=value2 is multiple words``` The spacing much match exactly as shown. For example, ```fieldname = value, field2 = value2``` would not work due to the spacing.

#### do

Gives the ability to make requests.

- GET
- POST

A URL must be set for both requests or an error will be raised. For POST request the POSTDATA variable must be set or an error will be raised.

#### $

The $ gives the ability to call the varaibles. They have limited use and can only be used after a `show` after a `set` and a `set POSTDATA` when setting the value of a field.

#### show

Gives the ability to print the variables.  

