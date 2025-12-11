# Отчёт по лабораторной  работе 3
### Володин Максим

1. Опишем методы из списка
---
#### **1. TCP - connect (`-sT`)**
- **Назначение:** Стандартное TCP-сканирование, которое устанавливает полное соединение по протоколу TCP.
- **Как работает:** Отправляет SYN-пакет, получает SYN-ACK в ответ, затем отправляет ACK для завершения трёхэтапного рукопожатия.
- **Результаты:** Показывает, какие порты открыты и готовы принимать соединения. 
Может быть легко обнаружено системами мониторинга.
---
#### **2. TCP SYN - stealth-сканирование (`-sS`)**
- **Назначение:** Более скрытное сканирование, не завершающее соединение полностью.
- **Как работает:** Отправляет SYN-пакет, получает SYN-ACK, но не отправляет финальный ACK (соединение остаётся полуоткрытым).
- **Результаты:** Определяет открытые порты без установления полноценного соединения. Меньше шансов быть зафиксированным в логах.
---
#### **3. UDP (`-sU`)**
- **Назначение:** Сканирование UDP-портов.
- **Как работает:** Отправляет пустые UDP-пакеты.
Если порт открыт, служба может ответить; если закрыт — ICMP-сообщение «port unreachable».
- **Результаты:** Медленное, но необходимое для обнаружения UDP-сервисов (DNS, DHCP, SNMP и др.).
---
#### **4. FIN (`-sF`)**
- **Назначение:** Использует FIN-пакеты для проверки состояния портов.
- **Как работает:** Отправляет FIN-пакет.
Закрытый порт ответит RST, открытый — проигнорирует.
- **Результаты:** Полезен для обхода unstrict firewalls, которые отслеживают только SYN-пакеты.
---
#### **5. ACK (`-sA`)**
- **Назначение:** Обнаружение firewall rules и их конфигурации.
- **Как работает:** Отправляет ACK-пакеты.
Ответ RST означает, что пакет прошёл; отсутствие ответа — наличие фильтра.
- **Результаты:** Помогает определить, используется ли stateful-фильтрация.
---
#### **6. XMAS tree (`-sX`)**
- **Назначение:** Отправка пакетов с установленными флагами FIN, URG и PSH (как «рождественская ёлка»).
- **Как работает:** Аналогично NULL и FIN сканированиям: закрытые порты отвечают RST, открытые — игнорируют.
- **Результаты:** Может использоваться для определения состояния портов на системах с нестандартным поведением стека TCP/IP.
---
#### **7. NULL-сканирование (`-sN`)**
- **Назначение:** Отправка пакетов без установленных флагов.
- **Как работает:** Отправляет TCP-пакет с пустым заголовком (без флагов).
- **Результаты:** Если порт закрыт, система отвечает RST-пакетом.
Если открыт — игнорирует.
Помогает обойти некоторые фильтры.
---
#### **8. ICMP ping(`-PE`, `-PP`, `-PM`)**
- **Назначение:** Обнаружение активных хостов в сети.
- **Как работает:** Отправляет ICMP Echo, Timestamp или Netmask Request пакеты.
- **Результаты:** Показывает, какие хосты «живые» и отвечают на ping.
---
#### **9. FTP-proxy**
- **Назначение:** Использование FTP-сервера в качестве прокси для сканирования других хостов.
- **Как работает:** Подключается к FTP-серверу и использует команду `PORT` для перенаправления трафика.
- **Результаты:** Маскирует источник сканирования, но требует уязвимого или сконфигурированного FTP-сервера.
---
#### **10. idle scan (`-sI`)**
- **Назначение:** Сканирование от имени другого хоста (зомби), чтобы скрыть источник.
- **Как работает:** Использует побочный канал через незанятый хост, анализируя изменения IP-идентификаторов.
- **Результаты:** Полностью анонимное сканирование, но требует наличия подходящего «зомби»-хоста.
---
#### **11. OS Detection (`-A` или `-O`)**
- **Назначение:** Определение операционной системы целевого хоста.
- **Как работает:** Анализирует отклики TCP/IP-стека, сравнивая их с базой отпечатков ОС.
- **Результаты:** Позволяет предположить тип и версию ОС, что важно для подбора эксплойтов.
---
#### **12. List Scan (`-sL`)**
- **Назначение:** Вывод списка хостов без отправки пакетов.
- **Как работает:** Просто преобразует имена хостов в IP-адреса через DNS.
- **Результаты:** Полезен для предварительного планирования сканирования.
---
#### **13. Ping Scan (`-sn`)**
- **Назначение:** Проверка активности хостов без сканирования портов.
- **Как работает:** Использует ICMP и ARP для определения живых хостов.
- **Результаты:** Быстрое определение активных устройств в сети.
---
#### **14. No Ping (`-Pn`)**
- **Назначение:** Сканирование без предварительной проверки активности.
- **Как работает:** Пропускает этап ping, считая все хосты активными.
- **Результаты:** Эффективно против хостов, блокирующих ICMP-трафик.
---
#### **15. Traceroute (`--traceroute`)**
- **Назначение:** Определение маршрута до целевого хоста.
- **Как работает:** Использует TTL-поля в IP-пакетах для построения пути.
- **Результаты:** Показывает сетевую топологию и промежуточные узлы.
---
2. Анализируем ответы
Сначала localhost
```
PS C:\Users\user\PycharmProjects\lanit_labs> nmap localhost
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 01:12 +0300
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00040s latency).
Other addresses for localhost (not scanned): ::1
Not shown: 997 closed tcp ports (reset)
PORT     STATE SERVICE
135/tcp  open  msrpc
445/tcp  open  microsoft-ds
7070/tcp open  realserver

Nmap done: 1 IP address (1 host up) scanned in 0.60 seconds
```
```
PS C:\Users\user\PycharmProjects\lanit_labs> nmap -sC localhost
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 01:14 +0300
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00014s latency).
Other addresses for localhost (not scanned): ::1
Not shown: 997 closed tcp ports (reset)
PORT     STATE SERVICE
135/tcp  open  msrpc
445/tcp  open  microsoft-ds
7070/tcp open  realserver
| ssl-cert: Subject: commonName=AnyDesk Client
| Not valid before: 2022-05-13T08:04:18
|_Not valid after:  2072-04-30T08:04:18
|_ssl-date: TLS randomness does not represent time

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-12-10T22:14:09
|_  start_date: N/A

Nmap done: 1 IP address (1 host up) scanned in 18.44 seconds
```
Теперь с флагами
```
PS C:\Users\user\PycharmProjects\lanit_labs> nmap -p localhost
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 01:16 +0300
Found no matches for the service mask 'localhost' and your specified protocols
QUITTING!
```
```
PS C:\Users\user\PycharmProjects\lanit_labs> nmap -O localhost
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 01:16 +0300
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00056s latency).
Other addresses for localhost (not scanned): ::1
Not shown: 997 closed tcp ports (reset)
PORT     STATE SERVICE
135/tcp  open  msrpc
445/tcp  open  microsoft-ds
7070/tcp open  realserver
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.98%E=4%D=12/11%OT=135%CT=1%CU=30949%PV=Y%DS=0%DC=L%G=Y%TM=6939F
OS:157%P=i686-pc-windows-windows)SEQ(SP=101%GCD=1%ISR=10D%TI=I%CI=I%II=I%SS
OS:=S%TS=U)SEQ(SP=102%GCD=1%ISR=108%TI=I%CI=I%II=I%SS=S%TS=U)SEQ(SP=105%GCD
OS:=1%ISR=107%TI=I%CI=I%II=I%SS=S%TS=U)SEQ(SP=105%GCD=1%ISR=10B%CI=I%II=I%T
OS:S=U)SEQ(SP=FE%GCD=1%ISR=105%TI=I%CI=I%II=I%SS=S%TS=U)OPS(O1=MFFD7NW8NNS%
OS:O2=MFFD7NW8NNS%O3=MFFD7NW8%O4=MFFD7NW8NNS%O5=MFFD7NW8NNS%O6=MFFD7NNS)WIN
OS:(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FFFF)ECN(R=Y%DF=Y%T=40%W=FFF
OS:F%O=MFFD7NW8NNS%CC=N%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=Y%DF
OS:=Y%T=40%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)T3(R=Y%DF=Y%T=40%W=0%S=Z%A=O%F=AR%O=
OS:%RD=0%Q=)T4(R=Y%DF=Y%T=40%W=0%S=A%A=O%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=
OS:0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=O%F=R%O=%RD=0%Q=)T
OS:7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN
OS:=0%RIPL=G%RID=G%RIPCK=Z%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=Z)

Network Distance: 0 hops

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.73 seconds
```
Теперь конкретные порты
```
PS C:\Users\user\PycharmProjects\lanit_labs> nmap -p 80 localhost          
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 01:18 +0300
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00s latency).
Other addresses for localhost (not scanned): ::1

PORT   STATE  SERVICE
80/tcp closed http

Nmap done: 1 IP address (1 host up) scanned in 0.31 seconds
```
```
 PS C:\Users\user\PycharmProjects\lanit_labs> nmap -p 443 localhost
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 01:20 +0300
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00s latency).
Other addresses for localhost (not scanned): ::1

PORT    STATE  SERVICE
443/tcp closed https

Nmap done: 1 IP address (1 host up) scanned in 0.33 seconds
```
```
PS C:\Users\user\PycharmProjects\lanit_labs> nmap -p 8443 localhost
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 01:21 +0300
Nmap scan report for localhost (127.0.0.1)
Host is up (0.0010s latency).
Other addresses for localhost (not scanned): ::1

PORT     STATE  SERVICE
8443/tcp closed https-alt

Nmap done: 1 IP address (1 host up) scanned in 0.32 seconds
```
```
PS C:\Users\user\PycharmProjects\lanit_labs> nmap -p "*" localhost
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 01:22 +0300
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00081s latency).
Other addresses for localhost (not scanned): ::1
Not shown: 8372 closed tcp ports (reset)
PORT      STATE    SERVICE
135/tcp   open     msrpc
137/tcp   filtered netbios-ns
445/tcp   open     microsoft-ds
5040/tcp  open     unknown
5354/tcp  open     mdnsresponder
5939/tcp  open     unknown
7070/tcp  open     realserver
27015/tcp open     unknown

Nmap done: 1 IP address (1 host up) scanned in 2.16 seconds
```
```
PS C:\Users\user\PycharmProjects\lanit_labs> nmap -sV -p 22,8080 localhost
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 01:23 +0300
Nmap scan report for localhost (127.0.0.1)
Host is up (0.0071s latency).
Other addresses for localhost (not scanned): ::1

PORT     STATE  SERVICE    VERSION
22/tcp   closed ssh
8080/tcp closed http-proxy

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1.01 seconds
```
Переходим к IP-адресам
```
PS C:\Users\user\PycharmProjects\lanit_labs> nmap -sP 192.168.1.0/24
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 01:24 +0300
Nmap done: 256 IP addresses (0 hosts up) scanned in 209.05 seconds
```
```
PS C:\Users\user\PycharmProjects\lanit_labs> nmap --open 192.168.1.1
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 01:29 +0300
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.35 seconds
```
```
PS C:\Users\user\PycharmProjects\lanit_labs> nmap --packet-trace 192.168.1.1
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 01:30 +0300
SENT (0.3080s) ICMP [192.168.0.104 > 192.168.1.1 Echo request (type=8/code=0) id=10157 seq=0] IP [ttl=59 id=56469 iplen=28 ]
SENT (0.3090s) TCP 192.168.0.104:58383 > 192.168.1.1:443 S ttl=43 id=33468 iplen=44  seq=1100222894 win=1024 <mss 1460>
SENT (0.3100s) TCP 192.168.0.104:58383 > 192.168.1.1:80 A ttl=55 id=18235 iplen=40  seq=0 win=1024 
SENT (0.3110s) ICMP [192.168.0.104 > 192.168.1.1 Timestamp request (type=13/code=0) id=23443 seq=0 orig=0 recv=0 trans=0] IP [ttl=38 id=3442 iplen=40 ]
SENT (2.3400s) ICMP [192.168.0.104 > 192.168.1.1 Timestamp request (type=13/code=0) id=45948 seq=0 orig=0 recv=0 trans=0] IP [ttl=49 id=40882 iplen=40 ]
SENT (2.3400s) TCP 192.168.0.104:58385 > 192.168.1.1:80 A ttl=48 id=59365 iplen=40  seq=0 win=1024 
SENT (2.3410s) TCP 192.168.0.104:58385 > 192.168.1.1:443 S ttl=51 id=62804 iplen=44  seq=1100353964 win=1024 <mss 1460>
SENT (2.3420s) ICMP [192.168.0.104 > 192.168.1.1 Echo request (type=8/code=0) id=14351 seq=0] IP [ttl=58 id=61728 iplen=28 ]
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.36 seconds
```
```
PS C:\Users\user\PycharmProjects\lanit_labs> nmap --packet-trace scanme.nmap.org 
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 01:31 +0300
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.17s latency).
Not shown: 995 closed tcp ports (reset)
PORT      STATE SERVICE
22/tcp    open  ssh
53/tcp    open  domain
80/tcp    open  http
9929/tcp  open  nping-echo
31337/tcp open  Elite

Nmap done: 1 IP address (1 host up) scanned in 5.48 seconds
```
nmap --iflist вывел таблицу портов, устройств и IP-адресов

