# Tkinter and Python -> Music Player App 

## Key Features 
* Volume Slider
* Song Slider 
* Add/Remove Music (.wav only) 

## Table of contents
* [General info](#general-info)
* [Built with](#built-with)
* [Tools](#tools)
* [Setup](#setup)
* [Note](#note)

## General info
This project is simple desktop music app made with python and tkinter. 
	
## Built with
Project is created with:
* Python3
* Tkinter
	
## Tools
The tools used within this project:
* IDLE 
* Text Editor (Vim, Brackets, Gedit, Atom, Sublime Text, VS Code - any of them would do fine work)

## Setup
To set up the project in Linux (Debian based distribution):
```
----- Installing Python3+ (or latest vesrion of Python) -----
$ sudo apt install python3  || $ sudo apt install python
$ python3 -V || python -V

----- Installing Python Package Installer (PIP) -----

$ sudo apt-get install python-pip 	[On Python2]
$ sudo apt-get install python3-pip 	[On Python3]

----- Installing Virtual Environmrnt -----
$ sudo apt-get install python-venv 	[On Python2]
$ sudo apt-get install python3-venv 	[On Python3]

----- Using Virtual Environment -----
$ python -m venv virt 			[On Python2]
$ python3 -m venv virt 			[On Python3]

----- Activating Virtual Environment -----
( The activate script is located at /virt/bin/)
$ source virt/bin/activate
# This will display something like this: 
(virt) id10t@git$h3ll: ~/BoilerPlate/$
# Deactivating virtual environment 
(virt) id1it@git$h3ll: ~/BoilerPlate/$ deactivate 

----- Installing Tkinter -----
$ sudo apt-get install python-tk	[On Python2]
$ sudo apt-get install python3-tk 	[On Python3]

----- Installing IDLE -----
$ sudo apt install idle                [On Python2]
$ sudo apt-get install idle3           [On Python3]

----- Installing PyGame -----

$ sudo apt-get install python-pygame
and then start the python2 interpreter	[On Python2]
$ python2
and then try to import pygame as
$ import pygame
To set python2 as your default interpreter, you can set an alias in your bash_aliases file. To do this, open a terminal and type:
$ nano ~/.bash_aliases
This may open an empty file, depending upon whether you have set an alias before and then type
alias python='python2'	

$ sudo apt-get build-dep python-pygame [On Python3]
pip install pygame	

----- Installing Mutagen -----
$ pip install mutagen			[On Python2]
$ pip3 install mutagen 			[On Python3]

``` 

## Note
>You must install virtual environment on project's directory 

## Overview
![song](https://user-images.githubusercontent.com/48232101/106730200-6b560a00-6636-11eb-8894-482e7c13b682.gif)

# LICENSE 
>You can check out the full license [here](https://github.com/pkgnpdeb/python-music/blob/main/LICENSE)

This project is licensed under the terms of the **GNU/GPL** license.  
