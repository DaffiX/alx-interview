
# 0x06. Star Wars API

The Star Wars API (SWAPI) is a public API that provides information about various aspects of the Star Wars universe, like characters, films, starships, and more.

## Resources
Read or watch:


- [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY) 

## More Info

#### Install Node 10

``` bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

#### Install semi-standard

[Documentation:](https://github.com/standard/semistandard)

```bash
$ sudo npm install semistandard --global
```

#### Install ```request``` module and use it
[Docx:](https://github.com/request/request)

```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```



### Task 0: Star Wars Characters

Write a script that prints all characters of a Star Wars movie:

+ The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
+ Display one character name per line in the same order as the “characters” list in the /films/ endpoint
+ You must use the Star wars API
+ You must use the ```request``` module

```bash 
alexa@ubuntu:~/0x06$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
alexa@ubuntu:~/0x06$ 
```