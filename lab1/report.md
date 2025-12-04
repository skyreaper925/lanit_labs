# Отчёт по лабораторной  работе 1
### Володин Максим
## Часть 1
1. Создадим репо
```
PS C:\Users\user> mkdir lanit_labs

    Directory: C:\Users\user

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----          04.12.2025    13:40                lanit_labs
```
2. Инициализируем его
```
PS C:\Users\user> cd lanit_labs
PS C:\Users\user\lanit_labs> git init
Initialized empty Git repository in C:/Users/user/lanit_labs/.git/
```
3. Входим на новом устройстве (авторизуемся)
```
PS C:\Users\user\lanit_labs> gh auth login
? Where do you use GitHub? GitHub.com
? What is your preferred protocol for Git operations on this host? SSH
? Upload your SSH public key to your GitHub account? C:\Users\user\.ssh\id_ed25519.pub
? Title for your SSH key: (GitHub CLI)

? Title for your SSH key: GitHub CLI
? How would you like to authenticate GitHub CLI? Login with a web browser

! First copy your one-time code: 5D5C-F26C
Press Enter to open https://github.com/login/device in your browser...
✓ Authentication complete.
- gh config set -h github.com git_protocol ssh
✓ Configured git protocol
✓ SSH key already existed on your GitHub account: C:\Users\user\.ssh\id_ed25519.pub
✓ Logged in as skyreaper925
```
4. Создаём README

```New-Item -ItemType file README.md```

5. Присваиваем ветке статус исходной
```
gh repo create lanit_labs --public --source=. --remote=origin
✓ Created repository skyreaper925/lanit_labs on github.com
  https://github.com/skyreaper925/lanit_labs
✓ Added remote git@github.com:skyreaper925/lanit_labs.git
```
6. Добавляем в снимок репо и делаем снимок
```
PS C:\Users\user\lanit_labs> git add README.md
PS C:\Users\user\lanit_labs> git commit -S -m "Initial commit: add empty README.md"
[master (root-commit) 8754021] Initial commit: add empty README.md
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
```
7. Делаем отправку в удалённый репо
```shell
On branch master
PS C:\Users\user\lanit_labs> git push -u origin master
The authenticity of host 'github.com (140.82.121.3)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
Enter passphrase for key '/c/Users/user/.ssh/id_ed25519':
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 755 bytes | 377.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To github.com:skyreaper925/lanit_labs.git
 * [new branch]      master -> master
branch 'master' set up to track 'origin/master'.
```
8. Создаю грязный файл hello.py

9. Добавляю его в снимок
```
PS C:\Users\user\lanit_labs> git add hello.py
PS C:\Users\user\lanit_labs> git commit -S -m "Add dirty hello.py"
[master e83d795] Add dirty hello.py
 1 file changed, 4 insertions(+)
 create mode 100644 hello.py
```
10. Меняю последнюю строчку в файле
11. Делаю отправку
```
PS C:\Users\user\lanit_labs> git push -u origin master
Enter passphrase for key '/c/Users/user/.ssh/id_ed25519':
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 890 bytes | 890.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To github.com:skyreaper925/lanit_labs.git
   8754021..e83d795  master -> master
branch 'master' set up to track 'origin/master'.
```
Вывод истории изменений
```
commit e83d795b8823c24c8ca90f51c36945a38ce1d73b (HEAD -> master, origin/master)
Author: skyreaper925 <volodinmaxim1995@gmail.com>
Date:   Thu Dec 4 15:48:17 2025 +0300

    Add dirty hello.py

commit 875402118d08da235e694944554374d63f03dcfc
Author: skyreaper925 <volodinmaxim1995@gmail.com>
Date:   Thu Dec 4 15:23:55 2025 +0300

    Initial commit: add empty README.md
``` 
12. Создаю ветку patch1 и меняю код в файле на код из задания
```
PS C:\Users\user\lanit_labs> git checkout -b patch1
Switched to a new branch 'patch1'
PS C:\Users\user\lanit_labs> git add hello.py
```
Делаю снимок
```
PS C:\Users\user\lanit_labs> git commit -S -m "modernize with Typer CLI"
[patch1 7de3777] modernize with Typer CLI
 1 file changed, 17 insertions(+), 4 deletions(-)
```
Отправляю на сервер
```
PS C:\Users\user\lanit_labs> git push -u origin patch1
Enter passphrase for key '/c/Users/user/.ssh/id_ed25519':
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 1.12 KiB | 383.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote:
remote: Create a pull request for 'patch1' on GitHub by visiting:
remote:      https://github.com/skyreaper925/lanit_labs/pull/new/patch1
remote:
To github.com:skyreaper925/lanit_labs.git
 * [new branch]      patch1 -> patch1
branch 'patch1' set up to track 'origin/patch1'.
```

