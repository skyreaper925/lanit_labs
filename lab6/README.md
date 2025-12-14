<h1><a id="intro">Лабораторная работа №6</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA">

***

## Список выполненного

- [x] 1. Необходимо установить `Docker Engine` для Linux

```bash
$ sudo apt-get update
$ sudo apt-get install -y docker.io
$ sudo usermod -aG docker "$USER"

$ sudo systemctl start docker
$ docker pull docker/docker-bench-security
```

- [x] 2. Проверьте работу докера и сделать скрипт `audit.sh` исполняемым
- [x] 3. Развернуть уязвимое приложение как отдельные стенды

```bash
$ docker compose up -d # основной web, app, postgres
$ docker-compose -f dvulnerable-app.yml up -d # поверх для vulnerable-web, debug-shell
    -f # file
    up # создает и поднимает файлы из compose
    -d # фоновый режим
```

- [x] 4. Запустите скрипт из `venv` и проанализируйте то, что вывело на терминале и что вывело при конвертировании

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install openpyxl odfpy
$ ./audit.sh
$ deactivate # или $ deactivate 2>/dev/null || true
```
 
- [x] 5. Проведите анализ уязвимостей, опишите их причину возникновения
- [x] 6. Опишите влияния уязвимостей, их сценарий атаки
- [x] 7. Оцените риски ИБ и предложите меры для их снижения: 
> - Следует разобрать `.yaml` описав, что в них считается не безопасным и почему
> - Опишите сценарии реализации рисков CR, DL
> - Предложили исправленные `.yaml`
- [x] 8. Сделайте анализ уязвимостей из сгенерированных файлов .odt, .xslx и опишите их в отчете. Файлы 
  конвертируются в эти директории

```bash
"├── json/          (Trivy JSON outputs)"
"├── text/          (CIS audit text outputs)"
"├── xlsx/          (Excel spreadsheets)"
"└── odt/           (OpenDocument Text files)"
```

- [x] 9. Подготовьте отчёт `gist`.
- [x] 10. Почистите кеш от `venv` и остановите уязвимостей приложение, почистите контейнера

```bash
$ rm -rf venv
$ docker-compose -f demo-vulnerable-app.yml down
$ docker system prune -f
```