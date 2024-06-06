<h1>introduction</h1>
simple memo application
![login](https://github.com/Yujunmo/my_memo-using-fastAPI-/assets/45279586/d91e8020-dc3f-46fa-a45e-fa60fcb19b76)
![memo](https://github.com/Yujunmo/my_memo-using-fastAPI-/assets/45279586/629d34ca-4973-4ad9-a6a5-f257a55f9c39)




<h1>[ develop environment ]</h1>

<h3>backend</h3> 
 ㄴ language : python==3.10.12<br>
 ㄴ framework : fastAPI==0.104.1, uvicorn==0.27.0.=post1<br>
	
<h3>front</h3> 
 ㄴ template : Jinja2==3.1.3

<h3>database</h3>
 ㄴ mysql==8.0.36

<h3>os</h3>
 ㄴ independent ( linux / window / mac ...etc ) 

<h3>neccessary python libraries</h3>
 refer to [ requirements ] file <br>
 ㄴ requirements file lists all the depending libraries<br>
 ㄴ command for installing all the libraries at once :  pip install -r requirements   <br>

<h3>how to execute this app</h3>
   download all the folders under [ project ] folder<br>
   directory tree will be like this ...<br>
        project<br>
								   <ul>
							    <li> api [d]</li>
           <li> database [d]</li>
           <li> common_function [d]</li>
           <li> schema [d]</li>
           <li> templates [d]</li>
           <li> main.py [f]</li>												
											</ul>
       
change directory to [ project ] and execute following command<br>
  ㄴ uvicorn main:app --reload<br>

applicaiton will be connected to 8000 port of your server<br>
