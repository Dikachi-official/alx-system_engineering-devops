Web infrastructure design
====================================================================================

Simple web stack
is a simple web infrastructure design that consist of:

1 server
1 web server (Nginx)
1 application server
1 application files (your code base)
1 database (MySQL)
1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8
Distributed web infrastructure
is a simple Distributed web infrastructure that consist of:

2 servers
1 web server (Nginx)
1 application server
1 load-balancer (HAproxy)
1 set of application files (your code base)
1 database (MySQL)
Secured and monitored web infrastructure
is a simple Secured and monitored web infrastructure that consist of:

2 servers
1 web server (Nginx)
1 application server
1 load-balancer (HAproxy)
1 set of application files (your code base)
1 database (MySQL)
3 firewalls
1 SSL certificate to serve www.foobar.com over HTTPS
3 monitoring clients (data collector for Sumologic or other monitoring services)
====================================================================================

AUTHORS
by: Dikachi-official
