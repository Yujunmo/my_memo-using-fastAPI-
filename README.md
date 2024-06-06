[ develop environment ]

backend 
 ㄴ language : python==3.10.12
 ㄴ framework : fastAPI==0.104.1, uvicorn==0.27.0.=post1
front 
 ㄴ template : Jinja2==3.1.3

database :
 ㄴ mysql==8.0.36

os : independent ( linux / window / mac ...etc ) 

neccessary python libraries : refer to [ requirements ] file 
 ㄴ requirements file lists all the depending libraries
 ㄴ command to install all the libraries at once :  pip install -r requirements   

how to execute this app :
   download all the folders under [ project ] folder
   directory tree will be like this ...
        0.project
           1. api [d]
           1. database [d]
           1. common_function [d]
           1. schema [d]
           1. templates [d]
           1. main.py [f]

change directory to [ project ] and execute following command
  ㄴ uvicorn main:app --reload

applicaiton will be connected to 8000 port of your server