Теперь сканируем цели из файла
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab3> nmap -iL exmp_targets.txt                        
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 01:42 +0300
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.20s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
Not shown: 994 closed tcp ports (reset)
PORT      STATE    SERVICE
22/tcp    open     ssh
23/tcp    filtered telnet
80/tcp    open     http
179/tcp   filtered bgp
9929/tcp  open     nping-echo
31337/tcp open     Elite

Nmap scan report for localhost (127.0.0.1)
Host is up (0.00048s latency).
Other addresses for localhost (not scanned): ::1
Not shown: 996 closed tcp ports (reset)
PORT     STATE    SERVICE
53/tcp   filtered domain
135/tcp  open     msrpc
445/tcp  open     microsoft-ds
7070/tcp open     realserver

Nmap done: 515 IP addresses (2 hosts up) scanned in 126.61 seconds
```
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab3> nmap -A -iL exmp_targets.txt
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 17:22 +0300
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.30s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
Not shown: 995 closed tcp ports (reset)
PORT      STATE SERVICE    VERSION
22/tcp    open  ssh        OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 ac:00:a0:1a:82:ff:cc:55:99:dc:67:2b:34:97:6b:75 (DSA)
|   2048 20:3d:2d:44:62:2a:b0:5a:9d:b5:b3:05:14:c2:a6:b2 (RSA)
|   256 96:02:bb:5e:57:54:1c:4e:45:2f:56:4c:4a:24:b2:57 (ECDSA)
|_  256 33:fa:91:0f:e0:e1:7b:1f:6d:05:a2:b0:f1:54:41:56 (ED25519)
53/tcp    open  domain     ISC BIND 9.10.3-P4 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.10.3-P4-Ubuntu
80/tcp    open  http       Apache httpd 2.4.7 ((Ubuntu))
|_http-title: Go ahead and ScanMe!
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-favicon: Nmap Project
9929/tcp  open  nping-echo Nping echo
31337/tcp open  tcpwrapped
Aggressive OS guesses: Linux 5.0 - 5.14 (98%), MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3) (97%), Linux 4.15 - 5.19 (94%), OpenWrt 21.02 (Linux 5.4) (94%), Linux 2.6.32 - 3.13 (93%), Linux 5.1 - 5.15 (93%), Linux 6.0 (93%), Linux 2.6.39 (93%), OpenWrt 22.03 (Linux 5.10) (93%), Linux 2.6.22 - 2.6.36 (91%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 17 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 8888/tcp)
HOP RTT       ADDRESS
1   1.00 ms   192.168.0.1
2   6.00 ms   6-ka-core.mipt.ru (93.175.6.1)
3   3.00 ms   campus-isg.asr.telecom.mipt.ru (81.5.90.1)
4   3.00 ms   p2p.telecom.mipt.ru (81.5.81.60)
5   6.00 ms   100.105.99.241
6   ...
7   28.00 ms  e0-34.switch2.sto2.he.net (184.104.227.233)
8   ...
9   113.00 ms port-channel4.core2.ewr5.he.net (184.104.189.25)
10  ...
11  170.00 ms port-channel9.core3.sjc2.he.net (184.104.199.21)
12  ...
13  228.00 ms eqix-sv1.linode.com (206.223.116.196)
14  228.00 ms 10.203.32.3
15  227.00 ms 10.203.35.71
16  197.00 ms 10.203.7.43
17  290.00 ms scanme.nmap.org (45.33.32.156)

Nmap scan report for localhost (127.0.0.1)
Host is up (0.00083s latency).
Other addresses for localhost (not scanned): ::1
Not shown: 997 closed tcp ports (reset)
PORT     STATE SERVICE         VERSION
135/tcp  open  msrpc           Microsoft Windows RPC
445/tcp  open  microsoft-ds?
7070/tcp open  ssl/realserver?
| ssl-cert: Subject: commonName=AnyDesk Client
| Not valid before: 2022-05-13T08:04:18
|_Not valid after:  2072-04-30T08:04:18
|_ssl-date: TLS randomness does not represent time
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.98%E=4%D=12/11%OT=135%CT=1%CU=40960%PV=Y%DS=0%DC=L%G=Y%TM=693AD
OS:46A%P=i686-pc-windows-windows)SEQ(SP=101%GCD=1%ISR=10B%TI=I%CI=I%II=I%SS
OS:=S%TS=U)SEQ(SP=102%GCD=1%ISR=107%TI=I%CI=I%II=I%SS=S%TS=U)SEQ(SP=103%GCD
OS:=1%ISR=109%TI=I%CI=I%II=I%SS=S%TS=U)SEQ(SP=103%GCD=1%ISR=10C%TI=I%CI=I%I
OS:I=I%SS=S%TS=U)SEQ(SP=104%GCD=1%ISR=109%TI=I%CI=I%II=I%SS=S%TS=U)OPS(O1=M
OS:FFD7NW8NNS%O2=MFFD7NW8NNS%O3=MFFD7NW8%O4=MFFD7NW8NNS%O5=MFFD7NW8NNS%O6=M
OS:FFD7NNS)WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FFFF)ECN(R=Y%DF=Y
OS:%T=40%W=FFFF%O=MFFD7NW8NNS%CC=N%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q
OS:=)T2(R=Y%DF=Y%T=40%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)T3(R=Y%DF=Y%T=40%W=0%S=Z%
OS:A=O%F=AR%O=%RD=0%Q=)T4(R=Y%DF=Y%T=40%W=0%S=A%A=O%F=R%O=%RD=0%Q=)T5(R=Y%D
OS:F=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=O%F=R%O
OS:=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40
OS:%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=Z%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=Z)

Network Distance: 0 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-12-11T14:25:34
|_  start_date: N/A

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 515 IP addresses (2 hosts up) scanned in 189.69 seconds
```
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab3> nmap -sA scanme.nmap.org
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 17:36 +0300
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.17s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
All 1000 scanned ports on scanme.nmap.org (45.33.32.156) are in ignored states.
Not shown: 1000 unfiltered tcp ports (reset)

