# Отчёт по лабораторной работе 7

### Володин Максим

1. Командой `python3 -m venv venv` установил виртуальное окружение (выполнилась без ответа)

Затем я активировал виртуальное окружение командой `source venv/bin/activate`, что тоже выполнилась без ответа

Устанавливаю требуемые пакеты из файла с помощью `pip install -r vulnerable-app/requirements.txt`

2. Запускаю уязвимое приложение

```
user@RAM:/mnt/c/Users/user/PycharmProjects/lanit_labs/lab7$ docker-compose -f docker-compose.yml up -d --build # http://localhost:8080
WARN[0000] /mnt/c/Users/user/PycharmProjects/lanit_labs/lab7/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Building 136.2s (14/14) FINISHED                                                                                                                                                
 => [internal] load local bake definitions                                                                                                                                     0.0s
 => => reading from stdin 607B                                                                                                                                                 0.0s
 => [internal] load build definition from Dockerfile                                                                                                                           0.1s 
 => => transferring dockerfile: 463B                                                                                                                                           0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                                                                            4.2s 
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                                  0.0s
 => [internal] load .dockerignore                                                                                                                                              0.1s
 => => transferring context: 2B                                                                                                                                                0.0s 
 => [1/6] FROM docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c                                                      0.1s 
 => => resolve docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c                                                      0.1s
 => [internal] load build context                                                                                                                                              0.1s 
 => => transferring context: 4.12kB                                                                                                                                            0.0s 
 => CACHED [2/6] WORKDIR /app                                                                                                                                                  0.0s 
 => [3/6] RUN apt-get update &&     apt-get install -y --no-install-recommends         build-essential         libjpeg-dev zlib1g-dev         libxml2-dev libxslt1-dev &&     53.4s 
 => [4/6] COPY requirements.txt /app/requirements.txt                                                                                                                          0.3s 
 => [5/6] RUN pip install --no-cache-dir -r requirements.txt                                                                                                                  34.9s 
 => [6/6] COPY . /app                                                                                                                                                          0.2s 
 => exporting to image                                                                                                                                                        40.3s 
 => => exporting layers                                                                                                                                                       20.5s 
 => => exporting manifest sha256:5b794e288199ab5e6639dc963fc98fd4bfe9078877f124b3d10df38117105dc4                                                                              0.0s 
 => => exporting config sha256:05caf9f7a641229b118d50832478878c403006598b67cc4ba7cd13b2c7339ff3                                                                                0.0s 
 => => exporting attestation manifest sha256:eb242006a9822ab0dc43b0d6a894013c43c60f332279ebb0cf22c61ae443c204                                                                  0.1s 
 => => exporting manifest list sha256:14c128b62a0eb77b1d9d84bd0b6a8871b274d8cbbb7e2cad2ceac3c3e14b9d79                                                                         0.0s 
 => => naming to docker.io/library/lab7-vulnerable-app:latest                                                                                                                  0.0s 
 => => unpacking to docker.io/library/lab7-vulnerable-app:latest                                                                                                              19.6s 
 => resolving provenance for metadata file                                                                                                                                     0.3s 
[+] Running 3/3                                                                                                                                                                     
 ✔ lab7-vulnerable-app              Built                                                                                                                                      0.0s 
 ✔ Network lab7_default             Created                                                                                                                                    0.1s 
 ✔ Container lab7-vulnerable-app-1  Started  
```

3. Сначала устанавливаем недостающее
```
user@RAM:/mnt/c/Users/user/PycharmProjects/lanit_labs/lab7$ sudo snap install semgrep
[sudo] password for user: 
semgrep 1.56.0 from George-Andrei Iosif (iosifache) installed
```

Запускаем SAST Semgrep.
Команда выполнилась молча

4. Теперь запускаем SAST Checkov по Dockerfile и compose.
Сначала вновь устанавливаем библиотеку

После выполнения в консоли отражена сводка

```
passed: 50 
failed: 2 
skipped: 0
parsing_errors: 0 
resource_count: 1 
checkov_version: 3.2.459
```
5. Сначала переходим в другую папку и оттуда обновляем базу.
После этого устанавливаем новые зависимости (322 тысячи)

Ошибка была исправлена выгрузкой зависимостей из файла `pom.xml` в папку из сценария

В результате выполнения SCA-анализа был сформирован единый агрегированный отчёт

6. Запускаем `SCA CLI OWASP Dependency-Check` для уязвимого приложения.

Для `pom.xml` сканирование работает в обратную сторону: получает версии библиотек, которые затем сопоставлялись с CVE.
То есть файл был основным источник информации о зависимостях.

Для `app.py` сканирование не находило логических или программных уязвимостей.

7. Запускаем `bash sca/generate_unified_report.sh`, что выполнилась молча и выдал три файла на выходе

8. Анализ общего отчёта.

Из основного 
- По результатам первичного сканирования выявлены уязвимости SAST в app.py (SQLi, XSS, RCE, LFI, небезопасная 
десериализация и eval) и нарушения Docker-политик (отсутствие HEALTHCHECK и запуск без явного non-root пользователя).
- SCA обнаружил множество CVE в устаревших Java-зависимостях (Jackson 2.4.6, Groovy 2.1.6, commons-httpclient 3.1).
- Статус UNKNOWN у Checkov связан с отсутствием/непопаданием severity в маппинг unified-скрипта, а не с ‘неизвестной’ 
  природой проблемы; проверки относятся к compliance/policy. 
- После исправлений (безопасная обработка ввода, отказ от опасных вызовов, ограничение доступа к файлам, обновление/замена зависимостей, добавление non-root и HEALTHCHECK) повторный прогон инструментов показал отсутствие уязвимостей в итоговом unified-report

9. Меняю файл и делаю снимок
10. Убираю лишнее

11. Запускаю скрипт проверки

Далее не делаю из-за цейтнота