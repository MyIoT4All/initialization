#!/usr/bin/python
import urllib.request
from datetime import datetime
import RPi.version
import psutil
import platform
import timea
import distro

#read id from file
with open('/home/pi/systemreport/settings.ini', 'r') as reader:
    pid=reader.readline(12)
    print("Curennt Device:",pid)
print("---Hardware Info ---")
print("memory",RPi.version.memory)
print("Processor",RPi.version.processor)
print("manufactor",RPi.version.manufacturer)
print("model",RPi.version.model)

memory=RPi.version.memory
processor=RPi.version.processor
manufactor=RPi.version.manufacturer
model=RPi.version.model
#processor Info
print("--Processor info--")
uname = platform.uname()
print("System:" ,platform.system())  #Windows or Linux
print("Node Name: ",platform.node()) # System name
print("Release: ",platform.release()) # OS release version like  10(Windows) or 5.4.0-72-generic(linux)
print("Version: ",platform.version())
print("Machine: ",platform.machine())  # machine can be AMD64 or x86-64
print("Processor:",platform.processor()) #  Intel64 Family 6 or x86_64
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))
new_ver = str(platform.version()).replace("#", "" ).replace(" ", "_" )
# CPU frequencies
cpufreq = psutil.cpu_freq()
print("Max Frequency:" ,cpufreq.max,"Mhz")
print("Min Frequency: ",cpufreq.min,"Mhz")
#print("Current Frequency: ",pufreq.current,"Mhz")

print("OS Version")

print("OS:" ,distro.like())
print("Version:" ,distro.version(best=True))

#'?type=HW&devid='+pid+'&memory='+memory+'&processor='+processor+'&manufactor='+manufactor+'&model='+model
#?type=HW&devid=0000&memory=0&processor=0&manufactor=0&model=0&system=0&nodename=0&release=0&version=0&machine=0&cores=0&maxfreq=0&minfreq=0
#htp2='http://data.systemengineers.gr/datalog.aspx'+'?type=HW&devid='+pid+'&memory='+str(memory)+'&processor='+str(processor)+'&manufactor='+manufactor+'&model='+model+"&system="+str(platform.system())+"&nodename="+str(platform.node())+"&release="+str(platform.release())+"&version="+str(platform.version())+"&machine="+str(platform.machine())"&cores="+str(psutil.cpu_count(logical=False))+"&maxfreq="+str(cpufreq.max)+"&minfreq="+str(cpufreq.min)
#htp2="http://data.systemengineers.gr/datalog.aspx"+"?type=HW&devid="+pid+"&memory="+str(memory)+"&processor="+str(processor)+"&manufactor="+manufactor+"&model="+model+"&system="+str(platform.system())+"&nodename="+str(platform.node())+"&release="+str(platform.release())+"&version="+str(new_ver)+"&machine="+str(platform.machine())+"&cores="+str(psutil.cpu_count(logical=True))+"&maxfreq="+str(cpufreq.max)+"&minfreq="+str(cpufreq.min)
htp2="http://data.systemengineers.gr/datalog.aspx"+"?type=HW&devid="+pid+"&memory="+str(memory)+"&processor="+str(processor)+"&manufactor="+manufactor+"&model="+model+"&system="+str(platform.system())+"&nodename="+str(platform.node())+"&release="+str(platform.release())+"&version="+str(new_ver)+"&machine="+str(platform.machine())+"&cores="+str(psutil.cpu_count(logical=True))+"&maxfreq="+str(cpufreq.max)+"&minfreq="+str(cpufreq.min)+"&os="+str(distro.like())+"&osver="+str(distro.version(best=True))
print("Active")
print ("Posting to systemengineers.gr")
print(htp2)
       
# Post Status
#request = urllib.request.Request(htp2)
#response = urllib.request.urlopen(request)
try:
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)   AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(htp2, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    respData =respData.decode('utf-8')
    print(respData)
except Exception as e:
    print(str(e))
        
   