## Часть 2
1. Проверяю на сайте, что новая ветка появилась
2. Создаю pull-request в виде patch1 -> master
```
PS C:\Users\user\lanit_labs> gh pr create --base master --head patch1 --title "modernize with Typer CLI" --body "Refactored script to use Typer library for CLI."

Creating pull request for patch1 into master in skyreaper925/lanit_labs

https://github.com/skyreaper925/lanit_labs/pull/1
```
3. Добавляю комментарии
```
PS C:\Users\user\lanit_labs> git add hello.py
```
Делаю снимок
```
PS C:\Users\user\lanit_labs> git commit -S -m "add code comments"
[patch1 63de800] add code comments
 1 file changed, 3 insertions(+), 2 deletions(-)
 ```
Отправляю на сервер
```
PS C:\Users\user\lanit_labs> git push -u origin patch1
Enter passphrase for key '/c/Users/user/.ssh/id_ed25519':
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 936 bytes | 234.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:skyreaper925/lanit_labs.git
   7de3777..63de800  patch1 -> patch1
branch 'patch1' set up to track 'origin/patch1'.
```
4. Выполняю слияние pull-request для patch1 -> master и удаляю ветку patch1
```
✓ Merged pull request skyreaper925/lanit_labs#1 (modernize with Typer CLI)
Enter passphrase for key '/c/Users/user/.ssh/id_ed25519':
remote: Enumerating objects: 1, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 1 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (1/1), 903 bytes | 75.00 KiB/s, done.
From github.com:skyreaper925/lanit_labs
 * branch            master     -> FETCH_HEAD
   e83d795..8872fd3  master     -> origin/master
Updating e83d795..8872fd3
Fast-forward
 hello.py | 22 ++++++++++++++++++----
 1 file changed, 18 insertions(+), 4 deletions(-)
✓ Deleted local branch patch1 and switched to branch master
✓ Deleted remote branch patch1
```
5. Смотрим историю изменений
```
PS C:\Users\user\lanit_labs> git checkout master
Already on 'master'
Your branch is up to date with 'origin/master'.
PS C:\Users\user\lanit_labs> git pull origin master
Enter passphrase for key '/c/Users/user/.ssh/id_ed25519':
From github.com:skyreaper925/lanit_labs
 * branch            master     -> FETCH_HEAD
Already up to date.
PS C:\Users\user\lanit_labs> git log --oneline --graph --all
*   8872fd3 (HEAD -> master, origin/master) Merge pull request #1 from skyreaper925/patch1
|\
| * 63de800 (origin/patch1) add code comments
| * 7de3777 modernize with Typer CLI
|/
* e83d795 Add dirty hello.py
* 8754021 Initial commit: add empty README.md
```
6. Удаляем ветку
```
PS C:\Users\user\lanit_labs> git branch -d patch1
error: branch 'patch1' not found
```
7. Создайте новую локальную ветку patch2
```
PS C:\Users\user\lanit_labs> git checkout -b patch2
Switched to a new branch 'patch2'
```
8. Меняю стиль, имена и проч.
```
PS C:\Users\user\lanit_labs> git add hello.py
```
9. Публикация и запрос как и ранее
```
PS C:\Users\user\lanit_labs> git commit -S -m "refactor: improve code style"
[patch2 8f03783] refactor: improve code style
 1 file changed, 16 insertions(+), 11 deletions(-)
PS C:\Users\user\lanit_labs> git push -u origin patch2
Enter passphrase for key '/c/Users/user/.ssh/id_ed25519':
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 1.12 KiB | 229.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote:
remote: Create a pull request for 'patch2' on GitHub by visiting:
remote:      https://github.com/skyreaper925/lanit_labs/pull/new/patch2
remote:
To github.com:skyreaper925/lanit_labs.git
 * [new branch]      patch2 -> patch2
branch 'patch2' set up to track 'origin/patch2'.
PS C:\Users\user\lanit_labs> gh pr create --base master --head patch2 --title "Refactoring" --body "Improved naming, formatting."

Creating pull request for patch2 into master in skyreaper925/lanit_labs

https://github.com/skyreaper925/lanit_labs/pull/2
```
10. Явно меняю комментарий в хозяйской ветке через веб-интерфейс GitHub. Делаю снимок прямо в master
11. На вкладке запросов вижу автоматически неликвидируемые расхождения
12. Делаю rebase
```
PS C:\Users\user\lanit_labs> git checkout patch2
Already on 'patch2'
Your branch is up to date with 'origin/patch2'.
PS C:\Users\user\lanit_labs> git fetch origin
Enter passphrase for key '/c/Users/user/.ssh/id_ed25519':
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 962 bytes | 25.00 KiB/s, done.
From github.com:skyreaper925/lanit_labs
   8872fd3..a6c8e0d  master     -> origin/master
PS C:\Users\user\lanit_labs> git rebase origin/master
Auto-merging hello.py
CONFLICT (content): Merge conflict in hello.py
error: could not apply 8f03783... refactor: improve code style
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
hint: Disable this message with "git config advice.mergeConflict false"
Could not apply 8f03783... refactor: improve code style
```
Вручную исправляю в файле и добавляю его
```
PS C:\Users\user\lanit_labs> git add hello.py
PS C:\Users\user\lanit_labs> git rebase --continue --m
```
13. Затем делаю снимок и отправку
```
PS C:\Users\user\lanit_labs> git commit -S -m "conflict demolishing"
[detached HEAD 1f89b01] conflict demolishing
 1 file changed, 15 insertions(+), 11 deletions(-)
PS C:\Users\user\lanit_labs> git push --force-with-lease origin patch2
Enter passphrase for key '/c/Users/user/.ssh/id_ed25519':
Everything up-to-date
```
14. Убеждаюсь, что конфликты пропали
15. Делаю слияние
```
PS C:\Users\user\lanit_labs> gh pr merge patch2 --merge --delete-branch --auto
✓ Merged pull request skyreaper925/lanit_labs#2 (Refactoring)
Enter passphrase for key '/c/Users/user/.ssh/id_ed25519':
remote: Enumerating objects: 1, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 1 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (1/1), 896 bytes | 81.00 KiB/s, done.
From github.com:skyreaper925/lanit_labs
 * branch            master     -> FETCH_HEAD
   a6c8e0d..3aae027  master     -> origin/master
Updating 8872fd3..3aae027
Fast-forward
 hello.py | 30 ++++++++++++++++++------------
 1 file changed, 18 insertions(+), 12 deletions(-)
 ```

## Эпилог
 Истории локальных снимков приведены здесь, а удалённых в моём репо на сайте
 
**Smimesign** - утилита для подписи S/MIME, совместимая с Git.
Она позволяет разработчикам подписывать снимки и теги Git с использованием сертификатов X.509, выпущенных 
публичными или внутренними центрами сертификации.
Именно она меня сегодня взбесила, когда надо было постоянно вводить пароль при каждом снимке и отправке