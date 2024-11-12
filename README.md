This webapp uses an NGINX server as a reverse proxy and load balancer.
The web server used for this application is deployed using uWSGI.
And there are 3 of them actively in use (i.e 3 uWSGI server)
While the traffic to each as stated ealier is handled by the intermidiary server NGINX, deployed from the official NGINX image on docker hub.
The uWSGI server was configured to listen on port 8080, while nginx listens on port 80.
This web application was written in python developed by using Flask.
