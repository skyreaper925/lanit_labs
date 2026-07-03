<h1><a id="intro">Лабораторная работа №7</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA">

***

## Список выполненного

- [x] 1. Разверните и подготовьте окружение для уязвимого приложения

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r vulnerable-app/requirements.txt
```

- [x] 2. Запустите уязвимое приложение

```bash
$ docker-compose -f docker-compose.yml up -d --build # http://localhost:8080
```

- [x] 3. Запустите SAST Semgrep и проанализируйте выведенный лог в консоли и опишите логику правил для 
`semgrep-rules.yml` исходя из паттернов, которые используются.
Отчёт будет в директории SAST

```bash
$ semgrep --config sast/semgrep-rules.yml \
  --json \
  --output sast/semgrep-report.json \
  vulnerable-app/
```

- [x] 4. Запустите SAST Checkov по Dockerfile, compose и проанализируйте выведенный лог в консоли и опишите логику 
         правил для `checkov-config.yaml` по `Docker`.
Отчёт будет в директории SAST

```bash
$ checkov \
  --framework dockerfile \
  --file vulnerable-app/Dockerfile docker-compose.yml \
  --output json \
  --output-file-path sast/checkov-report.json \
  --soft-fail
```

- [x] 5. Подготовка зависимостей Java и Maven‑скан для проведения SCA.
Отчёты будут в директории SCA.
Будет ошибка, которую надо поправить, что бы уязвимости определялись или добавить дополнительные уязвимости для их
вывода в отчёте

```bash
$ cd sca
$ ./dependency-check.sh --update # обновление и поставка базы NVD API
$ mvn dependency:resolve
$ mvn dependency:copy-dependencies -DoutputDirectory=./lib # зависимости из $ pom.xml как jar в ./lib
$ mvn org.owasp:dependency-check-maven:check || true # Maven-плагин OWASP
```

- [x] 6. Запустите SCA CLI OWASP Dependency-Check для уязвимого приложения.
Отчеты будут в директории SCA.
Опишите как работает сканирование SCA для `pom.xml` и `app.py`
- [x] 7. Соберите единый отчёт из всех сканирований в виде `html`, `csv`, `json`

```bash
$ bash sca/generate_unified_report.sh
```

- [x] 8. Проанализируйте все уязвимости и обьясните для SAST Checkov сработки статуса `Unknown`.
Классифицируйте их и укажите какие не должны быть в отчётах.
Внесите исправления и запустите повторное сканирование и убедитесь, что они устранены.
Приложите исправленный файл и отчёт без уязвимостей. 
- [x] 9. Опишите выведенные уязвимости для SAST Semgrep и принцип их работы.
Поправьте скрипт `app.py`.
Запустите повторное сканирование и убедитесь, что они устранены.
Приложите исправленный файл `app.py` и отчёт без уязвимостей. 
- [x] 10. Доработайте SCA уязвимости, что бы они только остались в фиинальной версии отчётов.
- [x] 11. Проверьте себя по найденным сработкам анализаторов и так вы сможете помочь себе разобраться в ситуации, если
возникнут сложности

```bash
$ bash cheat_check_yuorself.sh
```

- [x] 12. Делайте все коммиты на соответствующих шагах, далее заливайте изменения в удаленный репозиторий.
- [x] 13. Подготовьте отчет `gist`.
- [ ] 14. Почистите кеш от `venv` и остановите уязвимое приложение

```bash
$ deactivate
$ rm -rf venv
$ docker-compose -f ххх down
$ docker-compose -f docker-compose.yml down
$ docker system prune -f
```