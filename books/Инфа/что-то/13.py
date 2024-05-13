import ipaddress

net = ipaddress.ip_network('192.168.32.160/255.255.255.240')
cnt = 0

for i in net:
    if f'{i:b}'.count('1') % 2 == 0:
        cnt += 1
print(cnt)