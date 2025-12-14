# Отчёт по лабораторной работе 6

### Володин Максим

1. Устанавливаю `Docker Engine` для Windows

```
 PS C:\Users\user\PycharmProjects\lanit_labs\lab5> wsl --install -d Ubuntu
Скачивание: Ubuntu
Установка: Ubuntu                                           
Дистрибутив успешно установлен. Его можно запустить с помощью "wsl.exe -d Ubuntu"
Запуск Ubuntu...
Provisioning the new WSL instance Ubuntu
This might take a while...
Create a default Unix user account: user
New password: 
Retype new password: 
No password has been supplied.
New password: 
Retype new password: 
passwd: password updated successfully
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.
```

Обновляем списки пакетов

```
user@RAM:/mnt/c/Users/user/PycharmProjects/lanit_labs/lab5$ sudo apt-get update
[sudo] password for user:
Fetched 39.2 MB in 13s (3032 kB/s)                                                                                                                                                 
Reading package lists... Done
```

Устанавливаем `docker.io`, который содержит `Docker Engine` (демон), клиент и основные компоненты.

Ключ -y автоматически отвечает "yes" на все запросы подтверждения во время установки, что позволяет выполнить
установку без нашего вмешательства

```
user@RAM:/mnt/c/Users/user/PycharmProjects/lanit_labs/lab5$ sudo apt-get install -y docker.io
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base iptables libip4tc2 libip6tc2 libnetfilter-conntrack3 libnfnetlink0 libnftables1 libnftnl11 nftables pigz runc ubuntu-fan
Suggested packages:
  ifupdown aufs-tools btrfs-progs cgroupfs-mount | cgroup-lite debootstrap docker-buildx docker-compose-v2 docker-doc rinse zfs-fuse | zfsutils firewalld
The following NEW packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base docker.io iptables libip4tc2 libip6tc2 libnetfilter-conntrack3 libnfnetlink0 libnftables1 libnftnl11 nftables pigz runc
  ubuntu-fan
0 upgraded, 16 newly installed, 0 to remove and 92 not upgraded.
Need to get 77.0 MB of archives.
After this operation, 293 MB of additional disk space will be used.
```

Команда `sudo usermod -aG docker "$USER"` добавляет текущего пользователя (значение переменной среды `$USER`) в
системную группу `docker`. Команда выполнилась без ответа

Ключи:

- a (append) — добавляет пользователя в группу
- G — указывает имя группы

Команда `sudo systemctl start docker` запустил демон без ответа

После этого перезахожу в консоль и скачиваю официальный образ из публичного реестра

```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5> docker pull docker/docker-bench-security
Using default tag: latest
latest: Pulling from docker/docker-bench-security
164e5e0f48c5: Pull complete 
378ed37ea5ff: Pull complete 
cd784148e348: Pull complete 
48fe0d48816d: Pull complete 
Digest: sha256:ddbdf4f86af4405da4a8a7b7cc62bb63bfeb75e85bf22d2ece70c204d7cfabb8
Status: Downloaded newer image for docker/docker-bench-security:latest
docker.io/docker/docker-bench-security:latest                                                                                                                0.0s 
```

2. Проверяем работу контейнеровоза

```
PS C:\Users\user\PycharmProjects\lanit_labs> wsl docker run hello-world                                                     
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
17eec7bbc9d7: Pull complete 
ea52d2000f90: Download complete 
Digest: sha256:d4aaab6242e0cace87e2ec17a2ed3d779d18fbfd03042ea58f2995626396a274
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.
```

Делаем указанный файл исполняемым командой `wsl chmod +x audit.sh`

3. Разворачиваем основное и уязвимое приложение как отдельные стенды.
   Команды уже были проанализированы, поэтому просто выполняем

```
PS C:\Users\user\PycharmProjects\lanit_labs\lab6> docker compose up -d
time="2025-12-14T17:17:23+03:00" level=warning msg="C:\\Users\\user\\PycharmProjects\\lanit_labs\\lab6\\docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
[+] Running 29/30
 ✔ app Pulled                                                                                                                                                                 34.8s 
 ✔ insecure-db Pulled                                                                                                                                                         64.0s 
 ✔ vulnerable-web Pulled                                                                                                                                                      33.3s 
                                                                                                                                                                                                                                                                                                                                                  
[+] Running 4/4
 ✔ Network lab6_default        Created                                                                                                                                         0.2s 
 ✔ Container insecure-db       Started                                                                                                                                         4.0s 
 ✔ Container vulnerable-app    Started                                                                                                                                         3.1s 
 ✔ Container vulnerable-nginx  Started 
```

