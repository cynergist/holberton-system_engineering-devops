#0x0F. Load balancer

## Background Context

Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, we will write Bash scripts to automate the work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

## Resources
[What is an HTTP Header?](https://www.techopedia.com/definition/27178/http-header) </br >
[An Introduction to HAProxy and Load Balancing Concepts](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts) </br >
[First 5 Commands When I Connect on a Linux Server](https://www.youtube.com/watch?v=1_gqlbADaAw&feature=youtu.be) </br >
[Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/) </br >

## Tasks
0. Double the number of webservers // 0-custom_http_response-header
- Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
-- The name of the custom HTTP header must be X-Served-By
-- The value of the custom HTTP header must be the hostname of the server Nginx is running on
- Write 0-custom_http_response-header so that it configures a brand new Ubuntu machine to the requirements asked in this task
- Ignore SC2154 for shellcheck

1. Install your load balancer // 1-install_load_balancer
nstall and configure HAproxy on your lb-01 server.

Requirements:

- Configure HAproxy with version equal or greater than 1.5 so that it send traffic to web-01 and web-02
- Distribute requests using a roundrobin algorithm
- Make sure that HAproxy can be managed via an init script
- Make sure that your servers are configured with the right hostnames: [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02. If not, follow this tutorial.
- For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements
