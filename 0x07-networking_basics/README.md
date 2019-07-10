# 0x07. Networking Basics #0

## Resources
[OSI model](https://searchnetworking.techtarget.com/definition/OSI) </br >
[Different types of network](https://www.lifewire.com/lans-wans-and-other-area-networks-817376) </br >
[LAN network](https://searchnetworking.techtarget.com/definition/local-area-network-LAN) </br >
[WAN network](https://searchnetworking.techtarget.com/definition/WAN-wide-area-network) </br >
[Internet Wiki entry](https://en.wikipedia.org/wiki/Internet) </br >
[MAC address](https://whatismyipaddress.com/mac-address) </br >
[What is an IP address](https://www.bleepingcomputer.com/tutorials/ip-addresses-explained/) </br >
[Private and public address](https://www.iplocation.net/public-vs-private-ip-address) </br >
[IPv4 and IPv6](https://www.webopedia.com/DidYouKnow/Internet/ipv6_ipv4_difference.html) </br >
[Localhost](https://en.wikipedia.org/wiki/Localhost) </br >
[TCP and UDP](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/) </br >
[TCP/UDP ports List](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers) </br >
[What is ping/ICPMP](https://en.wikipedia.org/wiki/Ping_%28networking_utility%29) </br >
[Positional parameters](https://wiki.bash-hackers.org/scripting/posparams) </br >
### For reference:
[TCP/IP ILlustrated]() </br >
### man or help:
- `netstat`
- `ping`

# Learning Objectives
## OSI Model
- What it is
- How many layers it has
- How it is organized
## What is a LAN
- Typical usage
- Typical geographical size
## What is a WAN
- Typical usage
- Typical geographical size
## What is the Internet
- What is an IP address
- What are the 2 types of IP address
- What is localhost
- What is a subnet
- Why IPv6 was created
## TCP/UDP
- What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
- What is the main difference between TCP and UDP
- What is a port
- Memorize SSH, HTTP and HTTPS port numbers
- What tool/protocol is often used to check if a device is connected to a network

## Tasks
0. 0-OSI_model
- Q: What is the OSI model?
- A: The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology.

- Q: How is the OSI model organized?
- A: From the lowest to the highest level.

1. 1-types_of_network
- Q: What type of network are Holberton iMacs connected to?
- A: LAN
- Q: What type of network could connect an office in one building to another office in a building a few streets away?
- A: WAN
- Q: What network do you use when you browse www.holbertonschool.com from your smartphone (not connected to the Wifi)?
- A: Internet

2. 2-MAC_and_IP_address
- Q: What is a MAC address?
- A: Short answer-The unique identifier of a network interface. Long answer-A MAC (Media Access Control) adress is hardwired or hard-coded onto your computer's network interface card (NIC) and is unique to it. The ARP (Address Resolution Protocol) translates an IP address into a MAC address. MAC addresses are useful for network diagnosis because they never change, as opposed to a dynamic IP address, which can change from time to time. For a network administrator, that makes a MAC address a more reliable way to identify senders and receivers of data on the network.

- Q: What is an IP address?
- A: Is to devices connected to a network what postal address is to houses.

3. 3-UDP_and_TCP
- Q1: Correct statement about TCP: It is a protocol that is transferring data, slowly but surely.
- Q2: Correct statement about UDP: It is a protocol that is transferring data in a fast way and might lose data along the process.
- Q3: Correct statement about TCP worker: Have you received boxes x, y, z?

4. 4-TCP_and_UDP_ports // a Bash script that displays listening ports:
- That only shows listening sockets
- That shows the PID and name of the program to which each socket belongs

Introduction: If we continue the comparison of a network device to your house, where an IP address is like your postal address, UDP and TCP ports are like the windows and doors of your place. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free of use.

While the full list of ports should not be memorized, it is important to know the most used ports.
Here are 3 of them:

- 22 for SSH
- 80 for HTTP
- 443 for HTTPS

Note: A socket address is an IP address & port number.
```123.132.213.231         # IP address
               :1234    # port number
123.132.213.231:1234    # socket address```

5. 5-is_the_host_on_the_network // a Bash script that pings an IP address passed as an argument.
- Accepts a string as an argument
- Displays Usage: `5-is_the_host_on_the_network {IP_ADDRESS}` if no argument passed
- Ping the IP 5 times