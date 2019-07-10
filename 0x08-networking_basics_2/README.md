# 0x08. Networking basics #1

## Resources
[Localhost wiki](https://en.wikipedia.org/wiki/Localhost) </br >
[0.0.0.0 wiki](https://en.wikipedia.org/wiki/0.0.0.0) </br >
[How to Modify and Manage the Hosts File on Linux](https://www.makeuseof.com/tag/modify-manage-hosts-file-linux/) </br >
[Linux Netcat (nc) command examples](https://www.thegeekstuff.com/2012/04/nc-command-examples/) </br >

### For reference:
[TCP/IP Illustrated](http://pcvr.nl/tcpip/) </br >

### man or help:
- `ifconfig`
- `telnet`
- `nc`
- `cut`

## Learning Objectives
- What is localhost/127.0.0.1
- What is 0.0.0.0
- What is `/etc/hosts`
- How to display your machine’s active network interfaces

## Tasks
0. 0-localhost
- Q: What is `localhost`?
- A: A hostname that means /this computer/.

1. 1-wildcard
- Q: What is `0.0.0.0`?
- A: All IPv4 addresses on the local machine.

2. 2-change_your_home_IP // a Bash script that configures an Ubuntu server with the below requirements.

Requirements:

- `localhost` resolves to `127.0.0.2`
- `facebook.com` resolves to `8.8.8.8`.
- The checker is running on Docker, so make sure to read [this](https://web.archive.org/web/20171117023601/http://blog.jonathanargentiero.com/docker-sed-cannot-rename-etcsedl8ysxl-device-or-resource-busy/)

3. 3-show_attached_IPs // a Bash script that displays all active IPv4 IPs on the machine it’s executed on. 

4. 4-port_listening_on_localhost // a Bash script that listens on port `98` on `localhost`.