Nmap done: 1 IP address (1 host up) scanned in 3.40 seconds
```
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab3> nmap -PN scanme.nmap.org 
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 17:36 +0300
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.17s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
Not shown: 995 closed tcp ports (reset)
PORT      STATE SERVICE
22/tcp    open  ssh
53/tcp    open  domain
80/tcp    open  http
9929/tcp  open  nping-echo
31337/tcp open  Elite

Nmap done: 1 IP address (1 host up) scanned in 2.93 seconds
```
Далее используем сценарии
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab3> nmap --script=vuln 192.168.0.104 -vv
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 17:39 +0300
NSE: Loaded 105 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 17:39
Completed NSE at 17:39, 7.05s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 17:39
Completed NSE at 17:39, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 17:39
Completed Parallel DNS resolution of 1 host. at 17:39, 0.51s elapsed
Initiating SYN Stealth Scan at 17:39
Scanning 192.168.0.104 [1000 ports]
Discovered open port 445/tcp on 192.168.0.104
Discovered open port 139/tcp on 192.168.0.104
Discovered open port 135/tcp on 192.168.0.104
Discovered open port 7070/tcp on 192.168.0.104
Completed SYN Stealth Scan at 17:39, 0.23s elapsed (1000 total ports)
NSE: Script scanning 192.168.0.104.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 17:39
Completed NSE at 17:39, 18.39s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 17:39
Completed NSE at 17:39, 0.00s elapsed
Nmap scan report for 192.168.0.104
Host is up, received localhost-response (0.0011s latency).
Scanned at 2025-12-11 17:39:26 RTZ 2 (чшьр) for 19s
Not shown: 996 closed tcp ports (reset)
PORT     STATE SERVICE      REASON
135/tcp  open  msrpc        syn-ack ttl 64
139/tcp  open  netbios-ssn  syn-ack ttl 64
445/tcp  open  microsoft-ds syn-ack ttl 64
7070/tcp open  realserver   syn-ack ttl 64

