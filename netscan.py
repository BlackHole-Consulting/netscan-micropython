import socket
import time
import _thread
def ipRange(start_ip, end_ip):
  start = list(map(int, start_ip.split(".")))
  end = list(map(int, end_ip.split(".")))
  temp = start
  ip_range = []

  ip_range.append(start_ip)
  while temp != end:
    start[3] += 1
    for i in (3, 2, 1):
      if temp[i] == 256:
        temp[i] = 0
        temp[i-1] += 1
      ip_range.append(".".join(map(str, temp)))

  return ip_range


# sample usage

def getIpRange(start,end):
    x = []
    ip_range = ipRange(start, end)
    for ip in ip_range:
        x.append(ip)

    return x

scaned = {}

datasock = {}

def sockcon(addr,s2,p):
    #SK[0] = s.connect(addr)
    global datasock
    try:
        if len(datasock[s2])==0:
            datasock[s2]={}
            print(addr)
    except:
        pass
        datasock[s2]={}

    s = socket.socket()
    try:
        s.connect(addr)

        s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % ("/", "localhost"), 'utf8'))
        data = s.recv(800)
        if data:
            print(str(data, 'utf8'), end='')
            datasock[s2][p] = data
    except:
        pass

    s.close()
    _thread.exit()

def portscan(iprange, portlist):
    rang = iprange.split("-")
    for y in getIpRange(rang[0],rang[1]):
        #print(y)
        for x in portlist:
            print(x)
            addr = socket.getaddrinfo(y, x)[0][-1]
            _thread.start_new_thread(sockcon, (addr,y,x) )
            time.sleep(1)
            #if not SK[0]:
            print("data"+str(datasock))

    #return 0


