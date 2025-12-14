# Отчёт по лабораторной работе 5
### Володин Максим

1. Устанавливаю docker-desktop для Windows через Chocolatey
2. Анализируем ответы.
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

7. Делаю снимок.
Повторяю сборку
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker buildx build -t hello-appsec-world .                 
[+] Building 2.2s (14/14) FINISHED                                                                                                                             docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                           0.0s
 => => transferring dockerfile: 796B                                                                                                                                           0.0s 
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                                                                            1.6s 
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                                  0.0s
 => [internal] load .dockerignore                                                                                                                                              0.0s
 => => transferring context: 2B                                                                                                                                                0.0s 
 => [internal] load build context                                                                                                                                              0.0s 
 => => transferring context: 66B                                                                                                                                               0.0s 
 => [builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c                                              0.1s 
 => => resolve docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c                                                      0.0s 
 => CACHED [builder 2/4] WORKDIR /hello                                                                                                                                        0.0s
 => CACHED [builder 3/4] COPY requirements.txt .                                                                                                                               0.0s 
 => CACHED [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt                                                                    0.0s 
 => CACHED [stage-1 3/6] COPY --from=builder /wheels /wheels                                                                                                                   0.0s 
 => CACHED [stage-1 4/6] COPY requirements.txt .                                                                                                                               0.0s 
 => CACHED [stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt                                                                                   0.0s 
 => CACHED [stage-1 6/6] COPY hello2.py .                                                                                                                                      0.0s 
 => exporting to image                                                                                                                                                         0.2s 
 => => exporting layers                                                                                                                                                        0.0s 
 => => exporting manifest sha256:e616096521d87e359016897a95328555ce4e69fc25e904bbf51acc23626da0cc                                                                              0.0s 
 => => exporting config sha256:299df4359d31c14d1778b6124d44a7412f64c91ddd8c86e561d531229c0f773c                                                                                0.0s 
 => => exporting attestation manifest sha256:a2b6b7d49997b51e821bcee2d26ba97a819b7dcda0a1cfe48496635c4fc754ae                                                                  0.1s 
 => => exporting manifest list sha256:e30ca18ab248eb250e64e2dded38b6f6d5376e5035ff2059c4659a6cc57e5455                                                                         0.0s 
 => => naming to docker.io/library/hello-appsec-world:latest                                                                                                                   0.0s 
 => => unpacking to docker.io/library/hello-appsec-world:latest 
```
Теперь сохраняю конфигурацию в архив hello_ypur_project и вновь делаю снимок

8. Выводим и анализируем
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker login
Authenticating with existing credentials... [Username: skyreaper925]

i Info → To login with a different account, run 'docker logout' followed by 'docker login'


Login Succeeded
```
Команда docker tag hello-appsec-world skyreaper925/hello-appsec-world выполнилась без ответа
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker push skyreaper925/hello-appsec-world
Using default tag: latest
The push refers to repository [docker.io/skyreaper925/hello-appsec-world]
3ed168cd5a5b: Pushed 
3f0cdbca744e: Pushed 
02e7aee8b3ff: Pushed 
938fadf968c5: Pushed 
72cf4c3b8301: Pushed 
1ba09f86df22: Pushed 
4d55cfecf366: Pushed 
8614947fd91c: Pushed 
1a5ec6c9a91d: Pushed 
1733a4cd5954: Pushed 
latest: digest: sha256:e30ca18ab248eb250e64e2dded38b6f6d5376e5035ff2059c4659a6cc57e5455 size: 856
```
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker inspect skyreaper925/hello-appsec-world
[
    {
        "Id": "sha256:e30ca18ab248eb250e64e2dded38b6f6d5376e5035ff2059c4659a6cc57e5455",
        "RepoTags": [
            "hello-appsec-world:latest",
            "skyreaper925/hello-appsec-world:latest"
        ],
        "RepoDigests": [
            "hello-appsec-world@sha256:e30ca18ab248eb250e64e2dded38b6f6d5376e5035ff2059c4659a6cc57e5455",
            "skyreaper925/hello-appsec-world@sha256:e30ca18ab248eb250e64e2dded38b6f6d5376e5035ff2059c4659a6cc57e5455"
        ],
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2025-12-14T08:37:41.6036794Z",
        "Config": {
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D",
                "PYTHON_VERSION=3.11.14",
                "PYTHON_SHA256=8d3ed8ec5c88c1c95f5e558612a725450d2452813ddad5e58fdb1a53b1209b78",
                "PYTHONUNBUFFERED=1"
            ],
            "Entrypoint": [
                "python",
                "hello2.py"
            ],
            "WorkingDir": "/hello"
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 55401892,
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:77a2b55fbe8b9984ce0af3ffc0b0ab62507668e63306ec161a585e587a3eb164",
                "sha256:424dc4972605239ec660864fe4cc7bcf6ebdadd752a7ee7ad065a83c34798378",
                "sha256:600af8de593b464a3642857b2dce39ad42474145771745962fb90ea9c276fa9d",
                "sha256:fa384bf02ac198a84ae5f0bbe085a6e4bd2de0be1b595833ba52e9780a936ba9",
                "sha256:d3e56a92f0b1ff7d458de6a0703579c1453185fd28f49e7a660b2a8f59cb44b5",
                "sha256:5f0651f3fcfeb100b04a77b67f9c4628857e66f2f53224614ee2b4f5489f95bc",
                "sha256:160ec72e0926b0aa8cc7b431253fa55dce696c726895a870b6cdacb4e07943d6",
                "sha256:5631378a81ed15a66d90bcb0c01d9ee3ed218a20368cb714c05086cc6459d1a5",
                "sha256:f607aef82abeaa6ffc4cb8817d6f8c40108c3a6529723461e9cb85e457c297df"
            ]
        },
        "Metadata": {
            "LastTagTime": "2025-12-14T09:04:08.803620195Z"
        },
        "Descriptor": {
            "mediaType": "application/vnd.oci.image.index.v1+json",
            "digest": "sha256:e30ca18ab248eb250e64e2dded38b6f6d5376e5035ff2059c4659a6cc57e5455",
            "size": 856
        }
    }
]
```
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker container create --name first hello-appsec-world
c929fe9bab3cb62fd54cd10ca120efa93bb394a260d5540fadafcbf2aa259bef
```

Теперь получаем эталонный архив.
Архив от преподавателя недоступен для linux/amd64, поэтому был взят похожий найденный
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker image pull zlatasin/hello-appsec-world                    
Using default tag: latest
latest: Pulling from zlatasin/hello-appsec-world
c2caed0fc8c2: Pull complete 
38f251d4cf62: Pull complete 
5833e3daf776: Pull complete 
222697651838: Pull complete 
623069b60944: Pull complete 
Digest: sha256:71a41806b022a5b1aad758b2840962b8309a733662dffcbb9603ff4f0236668e
Status: Downloaded newer image for zlatasin/hello-appsec-world:latest
docker.io/zlatasin/hello-appsec-world:latest
```
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker inspect zlatasin/hello-appsec-world                         
[
    {
        "Id": "sha256:71a41806b022a5b1aad758b2840962b8309a733662dffcbb9603ff4f0236668e",
        "RepoTags": [
            "zlatasin/hello-appsec-world:latest"
        ],
        "RepoDigests": [
            "zlatasin/hello-appsec-world@sha256:71a41806b022a5b1aad758b2840962b8309a733662dffcbb9603ff4f0236668e"
        ],
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2025-12-13T19:48:37.446584062Z",
        "Config": {
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D",
                "PYTHON_VERSION=3.11.14",
                "PYTHON_SHA256=8d3ed8ec5c88c1c95f5e558612a725450d2452813ddad5e58fdb1a53b1209b78",
                "PYTHONUNBUFFERED=1"
            ],
            "Entrypoint": [
                "python",
                "hello_my.py"
            ],
            "WorkingDir": "/hello"
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 55401119,
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:77a2b55fbe8b9984ce0af3ffc0b0ab62507668e63306ec161a585e587a3eb164",
                "sha256:424dc4972605239ec660864fe4cc7bcf6ebdadd752a7ee7ad065a83c34798378",
                "sha256:600af8de593b464a3642857b2dce39ad42474145771745962fb90ea9c276fa9d",
                "sha256:fa384bf02ac198a84ae5f0bbe085a6e4bd2de0be1b595833ba52e9780a936ba9",
                "sha256:2ed536e77d35ada80b98421d9500abff9ff27fcaf197f8181839ac57a06179fb",
                "sha256:f9209d6e0d0368be941d9139d5f2c04e6779b3892a58729b771f68c8426fed6a",
                "sha256:3dede0cb039d69d2c5720d1888d57548a96ce99b0cd13c4bb1b971f1b0e0d045",
                "sha256:1df5dbce9a02f172f4b16441ffb8e3b8f3c6d79f49d622c995de69258cda2f1e",
                "sha256:e763f7291c46b317bbb9b2172c2fc5acd77fb7bd2b5e52f50e75794aac35247f"
            ]
        },
        "Metadata": {
            "LastTagTime": "2025-12-14T09:14:06.170832658Z"
        },
        "Descriptor": {
            "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
            "digest": "sha256:71a41806b022a5b1aad758b2840962b8309a733662dffcbb9603ff4f0236668e",
            "size": 2201
        }
    }
]
```
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker container create --name second hello-appsec-world           
677c226e9aad9dc5523d1cc274a6df3cf8d8f684b529fb9e301455f301918f54
```

9. Анализируем процессы
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker container run -it ubuntu /bin/bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
20043066d3d5: Pull complete 
06808451f0d6: Download complete 
Digest: sha256:c35e29c9450151419d9448b0fd75374fec4fff364a27f176fb458d472dfc9e54
Status: Downloaded newer image for ubuntu:latest
root@076e4a299b83:/# ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   4588  3584 pts/0    Ss   09:21   0:00 /bin/bash
root         9  100  0.0   7888  3840 pts/0    R+   09:24   0:00 ps aux
root@076e4a299b83:/# whoami
root 
```
10. Выводим оба контейнера на терминал
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker ps -a | Select-String "first|second"

677c226e9aad   hello-appsec-world    "python hello2.py"       23 minutes ago      Created                                  second
c929fe9bab3c   hello-appsec-world    "python hello2.py"       36 minutes ago      Created                                  first
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker start first
first
PS C:\Users\user\PycharmProjects\lanit_labs\lab5\source> docker start second
second
```
11. Переходим в основной корень, запускаем и анализируем
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5> docker-compose up --build
time="2025-12-14T12:52:59+03:00" level=warning msg="C:\\Users\\user\\PycharmProjects\\lanit_labs\\lab5\\docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
[+] Building 22.6s (27/27) FINISHED                                                                                                                                                 
 => [internal] load local bake definitions                                                                                                                                     0.0s
 => => reading from stdin 1.04kB                                                                                                                                               0.0s
 => [client internal] load build definition from Dockerfile                                                                                                                    0.1s 
 => => transferring dockerfile: 425B                                                                                                                                           0.0s 
 => [server internal] load build definition from Dockerfile                                                                                                                    0.1s 
 => => transferring dockerfile: 419B                                                                                                                                           0.0s 
 => [server internal] load metadata for docker.io/library/python:3.11-slim                                                                                                     1.3s 
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                                  0.0s
 => [server internal] load .dockerignore                                                                                                                                       0.0s
 => => transferring context: 2B                                                                                                                                                0.0s
 => [client internal] load .dockerignore                                                                                                                                       0.0s
 => => transferring context: 2B                                                                                                                                                0.0s 
 => [server builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c                                       0.1s 
 => => resolve docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c                                                      0.1s 
 => [server internal] load build context                                                                                                                                       0.0s 
 => => transferring context: 63B                                                                                                                                               0.0s 
 => [client internal] load build context                                                                                                                                       0.1s 
 => => transferring context: 66B                                                                                                                                               0.0s 
 => CACHED [server builder 2/4] WORKDIR /app                                                                                                                                   0.0s 
 => CACHED [client builder 3/4] COPY requirements.txt .                                                                                                                        0.0s 
 => CACHED [server builder 3/4] COPY requirements.txt .                                                                                                                        0.0s 
 => [server builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt                                                                   11.9s 
 => [client builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt                                                                   11.0s 
 => [client stage-1 3/6] COPY --from=builder /wheels /wheels                                                                                                                   0.1s 
 => [client stage-1 4/6] COPY requirements.txt .                                                                                                                               0.1s 
 => [client stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt                                                                                   4.2s 
 => [server stage-1 3/6] COPY --from=builder /wheels /wheels                                                                                                                   0.1s 
 => [server stage-1 4/6] COPY requirements.txt .                                                                                                                               0.1s 
 => [server stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt                                                                                   4.2s 
 => [client stage-1 6/6] COPY client.py .                                                                                                                                      0.1s 
 => [client] exporting to image                                                                                                                                                2.3s 
 => => exporting layers                                                                                                                                                        1.4s 
 => => exporting manifest sha256:df0c384f3132fd544ba53a0a5ab412b39a547d0c9f86599b77b576232ef3bb23                                                                              0.0s 
 => => exporting config sha256:e8f318e857ad93bea15881e1b7fa6e33e3af8161f98e3a3e151394e3a10ffbf9                                                                                0.0s 
 => => exporting attestation manifest sha256:e6dfa9ed13cc7e39e13699492bec0c8c8af1ffca354f471994125f658bcf5091                                                                  0.1s 
 => => exporting manifest list sha256:1fe64a994164713fe42c708fbb377700b217cea94780f01579370091daba8f45                                                                         0.0s 
 => => naming to docker.io/library/lab5-client:latest                                                                                                                          0.0s 
 => => unpacking to docker.io/library/lab5-client:latest                                                                                                                       0.7s 
 => [server stage-1 6/6] COPY app.py .                                                                                                                                         0.1s 
 => [server] exporting to image                                                                                                                                                2.9s 
 => => exporting layers                                                                                                                                                        1.4s 
 => => exporting manifest sha256:d6bf5e8bddc82f93823dbee1314cf7e6fd5013b8a2159183354c385bd489d6d6                                                                              0.0s 
 => => exporting config sha256:811025928b51f2d0c1e912696181e184583f6ff52b36227bf0295876c6b96839                                                                                0.0s 
 => => exporting attestation manifest sha256:3865cc8d5203a28f9b399c9ce8d72b8837c050278cfe354ef73941d6c3eba66a                                                                  0.1s 
 => => exporting manifest list sha256:5e2e8cf7b843114cb5d871761dd8ae46d91cf75a8a63390863ee2a76ff2c0b0a                                                                         0.1s 
 => => naming to docker.io/library/lab5-server:latest                                                                                                                          0.0s 
 => => unpacking to docker.io/library/lab5-server:latest                                                                                                                       1.1s 
 => [client] resolving provenance for metadata file                                                                                                                            0.2s 
 => [server] resolving provenance for metadata file                                                                                                                            0.1s 
[+] Running 5/5                                                                                                                                                                     
 ✔ lab5-server              Built                                                                                                                                              0.0s 
 ✔ lab5-client              Built                                                                                                                                              0.0s 
 ✔ Network lab5_app_net     Created                                                                                                                                            0.1s 
 ✔ Container lab5-server-1  Created                                                                                                                                            0.5s 
 ✔ Container lab5-client-1  Created                                                                                                                                            0.3s 
Attaching to client-1, server-1
```
12. Выводим на терминале
```
Start-Process "chrome.exe" "http://localhost:8000"
```
13. Обращаемся ко всем контейнерам
```aiignore
PS C:\Users\user\PycharmProjects\lanit_labs\lab5> docker ps -a
CONTAINER ID   IMAGE                 COMMAND                  CREATED             STATUS                         PORTS                                         NAMES
34758a563f74   lab5-client           "python client.py"       5 minutes ago       Exited (0) 3 minutes ago                                                     lab5-client-1
c473e56ec9b2   lab5-server           "python app.py"          5 minutes ago       Up 5 minutes                   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   lab5-server-1
076e4a299b83   ubuntu                "/bin/bash"              37 minutes ago      Exited (2) 33 minutes ago                                                    gallant_antonelli
677c226e9aad   hello-appsec-world    "python hello2.py"       38 minutes ago      Exited (2) 12 minutes ago                                                    second
c929fe9bab3c   hello-appsec-world    "python hello2.py"       51 minutes ago      Exited (2) 12 minutes ago                                                    first
ffe63b58c121   a574690d2d05          "python hello2.py Pa…"   About an hour ago   Exited (0) About an hour ago                                                 distracted_keller
8076776b940e   a574690d2d05          "python hello2.py Pa…"   About an hour ago   Exited (0) About an hour ago                                                 nostalgic_dewdney
c00d46750865   a574690d2d05          "python hello2.py"       About an hour ago   Exited (2) About an hour ago                                                 focused_herschel
0b0df746d9ca   a574690d2d05          "python hello2.py h"     About an hour ago   Exited (0) About an hour ago                                                 laughing_yonath
82fce3e37609   7c6c4a9ed199          "h"                      About an hour ago   Created                                                                      jovial_pasteur
9629276107e8   8e03bcc96e45          "h"                      About an hour ago   Created                                                                      reverent_haibt
cbf1e931af56   8e03bcc96e45          "-h"                     About an hour ago   Created                                                                      condescending_faraday
e5d041a6d984   8e03bcc96e45          "python hello2.py"       About an hour ago   Exited (2) About an hour ago                                                 angry_hertz
2bbd36c2ea13   f41fab8e8623          "python hello2.py"       11 hours ago        Exited (2) 11 hours ago                                                      quizzical_keldysh
60930ba2245b   6073ebbdff01          "python hello2.py"       11 hours ago        Exited (1) 11 hours ago                                                      mystifying_cannon
a0021d2e282f   e1ea8634c504          "python hello2.py"       11 hours ago        Exited (1) 11 hours ago                                                      lucid_ardinghelli
2c272365a356   44576ff2966e          "python hello2.py"       11 hours ago        Exited (1) 11 hours ago                                                      awesome_joliot
50cf15c257b0   44576ff2966e          "python hello2.py"       11 hours ago        Exited (1) 11 hours ago                                                      dazzling_kirch
5a0985067405   44576ff2966e          "python hello2.py"       11 hours ago        Exited (1) 11 hours ago                                                      cool_lewin
54ba766018dc   44576ff2966e          "python hello2.py"       11 hours ago        Exited (1) 11 hours ago                                                      suspicious_visvesvaraya
8169cf1a4bcb   44576ff2966e          "python hello2.py"       12 hours ago        Exited (1) 12 hours ago                                                      competent_dirac
0398b895d946   44576ff2966e          "python hello2.py"       12 hours ago        Exited (1) 12 hours ago                                                      funny_jepsen
4da558dfa731   hellow-appsec-world   "python hello.py"        13 hours ago        Exited (0) 13 hours ago                                                      infallible_banach
```
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5> docker ps -q
c473e56ec9b2
```
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5> docker images
                                                                                                                                                                i Info →   U  In Use
IMAGE                                    ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-appsec-world:latest                e30ca18ab248        226MB         55.4MB    U   
hellow-appsec-world:latest               168b5e477344        203MB         49.5MB    U   
lab5-client:latest                       1fe64a994164        208MB         50.9MB    U   
lab5-server:latest                       5e2e8cf7b843        211MB         51.8MB    U   
skyreaper925/hello-appsec-world:latest   e30ca18ab248        226MB         55.4MB    U   
ubuntu:latest                            c35e29c94501        119MB         31.7MB    U   
zlatasin/hello-appsec-world:latest       71a41806b022        226MB         55.4MB        
```
Останавливаем работу
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5> docker ps -q | xargs docker stop
c473e56ec9b2
```
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab5> docker-compose down
time="2025-12-14T13:02:51+03:00" level=warning msg="C:\\Users\\user\\PycharmProjects\\lanit_labs\\lab5\\docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
[+] Running 3/3
 ✔ Container lab5-client-1  Removed                                                                                                                                            0.1s 
 ✔ Container lab5-server-1  Removed                                                                                                                                            0.2s 
 ✔ Network lab5_app_net     Removed
 ```
14. По-большому счёту, доработка не требуется, но была произведена.
Делаем снимок
15. Делаем отправку на удалённое хранилище
16. Оформляем отчёт и делаем снимок с отправкой