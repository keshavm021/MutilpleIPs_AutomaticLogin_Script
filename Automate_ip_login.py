from autologin import AutoLogin
print("PRESS CTRL-Z to EXIT")
f = open('zmap_output.txt', "r")
lines = f.readlines()
num_lines = sum(1 for line in open('zmap_output.txt'))
#Zmap_output.txt contains list of scanned IPs of Specified Range
f.close()
for i in range(0,num_lines):
 Ip_s = lines[i]
 url ="http://"+Ip_s
 username = 'Enter_Specified_username'
 password = 'Enter_Specified_password'
 al = AutoLogin()
 try:
    cookies = al.auth_cookies_from_url(url, username, password)
    print("Working Url: "+url)
    print(type(cookies))
    with open("output_au.txt",mode='a') as z:
     z.write(str(url)+'\n')
 except:
   print("Try Next Ip: "+url)
   
