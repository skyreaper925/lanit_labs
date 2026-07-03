<h1><a id="intro">Лабораторные работы — AppSec / DevSecOps</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a>
<a href="https://www.docker.com"><img src="https://img.shields.io/static/v1?logo=docker&logoColor=fff&label=&message=Docker&color=36393f&style=flat" alt="Docker"></a>
<a href="https://www.python.org"><img src="https://img.shields.io/static/v1?logo=python&logoColor=fff&label=&message=Python&color=36393f&style=flat" alt="Python"></a>
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt="RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt="AppSec">

### Володин Максим

***

## О репозитории

Выполненные лабораторные работы курса прикладной безопасности приложений
([geminishkv/course_labs](https://github.com/geminishkv/course_labs)) — от основ Git
до построения элементов DevSecOps-конвейера: анализ рисков, сканирование сети,
контейнеризация, аудит Docker по CIS, SAST и SCA.

## Состав работ

| # | Тема | Ключевые материалы |
|---|------|--------------------|
| [1](lab1/) | Git SCM: SSH/GPG-ключи, подписанные коммиты, ветки, PR, rebase | `hello.py` (Typer CLI), [отчёт](lab1/report.md) |
| [2](lab2/) | Права доступа, пользователи и группы, ACL, процессы | `pygamesteel.py`, [отчёт](lab2/report.md) |
| [3](lab3/) | Сканирование сети Nmap, NSE-скрипты, отчёты в txt/xml/html | [`project/reports/`](lab3/project/reports/), [отчёт](lab3/report.md) |
| [4](lab4/) | Анализ рисков ИБ: кейс открытой админ-консоли, GDPR/152-ФЗ | [аналитическая записка](lab4/note.md) |
| [5](lab5/) | Docker: multi-stage сборка, образы и архивы, docker-compose (client/server) | [`source/`](lab5/source/), [`docker-compose.yml`](lab5/docker-compose.yml), [отчёт](lab5/report.md) |
| [6](lab6/) | Аудит Docker: CIS Benchmark (docker-bench-security), Trivy | [`audit.sh`](lab6/audit.sh), [`audit_reports/`](lab6/audit_reports/), [отчёт](lab6/report.md) |
| [7](lab7/) | SAST (Semgrep, Checkov) и SCA (OWASP Dependency-Check) уязвимого приложения | [`vulnerable-app/`](lab7/vulnerable-app/), [`reports/`](lab7/reports/), [отчёт](lab7/report.md) |

## Структура и процесс

- Каждая работа ведётся в своей ветке `labN` и вливается в `master` через pull request.
- Внутри каталога работы: `README.md` — задание/чек-лист, `report.md` — отчёт о выполнении
  с выводом команд; отчёты дублируются в виде gist.
- Все коммиты подписаны GPG (`git commit -S`).

## Инструменты

`git` / `gh` / GnuPG · Linux CLI (права, ACL, процессы) · `nmap` + NSE · Docker, BuildKit,
docker-compose · docker-bench-security, Trivy · Semgrep, Checkov, OWASP Dependency-Check, Maven

## Лицензия

[Apache License 2.0](LICENSE.md) · [NOTICE](NOTICE.md) · [SECURITY](SECURITY.md) ·
[CONTRIBUTING](CONTRIBUTING.md) · [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md)
