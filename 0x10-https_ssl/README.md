# 0x10. HTTPS SSL

## Resources

[HTTP vs. HTTPS](https://www.instantssl.com/http-vs-https) </br >
[Why SSL? The Purpose of using SSL Certificates](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html) </br >
[Load Balancing HTTPS with Let's Encrypt and HAProxy](https://fly.io/articles/load-balancing-https-with-lets-encrypt/) </br >
[TLS termination proxy Wiki](https://en.wikipedia.org/wiki/TLS_termination_proxy) </br >
[Advanced Bash-Scripting Guide](http://tldp.org/LDP/abs/html/complexfunct.html) </br >

man or help: </br >
- `awk`
- `dig`

## Tasks

0. 0-https_abc // File contains answers to the following questions:

- What is HTTPS? 1. A secure version of HTTP

- Why do you need HTTPS? 2. To encrypt all communication between the client and the website servers

- You want to setup HTTPS on your website, where shall you place the certificate?  3. On your website web server(s)

1. 1-world_wide_web // Configures my domain zone so that the subdomain www points to my load-balancer IP (lb-01). Add other subdomains to make my life easier. Contains a Bash script that will display information about subdomains.

2. 2-haproxy_ssl_termination // The file 2-haproxy_ssl_termination is my HAproxy configuration file
