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

4. Копируем файл из первой работы в нашу папку и переименовываем в hello2.py.
Меняем Dockerfile и анализируем его.
Делаем снимок

5. Анализируем ответы
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker buildx build -t hello-appsec-world .
[+] Building 1.0s (13/13) FINISHED                                                                                                                             docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                           0.0s
 => => transferring dockerfile: 796B                                                                                                                                           0.0s 
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                                                                            0.3s 
 => [internal] load .dockerignore                                                                                                                                              0.0s
 => => transferring context: 2B                                                                                                                                                0.0s 
 => [internal] load build context                                                                                                                                              0.0s 
 => => transferring context: 66B                                                                                                                                               0.0s 
 => [builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c                                              0.1s 
 => => resolve docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c                                                      0.1s 
 => CACHED [builder 2/4] WORKDIR /hello                                                                                                                                        0.0s 
 => CACHED [builder 3/4] COPY requirements.txt .                                                                                                                               0.0s
 => CACHED [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt                                                                    0.0s 
 => CACHED [stage-1 3/6] COPY --from=builder /wheels /wheels                                                                                                                   0.0s 
 => CACHED [stage-1 4/6] COPY requirements.txt .                                                                                                                               0.0s 
 => CACHED [stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt                                                                                   0.0s 
 => CACHED [stage-1 6/6] COPY hello2.py .                                                                                                                                      0.0s 
 => exporting to image                                                                                                                                                         0.3s 
 => => exporting layers                                                                                                                                                        0.0s 
 => => exporting manifest sha256:e616096521d87e359016897a95328555ce4e69fc25e904bbf51acc23626da0cc                                                                              0.0s 
 => => exporting config sha256:299df4359d31c14d1778b6124d44a7412f64c91ddd8c86e561d531229c0f773c                                                                                0.0s 
 => => exporting attestation manifest sha256:3492461941a290fa140decee2637a1ca2f1eb73634489d00ca48dd8fa3c9633d                                                                  0.1s 
 => => exporting manifest list sha256:a574690d2d058d09bc6742ec31fc3b2e75c7b861a981881fdd50f81349c87c3d                                                                         0.0s 
 => => naming to docker.io/library/hello-appsec-world:latest                                                                                                                   0.0s 
 => => unpacking to docker.io/library/hello-appsec-world:latest                                                                                                                0.0s 
```
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker run hello-appsec-world h                                                                                            
Hello, h!
```
Команда docker save -o hello_ypur_project.tar hello-appsec-world выполнилась без ответа

Загружаем из файла
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker load -i hello_ypur_project.tar
Loaded image: hello-appsec-world:latest
```
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker run hello-appsec-world Paul
Hello, Paul!
```
Выгружаем старый файл
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker load -i hello.tar          
Loaded image: hellow-appsec-world:latest
```
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker run hello-appsec-world Paul
Hello, Paul!
```
Сравниваем суммы: не равны
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> (Get-FileHash hello_ypur_project.tar -Algorithm SHA256).Hash
1393B0535CBF34A19C8A8CB96B760FE39EE71DE23E65F83E6A7990FCF352CE9B
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> (Get-FileHash hello.tar -Algorithm SHA256).Hash
3CA95D23B7FDE0FEDB6526BE1AC9D6F8450D4F686A8B4D92B10DA0C0B327639C
```
В итоге выясняется, что это Windows (хотя сам nmap это автоматически не понял), ssh и telnet закрыты

6. Дорабатываем сценарий, путём прописывания требований.
Была выбрана запись со знаками порядка для большей гибкости: `typer>=0.20.0`