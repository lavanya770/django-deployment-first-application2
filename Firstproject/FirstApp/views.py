from django.shortcuts import render 
from django.http import HttpResponse
#create views heare
def display(request): #view-function
   #ss----->html data/code
    print("welcome/ url is request & display() is excuted");
    ss='''
        <center>
        <h1 style='color:red'>
        ***hello user welcome to django*** 
        </h1>
        <hr/>
        </center>
    ''';
    return HttpResponse(ss);


def show(request):
    ss='''
        <html>
	<head>
		<title>***welcome-message***</title>
		<style>
			h1{
				color:blue;
			}
			h2{
				color:green;
			}
			h3{
				color:red;
			}
			h4{
				color:orange;
			}
			h5{
				color:pink;
			}
			h6{
				color:violate;
			}
			h1,h2,h5{
				background-color:yellow;
			}
			h2,h4,h6{
				background-color:lightgreen;
			}
		
		
		
		</style>
	</head>
	<body>
		<center>
		<h1>welcome to django html webpage</h1>
		<hr color='brown'/>
		<h2>welcome to django html webpage</h2>
		<hr color='brown' width='85'/>
		<h3>welcome to django html webpage</h3>
		<hr color='brown' width='75'/>
		<h4>welcome to django html webpage</h4>
		<hr color='brown' width='65'/>
		<h5>welcome to django html webpage</h5>
		<hr color='brown' width='55'/>
		<h6>welcome to django html webpage</h6>
		<hr color='brown' width='45'/>
		</center>
	</body>
</html>
    
    ''';
    return HttpResponse(ss);

def hello(request):
    print("helo/url is requested & hello is wexcuted")
    ss='''
    <html>
        <head>
        <title>Webpage</title>
            <style>
                h1{
                    color:blue;
                    width:90%;
                }
                h2{
                    color:green;
                    width:80%;
                }   
                h3{
                    color:red;
                    width:70%
                }
                h1,h2,h3{
                    background-color:lightblue;
                    border:2px solid brown;
                }
        
            </style>    
        </head>
        <body>
            <center>
                <h1>Hello user...!!!</h1>
                <hr color='brown' width=80%>
                <h2>Welcome to Django-app</h2>
                <hr color='brown' width=60%>
                <h3>Have a noce day...</h3>
                <hr color='brown' width=40%>
            
            </center>
        
        </body>
    
    </html>    
    '''
    return HttpResponse(ss);
    

import time
def senddatetime(request):
    print("dtime /; url is requested & senddatetime is excuted");
    ct = time.ctime()
    print("clint request data & time on server :: ",ct);
    ss='''
    <html>
        <head>
        <title>Date-time Webpage</title>
            <style>
                h1{
                    color:Blue;
                    width:90%;
                }
                h2{
                    color:Green;
                    width:80%;
                }
                h3{
                    color:Red;
                    width:70%;
                }
                h1,h2,h3{
                    background-color:lightgreen;
                    border:2px Solid Brown;  #we can alo take (dotted),(dashed),(solid)
                }
            </style>
        </head>
        <body>
            <center>
            <h1>Welcome to DJango-User..!!!</h1>
            <hr color='brown' width='80%'/>
            <h2>Server-Date & Time :: </h2>
            <hr color='brown' width='70%'/>
            <h3>''',ct,'''</h3>
            <hr color='brown' width='60%'/>
            </center>
        </body>
    </html>
    ''';
    return HttpResponse(ss);
    
def demo(request): 
    print("mulitple-Requests-URLs same respose");
    htmldata='''<center>
        <h1>Welcome Demo User!!!</h1>
        <hr />
        <h2>This is Same-Output for diff-mulitple-RequestsURLs</h2>
        <hr />
        <h3>Have a Great Day...</h3>
        </center>''';
    return HttpResponse(htmldata);


def homepage(request):
    htmldata='''<center>
        <h1>Welcome to DEFAULT Home-Page!!!</h1>
        <hr />
        <h2>Your Request Page is Not-Found...</h2>
        <hr />
        <h3>Plz try other URL or Links!!!</h3>
        </center>''';
    return HttpResponse(htmldata)