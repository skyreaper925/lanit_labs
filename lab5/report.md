# Отчёт по лабораторной работе 5
### Володин Максим

1. Устанавливаю docker-desktop для Windows через Chocolatey
2. Анализируем ответы
Сначала настройка и запуск
```
 PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker buildx build -t hellow-appsec-world .           
[+] Building 31.5s (14/14) FINISHED                                                                                                                            docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                           0.1s
 => => transferring dockerfile: 429B                                                                                                                                           0.0s 
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                                                                            3.0s 
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                                  0.0s
 => [internal] load .dockerignore                                                                                                                                              0.1s
 => => transferring context: 2B                                                                                                                                                0.0s 
 => [internal] load build context                                                                                                                                              0.2s 
 => => transferring context: 477B                                                                                                                                              0.1s
 => [builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c                                             12.5s
 => => resolve docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c                                                      0.1s
 => => sha256:3f0cdbca744e7bd0ce0ff6da73b9148829b04309925992954a314ba203f56e99 249B / 249B                                                                                     0.4s
 => => sha256:4d55cfecf3663813d03c369bcd532b89f41cf07b65d95887ef686538370a747c 14.36MB / 14.36MB                                                                               6.4s 
 => => sha256:72cf4c3b83019e176aba979aba419d35f56576bbcfc4f7249a1ab1d4b536730b 1.29MB / 1.29MB                                                                                 1.8s 
 => => sha256:1733a4cd59540b3470ff7a90963bcdea5b543279dd6bdaf022d7883fdad221e5 29.78MB / 29.78MB                                                                               9.3s 
 => => extracting sha256:1733a4cd59540b3470ff7a90963bcdea5b543279dd6bdaf022d7883fdad221e5                                                                                      1.5s 
 => => extracting sha256:72cf4c3b83019e176aba979aba419d35f56576bbcfc4f7249a1ab1d4b536730b                                                                                      0.2s 
 => => extracting sha256:4d55cfecf3663813d03c369bcd532b89f41cf07b65d95887ef686538370a747c                                                                                      1.1s 
 => => extracting sha256:3f0cdbca744e7bd0ce0ff6da73b9148829b04309925992954a314ba203f56e99                                                                                      0.0s 
 => [builder 2/4] WORKDIR /hello                                                                                                                                               0.5s 
 => [builder 3/4] COPY requirements.txt .                                                                                                                                      0.2s 
 => [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt                                                                           7.5s 
 => [stage-1 3/6] COPY --from=builder /wheels /wheels                                                                                                                          0.2s 
 => [stage-1 4/6] COPY requirements.txt .                                                                                                                                      0.3s 
 => [stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt                                                                                          2.6s 
 => [stage-1 6/6] COPY hello.py .                                                                                                                                              0.3s 
 => exporting to image                                                                                                                                                         3.2s 
 => => exporting layers                                                                                                                                                        1.7s 
 => => exporting manifest sha256:6580dc92dd74b9d62594969404ed4bc129d9ea774295e439b2879a9d9ff3dbe6                                                                              0.1s 
 => => exporting config sha256:9206de6cc745c442cd14446523777655cbe50052515fda53d0b7c8fca990da01                                                                                0.2s 
 => => exporting attestation manifest sha256:484f271d9a17a12e7e5847176368b6669ae27d152863167c2556f87d108b88a3                                                                  0.2s 
 => => exporting manifest list sha256:168b5e4773446f5d2a516f47f49af60771a07db16a6822367ff0c1dd42f80d50                                                                         0.1s 
 => => naming to docker.io/library/hellow-appsec-world:latest                                                                                                                  0.0s 
 => => unpacking to docker.io/library/hellow-appsec-world:latest
```
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker run hellow-appsec-world  
hello appsec world
```
Команда docker run --rm -it hellow-appsec-world вывела то же самое
Команда docker save -o hello.tar hello-appsec-world выполнилась без ответа

Команда docker load -i image.tar выполнилась с ошибкой, так как в актуальной версии репо нет такого файла.
На нет и суда нет.
К тому же, про пустое множество известно всё что угодно

3. Проанализируем файл

Он создан для упаковки Python-приложения.
Целью его создания было разделения этапов установки зависимостей и финальной сборки.

Всего описано три стадии сборки.
    
    1. Собираются зависимости (временные файлы, то есть исходный код пакетов и кэш pip остаются внутри стадии)

    2. Устанавливаются зависимости, притом только из локальных wheels, то есть без обращения к интернету

    3. Запускается основной сценарий приложения
Делаем снимок
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