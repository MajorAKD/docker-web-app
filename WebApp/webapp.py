from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def firstpage():
    hostname = socket.gethostname()
    message = "And this server likes to see New users (*_*)" if hostname == "uwsgi-1" else "This server doesn't like to see New users"
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Webapp With Loadbalancer</title>
    </head>
    <body style="color:burlywood">
        <h1 style="color:blue">You are currentlly using the {hostname} server</h1>
        <h1>{message}</h1>
        <p>Use the <strong>next</strong> route to view the next page by adding "/next" </p>
    </body>
    </html>
    """

@app.route("/next")
def secondpage():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Webapp With Loadbalancer</title>
    </head>
    <body>
        <h1 style="align: center">Primary Author: Jose Arturo Fernandez</h1>
        <h2 style="align: center">Secondary Author: Major AKD</h2>
        <h3 style="align: center">For Demostration Purpose Only</h3>
        <h1>Details</h1>
        <ul>
            <li>This webapp uses an NGINX server as a reverse proxy and load balancer.</li>
            <li>The web server used for this application is deployed using uWSGI.</li>
            <li>And there are 3 of them actively in use (i.e 3 uWSGI server)</li> 
            <li>While the traffic to each as stated ealier is handled by the intermidiary server NGINX, deployed from the official NGINX image on docker hub</li>
            <li>This web application was written in python developed by using Flask</li>
        </ul>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()


