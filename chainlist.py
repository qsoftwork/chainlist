import urllib.request
import os
selected=["socks5"]
proxylist=[]
if os.path.isfile("chainlist.txt"):
    os.remove("chainlist.txt")
print("Downloading...")
for type in selected:
    urllib.request.urlretrieve('https://api.proxyscrape.com/?request=getproxies&proxytype='+str(type)+'&timeout=10000&country=all', str(type)+'proxylist.txt')
    f=open(str(type)+'proxylist.txt',"r+")
    f=f.readlines()
    for line in f:
        proxylist.append(str(line))
save=open("chainlist.txt","a")
for item in proxylist:
    save.write(item)
save.close()
for i in selected:
    if os.path.isfile(str(i)+'proxylist.txt'):
        os.remove(str(i)+'proxylist.txt')
print("Done.")