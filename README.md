About
=====

HTTPLang is a scripting language that makes writing HTTP request routines simpler.

Why?
====

Here's the thing, I don't like using urllib or requests to make HTTP requests, and curl gets messy. I find the process to be stupidly complicated, and handling cookies is a nightmare. I have had enough, and so I have decided to start this project. HTTPLang will hopefully be some kind of solution to the problem of simulating a browser programatically. HTTPLang allows you to make POST and GET requests easily. It makes handling cookies and sessions a breeze, and making POST requests simple. It's a scripting language dedicated 100% to writing HTTP request routines that could be called from another program. My end goal here is to have HTTPLang be a little helper to a larger program that is trying to do some HTTP request stuff. So if I am trying to write a script that logs into a website and changes a field or something. Instead of trying to figure out some complicated library that doesn't really do what you want anyway, just write a quick HTTPLang script that does it in less lines of code. 

Whether it is helpful to other people or not I don't know, but I know I could use something like this.

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