Host script results:
|_samba-vuln-cve-2012-1182: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
|_smb-vuln-ms10-054: false

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 17:39
Completed NSE at 17:39, 0.00s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 17:39
Completed NSE at 17:39, 0.00s elapsed
Read data files from: C:\Program Files (x86)\Nmap
Nmap done: 1 IP address (1 host up) scanned in 26.70 seconds
           Raw packets sent: 1000 (44.000KB) | Rcvd: 2004 (84.176KB)
```
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab3> nmap -sV --script vuln -oN nmapres_new.txt localhost
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 17:40 +0300
Nmap scan report for localhost (127.0.0.1)
Host is up (0.0011s latency).
Other addresses for localhost (not scanned): ::1
Not shown: 997 closed tcp ports (reset)
PORT     STATE SERVICE         VERSION
135/tcp  open  msrpc           Microsoft Windows RPC
445/tcp  open  microsoft-ds?
7070/tcp open  ssl/realserver?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb-vuln-ms10-054: false
|_samba-vuln-cve-2012-1182: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 37.34 seconds
```

Весь этот вывод был также продублирован в файл.
После выполнения cat > ./nmapres_new.txt файл был очищен
А команда Select-String -Pattern "VULNERABLE" -Path nmapres_new.txt выполнилась без ответа

