# MutilpleIPs_AutomaticLogin_Script
Run Following Commands Before Running The script.

`sudo pip3 install autologin`

Description:
It is script which attempt automatic login on multiple Ips from the list of Ips Provided in the text File.
To Run the File:
`python3 Automate_ip_login.py`

If you want to have your List of IPs perform the scanning through Zmap:
`zmap -o output_ip.txt -p 80 10.0.0.0/16 188.12.13.14/16`
You can specify your own range of Ips.
And you need to specify port number also which will be fix for `http port=80`
