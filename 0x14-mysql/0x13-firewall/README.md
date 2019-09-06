# 0x13. Firewall

## Resources
[Firewall wiki](https://en.wikipedia.org/wiki/Firewall_%28computing%29)</br >

## Tasks

0-firewall_ABC // Q&A!

- Q: What is a firewall?  A: A hardware or software security system
- Q: What are the two types of firewall?  A: Network and host-based firewall
- Q: What is the main function of a firewall?  A: To filter incoming and outgoing network traffic

1-block_all_incoming_traffic_but // install the `ufw` firewall and setup a few rules on `web-01`.

Requirements:

The requirements below must be applied to `web-01` (feel free to do it on `lb-01` and `web-02`, but it won’t be checked)
Configure `ufw` so that it blocks all incoming traffic, except the following TCP ports:
- `22` (SSH)
- `443` (HTTPS SSL)
- `80` (HTTP)
- Share the `ufw` commands that you used in your answer file