```
PS C:\Users\user\PycharmProjects\lanit_labs\lab6> docker-compose -f vulnerable-app.yml up -d  
time="2025-12-14T17:20:41+03:00" level=warning msg="C:\\Users\\user\\PycharmProjects\\lanit_labs\\lab6\\vulnerable-app.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
[+] Running 12/12
 ✔ vulnerable-web Pulled                                                                                                                                                      18.9s 
 ✔ debug-shell Pulled                                                                                                                                                          5.1s 
                                                                                                                                                                              
time="2025-12-14T17:21:01+03:00" level=warning msg="Found orphan containers ([vulnerable-app insecure-db]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up."
[+] Running 4/4
 ✔ Container debug-shell                                                  Started                                                                                              2.7s 
 ✔ Container vulnerable-nginx                                             Recreated                                                                                            1.3s 
 ! debug-shell Published ports are discarded when using host network mode                                                                                                      0.0s 
 ✔ Container vulnerable-web                                               Started
```

4. Устанавливаю виртуальное окружение командой `wsl sudo apt install python3.12-venv`.
   С первого раза неуспешно, поэтому я применил `wsl rm -rf venv` и повторил процесс

Затем я активировал виртуальное окружение командой `wsl source venv/bin/activate`, что выполнилась без ответа

```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker run hello-appsec-world Paul
Hello, Paul!
```

После этого устанавливаю `pip` командой `sudo apt install python3-pip` и пакеты командой
`sudo apt install python3-openpyxl`.
Длиннющие выводы консоли приводить не буду

Теперь запускаю аудит, а после этого деактивирую его.
В процессе было потрачено много времени, потому что работать всё отказывалось: не было dumb-init.
Потом консоль постоянно медленно обновлялась и жаловалась на basename.
В итоге как-то отработало.
И тоже с очень длинными выводами

5. Анализируем уязвимости и определяем их причину из консоли

   | Уязвимость | Причина возникновения                                                                                                               |
               |-----------|-------------------------------------------------------------------------------------------------------------------------------------|
   | Избыточная установка зависимостей | Установка `python3-pip` и Python-библиотек приводит к автоматической установке большого числа дополнительных пакетов и компиляторов |
   | Увеличенная поверхность атаки системы | Наличие большого количества неиспользуемых пакетов и библиотек, расширяющих потенциальные точки эксплуатации                        |
   | Использование устаревших пакетов | Выполнение `apt update` без последующего `apt upgrade`, несмотря на наличие доступных обновлений                                    |
   | Отсутствие контроля версий библиотек | Установка пакетов без фиксации версий, что делает окружение невоспроизводимым                                                  |

6. Опишем влияния уязвимостей, их сценарий атаки.
   Не буду использовать таблицу, так как она получится слишком громоздкой в этом markdown

#### Избыточная установка зависимостей

- Влияние
    - Увеличение размера образа и времени сборки
    - Усложнение аудита безопасности из-за большого числа пакетов
    - Риск наличия уязвимостей в неиспользуемых пакетах
- Сценарий атаки
    - Злоумышленник использует уязвимость в одном из автоматически установленных неиспользуемых пакетов для
      получения доступа к контейнеру или системе

#### Увеличенная поверхность атаки системы

- Влияние
    - Повышенный риск эксплуатации уязвимостей в неиспользуемых компонентах
    - Усложнение мониторинга и защиты системы
- Сценарий атаки
    - Атакующий сканирует систему на наличие уязвимых версий пакетов и эксплуатирует одну из них для повышения
      привилегий или выполнения произвольного кода

#### Использование устаревших пакетов

- Влияние
    - Система содержит известные уязвимости, для которых уже существуют обновления безопасности
    - Возможность эксплуатации публично известных CVE
- Сценарий атаки
    - Использование публичного эксплойта для уязвимой версии пакета с целью компрометации системы, например, через
      RCE (Remote Code Execution) или отказ в исполнении

#### Отсутствие контроля версий библиотек

- Влияние
    - Невоспроизводимость окружения, что усложняет отладку и развертывание
    - Риск несовместимости или скрытых уязвимостей при установке новых версий пакетов
- Сценарий атаки
    - При развёртывании в prod может быть установлена новая версия пакета с уязвимостью, которая эксплуатируется
      атакующим до выпуска исправления

7. Оценим риски ИБ и предложите меры для их снижения

#### Анализ файлов

Начнём с `docker-compose.yml`

- `vulnerable-web`
    - Конфигурация получается с хоста (есть риск, что она содержит уязвимости)
- `insecure-db`:
    - Публичный порт 5432 (PostgreSQL доступен снаружи)
    - Простой пароль для `root`
- `app`:
    - Секретный ключ в переменных среды (`APP_SECRET_KEY=hardcoded-in-env`)
    - Учётные данные БД в открытом виде
- везде
    - Отсутствие использования секретов (Docker Secrets / внешние vault)
    - Отсутствие ограничений ресурсов
    - Нет healthcheck
    - Нет явного указания сетей

Перейдём к `vulnerable-app.yml` ожидая гораздо больший набор уязвимостей

- `vulnerable-web`
    - `privileged: true` - полный доступ к хосту
    - `network_mode: host` - отсутствие сетевой изоляции
    - `user: "0:0"` - выполнение от root
    - `cap_add: - ALL` - все возможные capabilities
    - `security_opt: unconfined` - отключены AppArmor и seccomp
    - все секреты в среде (включая флаг!)
