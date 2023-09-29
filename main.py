import socket

hosts = ['developerhouse.ru', 'google.com', 'vk.com']

for host in hosts:
    print("Список всех альтернативных имен и адресов для домена: %s -->" % host, socket.gethostbyname_ex(host))
