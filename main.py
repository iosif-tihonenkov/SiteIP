import gevent
from gevent import socket
hosts = ['www.developerhouse.ru']
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs)
count = 0
for job in jobs:
    print("IP адрес домена " + hosts[count] + ": " + job.value)
    count += 1