- `debug-shell`
    - Все те же привилегии, что и у первого сервиса
    - SSH сервер в контейнере с паролем `password`
    - Разрешение root-логина по паролю

#### Сценарии реализации рисков

Начнём с Confidentiality Risks (CR)

- Утечка секретов через переменные окружения
    - `docker inspect`, `docker exec env` раскрывают все секреты
    - Логи приложений могут содержать секреты
    - При компрометации одного сервиса становятся доступны сразу все секреты
- Доступ к данным БД
    - Публичный порт PostgreSQL + простой пароль = прямой доступ к данным
    - SQL инъекция через уязвимое приложение
- Доступ к хосту через Docker socket
    - Атакующий может создавать/удалять контейнеры и получать доступ к хосту

Продолжим уже по Data Loss Risks (DL)

- Отсутствует шифрование данных
    - Тома монтируются без шифрования
    - Бэкапы хранятся в открытом виде
- Упрощённое удаление данных
    - Через mounted Docker socket с помощью `docker volume rm`, `docker system prune`
    - Через root-монтирование с помощью `rm -rf /hostroot/*`
- Атака с последующим вымогательством (через root-доступ к хосту и последующим шифрованием всех данных)

В соответствии с этим меняем файлы, добавляя защищенные поля, порты и так далее

8. Анализируем и описываем уязвимости из файлов в результате сканирования безопасности (Trivy).
   Данные получены из `.odt` и `excel` файлов

#### Образ `postgres:16-alpine`

Он содержит критически важные компоненты инфраструктурного уровня.
Выявленные уязвимости сосредоточены в основном в стандартной библиотеке Go, используемой бинарным файлом `gosu`,
входящим в образ.

Всего выявлено 4 уязвимости уровня HIGH и 8 уязвимостей уровня MEDIUM

Уязвимости уровня HIGH

1. **CVE-2025-58183**  
   *Компонент:* `archive/tar` (Go)  
   *Описание:* Неконтролируемое выделение памяти при разборе GNU sparse map.  
   *Риск:* Возможен отказ в обслуживании при обработке специально сформированных tar-архивов.

2. **CVE-2025-58186**  
   *Компонент:* HTTP stack (Go)  
   *Описание:* Ограничение на размер HTTP-заголовков обходится за счёт большого числа cookies.  
   *Риск:* Переполнение памяти и деградация производительности сервиса.

3. **CVE-2025-58187**  
   *Компонент:* `crypto/x509`  
   *Описание:* Неэффективный алгоритм проверки name constraints в сертификатах.  
   *Риск:* Возможность атак типа отказ в обслуживании при обработке специально подготовленных сертификатов.

4. **CVE-2025-61729**  
   *Компонент:* `crypto/x509`  
   *Описание:* Чрезмерное потребление ресурсов при формировании строк ошибок.  
   *Риск:* Увеличение нагрузки на CPU при валидации TLS-сертификатов.

Уязвимости уровня MEDIUM

Уязвимости данной категории в основном связаны с:

- некорректной обработкой ASN.1, PEM и TLS структур;
- возможными panic-сценариями при обработке DSA-ключей;
- квадратичной сложностью алгоритмов парсинга сетевых данных.

Совокупный риск данных уязвимостей заключается в возможности локального или удалённого отказа в обслуживании.
Это особенно опасно в сценариях, где контейнер обрабатывает внешние TLS-соединения или пользовательский ввод.

Заметим, несмотря на то, что уязвимости не затрагивают непосредственно PostgreSQL, они присутствуют в служебных
бинарных зависимостях образа.
В средах с внешним сетевым доступом рекомендуется переход на образ с исправленными Go-библиотеками.

#### Образ `python:3.11-alpine`

В образе выявлена одна уязвимость среднего уровня, связанная с менеджером пакетов `pip`.

Уязвимость уровня MEDIUM

1. **CVE-2025-8869**  
   *Компонент:* `pip`  
   *Описание:* Отсутствие проверок при извлечении символических ссылок из пакетов.  
   *Риск:* Возможна запись файлов вне целевого каталога при установке вредоносного пакета.

Данная уязвимость актуальна в сценариях, где контейнер устанавливает зависимости во время сборки или выполнения.
Или использует непроверенные (сторонние) Python-пакеты.

#### Образ `docker/docker-bench-security:latest`

Тут и комментировать нечего: сборка 2018 года.
Две критические уязвимости, приводящие к дисбалансу стека.
Надо срочно обновиться до актуальной версии

9. Подготавливаю отчёт и делаю снимок с отправкой
10. Чистим кэш и контейнеры

`rm -rf ven` молча рекурсивно и без подтверждений удаляет каталог venv и всё его содержимое

`docker-compose -f demo-vulnerable-app.yml down` останавливает и удаляет использованные контейнеровозом ресурсы

`docker system prune -f` удаляет неиспользованные контейнеровозом ресурсы.
В ходе удаления вернул 158 Мбайт