Далее командой создали папку и записали в файл отчёт по сканированию
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab3> nmap -sV -p 8080 --script vuln -oN $HOME/project/reports/nmapres_new.txt -oX $HOME/project/reports/nmapres_new.xml localhost     
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 18:03 +0300
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00s latency).
Other addresses for localhost (not scanned): ::1

PORT     STATE  SERVICE    VERSION
8080/tcp closed http-proxy

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.42 seconds
```
Выполнение xsltproc nmapres_new.xml -o nmapres_new.html произошло без ответа
3. Выводим все вложенные файлы по директориям
```
 PS C:\Users\user\PycharmProjects\lanit_labs\lab3> tree /F
Структура папок
Серийный номер тома: 56F7-E6DC
C:.
│   exmp_targets.txt
│   nmapres_new.txt
│   README.md
│   report.md
│   
└───project
    └───reports
        │   nmapres_new.html
        │   nmapres_new.txt
        │   nmapres_new.xml
        │   
        └───styles
                nmap.xsl
                
```
4. IP у сетевой карты `Ethernet` нет, поэтому беру обычный IPv4-адрес
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab3> nmap -sP 192.168.0.104
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 18:23 +0300
Nmap scan report for 192.168.0.104
Host is up.
Nmap done: 1 IP address (1 host up) scanned in 0.71 seconds
```
5. Используем nmap и анализируем
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab3> nmap -O localhost  # Для ОС
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 18:25 +0300
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00068s latency).
Other addresses for localhost (not scanned): ::1
Not shown: 997 closed tcp ports (reset)
PORT     STATE SERVICE
135/tcp  open  msrpc
445/tcp  open  microsoft-ds
7070/tcp open  realserver
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.98%E=4%D=12/11%OT=135%CT=1%CU=39031%PV=Y%DS=0%DC=L%G=Y%TM=693AE
OS:259%P=i686-pc-windows-windows)SEQ(SP=100%GCD=1%ISR=106%TI=I%CI=I%II=I%SS
OS:=S%TS=U)SEQ(SP=100%GCD=1%ISR=107%TI=I%CI=I%II=I%SS=S%TS=U)SEQ(SP=100%GCD
OS:=1%ISR=10C%TI=I%CI=I%II=I%SS=S%TS=U)SEQ(SP=FD%GCD=1%ISR=102%TI=I%CI=I%II
OS:=I%SS=S%TS=U)SEQ(SP=FD%GCD=1%ISR=108%TI=I%CI=I%II=I%SS=S%TS=U)OPS(O1=MFF
OS:D7NW8NNS%O2=MFFD7NW8NNS%O3=MFFD7NW8%O4=MFFD7NW8NNS%O5=MFFD7NW8NNS%O6=MFF
OS:D7NNS)WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FFFF)ECN(R=Y%DF=Y%T
OS:=40%W=FFFF%O=MFFD7NW8NNS%CC=N%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)
OS:T2(R=Y%DF=Y%T=40%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)T3(R=Y%DF=Y%T=40%W=0%S=Z%A=
OS:O%F=AR%O=%RD=0%Q=)T4(R=Y%DF=Y%T=40%W=0%S=A%A=O%F=R%O=%RD=0%Q=)T5(R=Y%DF=
OS:Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=O%F=R%O=%
OS:RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%I
OS:PL=164%UN=0%RIPL=G%RID=G%RIPCK=Z%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=Z)

Network Distance: 0 hops

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.44 seconds
(.venv) PS C:\Users\user\PycharmProjects\lanit_labs\lab3> nmap -sV -p 22 localhost  # Для SSH
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 18:25 +0300
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00s latency).
Other addresses for localhost (not scanned): ::1

PORT   STATE  SERVICE VERSION
22/tcp closed ssh

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 0.56 seconds
(.venv) PS C:\Users\user\PycharmProjects\lanit_labs\lab3> nmap -sV -p 23 localhost
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 18:26 +0300
Nmap scan report for localhost (127.0.0.1)
Host is up (0.0010s latency).
Other addresses for localhost (not scanned): ::1

PORT   STATE  SERVICE VERSION
23/tcp closed telnet

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 0.56 seconds
```
В итоге выясняется, что это Windows (хотя сам nmap это автоматически не понял), ssh и telnet закрыты
6. Выполняем команду Copy-Item -Path nmapres_new.txt -Destination nmapres.txt и результат скопирован