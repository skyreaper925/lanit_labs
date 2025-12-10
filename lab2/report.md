# Отчёт по лабораторной  работе 2
### Володин Максим

1. Анализируем команды
```
PS C:\Users\user> quser | Measure-Object -Line

Lines Words Characters Property
----- ----- ---------- --------
    2

PS C:\Users\user> id
uid=0(user) gid=0
PS C:\Users\user> whoami
ram\user
PS C:\Users\user> hostname
RAM
```
2. Долго выводим все вложенности утилитой дерева.
Затем используем  ls -a и ls -l.
Отличие между ними в том, что -a показывает просто имена, а -l (long) ещё и дополнительную информацию
3. Выводим команду для определения файловой системы на разделе
```
PS C:\Users\user> df
C:\Program Files (x86)\Gow\bin\df.exe: cannot read table of mounted file systems: Invalid argument
PS C:\Users\user> wmic logicaldisk get caption,description,filesystem
Caption  Description       FileSystem
C:       Local Fixed Disk  NTFS


```
4. Выполняем команды и анализируем ответы

```
PS C:\Users\user> which vi
C:\Program Files (x86)\Gow\bin\which.exe: no vi in (.;
C:\Program Files\PowerShell\7;
C:\Program Files\Common Files\Oracle\Java\javapath;
C:\WINDOWS\system32;
C:\WINDOWS;
C:\WINDOWS\System32\WindowsPowerShell\v1.0\;
C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;
C:\WINDOWS\system32;
C:\WINDOWS;
C:\WINDOWS\System32\Wbem;
C:\WINDOWS\System32\WindowsPowerShell\v1.0\;
C:\Program Files\Git\cmd;
C:\Program Files\NVIDIA Corporation\NVIDIA app\NvDLISR;
C:\Program Files\PowerShell\7\;
C:\Program Files\GitHub CLI\;
C:\Program Files (x86)\Gow\bin;
C:\Program Files (x86)\gnupg\bin;
C:\Users\user\AppData\Local\Microsoft\WindowsApps;
C:\Users\user\AppData\Local\Programs\MiKTeX\miktex\bin\x64\;
C:\Program Files\Graphviz\bin;
C:\adb)
```
```
PS C:\Users\user> Get-ChildItem -Path C:\ -Filter "hello.py" -Recurse -ErrorAction SilentlyContinue
    
    Directory: C:\Users\user\lanit_labs

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          04.12.2025    18:03            709 hello.py
```
```
PS C:\Users\user> sudo updatedb
Sudo отключен на этом компьютере. 
Чтобы включить его, перейдите в раздел Developer Settings page в приложении "Параметры"
```
```
PS C:\Users\user> Get-ChildItem -Path C:\ -Filter "hello" -Recurse -ErrorAction SilentlyContinue

    Directory: C:\Program Files\Git\mingw64\lib\tk8.6\demos

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          02.05.2024    19:05            511 hello
```
Команда echo $null > screen создаёт файл "touch" без ответа
```
PS C:\Users\user> Get-ChildItem -Path $HOME -Filter "screen" -Recurse -ErrorAction SilentlyContinue

    Directory: C:\Users\user

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          10.12.2025     1:32              0 screen

```
```
PS C:\Users\user> Get-ChildItem -Path C:\ -Filter "screen" -Recurse -ErrorAction SilentlyContinue

    Directory: C:\Program Files\Git\usr\lib\terminfo\73

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          02.05.2024    19:05           1607 screen

    Directory: C:\Program Files\Git\usr\share\terminfo\73

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          02.05.2024    19:05           1607 screen

    Directory: C:\Users\user

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          10.12.2025     1:32              0 screen

    Directory: C:\Windows\Web

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-r--          01.04.2024    10:26                Screen
```
Во-первых, команды sudo updated не существует, 
а во-вторых в Windows поиск индексируется автоматически и подобные команды не нужны

Повторный вывод аналога locate screen дал тот же ответ
5. Делаем снимок и отправку
6. Выполняем команды и анализируем ответы
```
PS C:\Users\user> net user user
Имя пользователя                       user
Полное имя                             Максим Володин
Комментарий
Комментарий пользователя
Код страны или региона                 000 (Стандартный системный)
Учетная запись активна                 Yes
Учетная запись просрочена              Никогда

Последний пароль задан                 10.04.2023 2:25:53
Действие пароля завершается            Никогда
Пароль допускает изменение             10.04.2023 2:25:53
Требуется пароль                       No
Пользователь может изменить пароль     Yes

Разрешенные рабочие станции            Все
Сценарий входа
Конфигурация пользователя
Основной каталог
Последний вход                         10.04.2023 2:25:52

Разрешенные часы входа                 Все

Членство в локальных группах           *Администраторы
Членство в глобальных группах          *Отсутствует
Команда выполнена успешно.
```
```
PS C:\Windows\System32> net user smallman /add
Команда выполнена успешно.
```
```
PS C:\Windows\System32> Remove-LocalUser -Name "smallman"
PS C:\Windows\System32> $userPath = "C:\Users\smallman"
PS C:\Windows\System32> if (Test-Path $userPath) {
    Remove-Item -Path $userPath -Recurse -Force -ErrorAction SilentlyContinue
}
```
```
PS C:\Windows\System32> net user smallman /add
Команда выполнена успешно.
```
```
PS C:\Windows\System32> net user smallman *
Введите пароль для пользователя:
Повторите ввод пароля для подтверждения:
Команда выполнена успешно.
```
```
PS C:\Windows\System32> Set-LocalUser -Name "smallman" 
-Description "Hach Hachov Hacherovich,239,45-67,499-239-45-33"
```
```
PS C:\Windows\System32> net user smallman *
Введите пароль для пользователя:
Повторите ввод пароля для подтверждения:
Команда выполнена успешно.
```
``` 
PS C:\Users\user\PycharmProjects\lanit_labs\lab2> whoami /groups

Сведения о группах
-----------------

Группа                                                               Тип                     SID                                                                                                           Атрибуты                                                     
==================================================================== ======================= ============================================================================================================= =============================================================
Обязательная метка\Средний обязательный уровень                      Метка                   S-1-16-8192                                                                                                                                                                
Все                                                                  Хорошо известная группа S-1-1-0                                                                                                       Обязательная группа, Включены по умолчанию, Включенная группа
NT AUTHORITY\Локальная учетная запись и член группы "Администраторы" Хорошо известная группа S-1-5-114                                                                                                     Группа, используемая только для запрета                      
BUILTIN\Администраторы                                               Псевдоним               S-1-5-32-544                                                                                                  Группа, используемая только для запрета                      
BUILTIN\Пользователи                                                 Псевдоним               S-1-5-32-545                                                                                                  Обязательная группа, Включены по умолчанию, Включенная группа
NT AUTHORITY\ИНТЕРАКТИВНЫЕ                                           Хорошо известная группа S-1-5-4                                                                                                       Обязательная группа, Включены по умолчанию, Включенная группа
КОНСОЛЬНЫЙ ВХОД                                                      Хорошо известная группа S-1-2-1                                                                                                       Обязательная группа, Включены по умолчанию, Включенная группа
NT AUTHORITY\Прошедшие проверку                                      Хорошо известная группа S-1-5-11                                                                                                      Обязательная группа, Включены по умолчанию, Включенная группа
NT AUTHORITY\Данная организация                                      Хорошо известная группа S-1-5-15                                                                                                      Обязательная группа, Включены по умолчанию, Включенная группа
MicrosoftAccount\volodinmaxim1995@gmail.com                          Пользователь            S-1-11-96-3623454863-58364-18864-2661722203-1597581903-2115156820-4294215291-1466442587-2335343980-3061770256 Обязательная группа, Включены по умолчанию, Включенная группа
NT AUTHORITY\Локальная учетная запись                                Хорошо известная группа S-1-5-113                                                                                                     Обязательная группа, Включены по умолчанию, Включенная группа
ЛОКАЛЬНЫЕ                                                            Хорошо известная группа S-1-2-0                                                                                                       Обязательная группа, Включены по умолчанию, Включенная группа
NT AUTHORITY\Проверка подлинности учетной записи в облаке            Хорошо известная группа S-1-5-64-36                                                                                                   Обязательная группа, Включены по умолчанию, Включенная группа
```
```
PS C:\Windows\System32> New-LocalGroup -Name "readgroup"

Name      Description
----      -----------
readgroup

```
Команда Add-LocalGroupMember -Group "readgroup" -Member "smallman" выполнилась без ответа
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab2> icacls screen /grant *S-1-1-0:F
обработанный файл: screen                        
Успешно обработано 1 файлов; не удалось обработать 0 файлов
```
7. Выводим группу прав
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab2> icacls screen
screen Все:(F)
       NT AUTHORITY\СИСТЕМА:(I)(F)
       BUILTIN\Администраторы:(I)(F)
       RAM\user:(I)(F)

Успешно обработано 1 файлов; не удалось обработать 0 файлов
```
Удаляем все наследованные права
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab2> icacls screen /inheritance:r
обработанный файл: screen
Успешно обработано 1 файлов; не удалось обработать 0 файлов
```
Удаляем всех пользователей
```
 PS C:\Users\user\PycharmProjects\lanit_labs\lab2> icacls screen /remove Everyone
Успешно обработано 0 файлов; не удалось обработать 0 файлов
(.venv) PS C:\Users\user\PycharmProjects\lanit_labs\lab2> icacls screen /remove Users
Успешно обработано 0 файлов; не удалось обработать 0 файлов
(.venv) PS C:\Users\user\PycharmProjects\lanit_labs\lab2> icacls screen /remove "Аутентифицированные пользователи"
Успешно обработано 0 файлов; не удалось обработать 0 файлов
```
Добавляем только smallman с правами чтения
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab2> icacls screen /grant smallman:R
обработанный файл: screen
Успешно обработано 1 файлов; не удалось обработать 0 файлов
```
Добавляем группу readgroup с правами чтения
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab2> icacls screen /grant readgroup:R
обработанный файл: screen
Успешно обработано 1 файлов; не удалось обработать 0 файлов

```
Проверяем результат
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab2> icacls screen
screen RAM\readgroup:(R)
       RAM\smallman:(R)
       Все:(F)

Успешно обработано 1 файлов; не удалось обработать 0 файлов
```
8. Команда touch nmapres.txt была выполнена тихо.
В папке появился файл

Даём права пользователю smallman
```shell
PS C:\Users\user\PycharmProjects\lanit_labs\lab2> icacls nmapres.txt /grant smallman:RW
обработанный файл: nmapres.txt
Успешно обработано 1 файлов; не удалось обработать 0 файлов
```
Теперь права группе readgroup
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab2> icacls nmapres.txt /grant readgroup:R
обработанный файл: nmapres.txt
```
Смотрим все права
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab2> icacls nmapres.txt
nmapres.txt RAM\readgroup:(R)
            RAM\smallman:(R,W)
            NT AUTHORITY\СИСТЕМА:(I)(F)
            BUILTIN\Администраторы:(I)(F)
            RAM\user:(I)(F)

Успешно обработано 1 файлов; не удалось обработать 0 файлов
 ```
9. Файл уже сохранён, дополнительных действий не требуется
10. Вывожу все локальные группы
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab2> Get-LocalGroup | Format-Table Name, Description

Name                                            Description                                                                                                                        
----                                            -----------                                                                                                                        
readgroup                                                                                                                                                                          
IIS_IUSRS                                       Встроенная группа, которую используют службы IIS.                                                                                  
Администраторы                                  Администраторы имеют полные, ничем не ограниченные права доступа к компьютеру или домену                                           
Администраторы Hyper-V                          Члены этой группы имеют полный и неограниченный доступ ко всем функциям Hyper-V.                                                   
Владельцы устройства                            Члены этой группы могут изменять параметры на уровне системы.                                                                      
Гости                                           Гости по умолчанию имеют те же права, что и пользователи, за исключением учетной записи "Гость", еще более ограниченной в правах.  
Криптографические операторы                     Членам разрешено выполнение операций криптографии.                                                                                 
Операторы архива                                Операторы архива могут переопределять ограничения доступа только в целях копирования и восстановления файлов                       
Операторы настройки сети                        Члены этой группы могут иметь некоторые административные права для управления настройкой сетевых параметров                        
Операторы оборудования пользовательского режима Участники этой группы могут работать с оборудованием в пользовательском режиме.                                                    
Операторы помощи по контролю учетных записей    Члены этой группы могут удаленно запрашивать атрибуты авторизации и разрешения для ресурсов на данном компьютере.                  
Опытные пользователи                            Категория опытных пользователей оставлена для обратной совместимости и обладает ограниченными административными правами            
Пользователи                                    Пользователи не имеют прав на изменение параметров системы и могут запускать большинство приложений                                
Пользователи DCOM                               Члены этой группы могут запускать, активизировать и использовать объекты DCOM на этом компьютере.                                  
Пользователи OpenSSH                            Члены этой группы могут подключаться к этому компьютеру с помощью SSH.                                                             
Пользователи журналов производительности        Члены этой группы могут планировать ведение журнала счетчиков производительности, включать поставщиков трассировки и собирать тр...
Пользователи системного монитора                Члены данной группы имеют как местный, так и удаленный доступ к счетчику производительности                                        
Пользователи удаленного рабочего стола          Члены этой группы имеют право на выполнение удаленного входа                                                                       
Пользователи удаленного управления              Члены этой группы могут получать доступ к ресурсам инструментария WMI по протоколам управления (таким как WS-Management в службе...
Репликатор                                      Поддержка репликации файлов в домене                                                                                               
Управляемая системой группа учетных записей     Члены этой группы управляются системой.                                                                                            
Читатели журнала событий                        Члены этой группы могут читать журналы событий с локального компьютера                                                             
```
Вывожу права на каталоги верхнего уровня для диска C:\
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab2> Get-Acl C:\ | Format-List


Path   : Microsoft.PowerShell.Core\FileSystem::C:\
Owner  : NT SERVICE\TrustedInstaller
Group  : NT SERVICE\TrustedInstaller
Access : NT AUTHORITY\Прошедшие проверку Allow  AppendData
         NT AUTHORITY\Прошедшие проверку Allow  -536805376
         NT AUTHORITY\СИСТЕМА Allow  FullControl
         BUILTIN\Администраторы Allow  FullControl
         BUILTIN\Пользователи Allow  ReadAndExecute, Synchronize
         S-1-15-3-65536-1888954469-739942743-1668119174-2468466756-4239452838-1296943325-355587736-700089176 Allow  ReadData, ExecuteFile, ReadAttributes, Synchronize
Audit  : 
Sddl   : O:S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464G:S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464D:(A;;LC;;;AU)(A;OICIIO;SDGXGWGR;;;AU)(A;O
         ICI;FA;;;SY)(A;OICI;FA;;;BA)(A;OICI;0x1200a9;;;BU)(A;;0x1000a1;;;S-1-15-3-65536-1888954469-739942743-1668119174-2468466756-4239452838-1296943325-355587736-700089176)
```
И для всех корневых каталогов на всех дисках
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab2> Get-PSDrive -PSProvider FileSystem | ForEach-Object {
>>     $root = $_.Root
>>     Write-Host "=== Права для $root ===" -ForegroundColor Green
>>     try {
>>         Get-Acl $root | Select-Object -ExpandProperty Access | 
>>         Format-Table IdentityReference, FileSystemRights, AccessControlType -AutoSize
>>     } catch {
>>         Write-Host "Нет доступа к $root" -ForegroundColor Red
>>     }
>>     Write-Host ""
>> }
=== Права для C:\ ===

IdentityReference                                                                                                                     FileSystemRights AccessControlType
-----------------                                                                                                                     ---------------- -----------------
NT AUTHORITY\Прошедшие проверку                                                                                                             AppendData             Allow
NT AUTHORITY\Прошедшие проверку                                                                                                             -536805376             Allow
NT AUTHORITY\СИСТЕМА                                                                                                                       FullControl             Allow
BUILTIN\Администраторы                                                                                                                     FullControl             Allow
BUILTIN\Пользователи                                                                                                       ReadAndExecute, Synchronize             Allow
S-1-15-3-65536-1888954469-739942743-1668119174-2468466756-4239452838-1296943325-355587736-700089176 ReadData, ExecuteFile, ReadAttributes, Synchronize             Allow
```
Более подробно для основных каталогов
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab2> $topDirs = @("C:\", "C:\Program Files", "C:\Program Files (x86)", "C:\Users", "C:\Windows")
(.venv) PS C:\Users\user\PycharmProjects\lanit_labs\lab2> foreach ($dir in $topDirs) {
>>     if (Test-Path $dir) {
>>         Write-Host "=== $dir ===" -ForegroundColor Yellow
>>         Get-Acl $dir | Select-Object -ExpandProperty Access | 
>>         Where-Object { $_.IdentityReference -notlike "NT AUTHORITY\*" -and $_.IdentityReference -notlike "BUILTIN\*" } |
>>         Format-Table IdentityReference, FileSystemRights -AutoSize
>>         Write-Host ""
>>     }
>> }
=== C:\ ===

IdentityReference                                                                                                                     FileSystemRights
-----------------                                                                                                                     ----------------
S-1-15-3-65536-1888954469-739942743-1668119174-2468466756-4239452838-1296943325-355587736-700089176 ReadData, ExecuteFile, ReadAttributes, Synchronize



=== C:\Program Files ===

IdentityReference                                                      FileSystemRights
-----------------                                                      ----------------
СОЗДАТЕЛЬ-ВЛАДЕЛЕЦ                                                            268435456
NT SERVICE\TrustedInstaller                                                   268435456
NT SERVICE\TrustedInstaller                                                 FullControl
ЦЕНТР ПАКЕТОВ ПРИЛОЖЕНИЙ\ВСЕ ПАКЕТЫ ПРИЛОЖЕНИЙ              ReadAndExecute, Synchronize
ЦЕНТР ПАКЕТОВ ПРИЛОЖЕНИЙ\ВСЕ ПАКЕТЫ ПРИЛОЖЕНИЙ                              -1610612736
ЦЕНТР ПАКЕТОВ ПРИЛОЖЕНИЙ\ВСЕ ОГРАНИЧЕННЫЕ ПАКЕТЫ ПРИЛОЖЕНИЙ ReadAndExecute, Synchronize
ЦЕНТР ПАКЕТОВ ПРИЛОЖЕНИЙ\ВСЕ ОГРАНИЧЕННЫЕ ПАКЕТЫ ПРИЛОЖЕНИЙ                 -1610612736



=== C:\Program Files (x86) ===

IdentityReference                                                      FileSystemRights
-----------------                                                      ----------------
СОЗДАТЕЛЬ-ВЛАДЕЛЕЦ                                                            268435456
NT SERVICE\TrustedInstaller                                                   268435456
NT SERVICE\TrustedInstaller                                                 FullControl
ЦЕНТР ПАКЕТОВ ПРИЛОЖЕНИЙ\ВСЕ ПАКЕТЫ ПРИЛОЖЕНИЙ              ReadAndExecute, Synchronize
ЦЕНТР ПАКЕТОВ ПРИЛОЖЕНИЙ\ВСЕ ПАКЕТЫ ПРИЛОЖЕНИЙ                              -1610612736
ЦЕНТР ПАКЕТОВ ПРИЛОЖЕНИЙ\ВСЕ ОГРАНИЧЕННЫЕ ПАКЕТЫ ПРИЛОЖЕНИЙ ReadAndExecute, Synchronize
ЦЕНТР ПАКЕТОВ ПРИЛОЖЕНИЙ\ВСЕ ОГРАНИЧЕННЫЕ ПАКЕТЫ ПРИЛОЖЕНИЙ                 -1610612736



=== C:\Users ===

IdentityReference                                                                                                  FileSystemRights
-----------------                                                                                                  ----------------
Все                                                                                                                     -1610612736
Все                                                                                                     ReadAndExecute, Synchronize
S-1-15-3-65536-4045685566-1323397456-4055816110-285687253-194181-4019357623-1925838800-191844675 ReadData, ExecuteFile, Synchronize



=== C:\Windows ===

IdentityReference                                                      FileSystemRights
-----------------                                                      ----------------
СОЗДАТЕЛЬ-ВЛАДЕЛЕЦ                                                            268435456
NT SERVICE\TrustedInstaller                                                   268435456
NT SERVICE\TrustedInstaller                                                 FullControl
ЦЕНТР ПАКЕТОВ ПРИЛОЖЕНИЙ\ВСЕ ПАКЕТЫ ПРИЛОЖЕНИЙ              ReadAndExecute, Synchronize
ЦЕНТР ПАКЕТОВ ПРИЛОЖЕНИЙ\ВСЕ ПАКЕТЫ ПРИЛОЖЕНИЙ                              -1610612736
ЦЕНТР ПАКЕТОВ ПРИЛОЖЕНИЙ\ВСЕ ОГРАНИЧЕННЫЕ ПАКЕТЫ ПРИЛОЖЕНИЙ ReadAndExecute, Synchronize
ЦЕНТР ПАКЕТОВ ПРИЛОЖЕНИЙ\ВСЕ ОГРАНИЧЕННЫЕ ПАКЕТЫ ПРИЛОЖЕНИЙ                 -1610612736
```
11. Выводим все права для всех файлов и папок в текущей директории (без рекурсии)
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab2> Get-ChildItem -Force | ForEach-Object {
>>     Write-Host "=== $($_.Name) ===" -ForegroundColor Cyan
>>     try {
>>         $acl = Get-Acl $_.FullName
>>         $acl.Access | ForEach-Object {
>>             [PSCustomObject]@{
>>                 File = $_.Name
>>                 User = $_.IdentityReference
>>                 Rights = $_.FileSystemRights
>>                 Type = $_.AccessControlType
>>             }
>>         } | Format-Table User, Rights, Type -AutoSize
>>     } catch {
>>         Write-Host "Нет доступа" -ForegroundColor Red
>>     }
>>     Write-Host ""
>> }
=== exmpl_hello.py ===

User                        Rights  Type
----                        ------  ----
NT AUTHORITY\СИСТЕМА   FullControl Allow
BUILTIN\Администраторы FullControl Allow
RAM\user               FullControl Allow



=== nmapres.txt ===

User                                     Rights  Type
----                                     ------  ----
RAM\smallman           Write, Read, Synchronize Allow
RAM\readgroup                 Read, Synchronize Allow
NT AUTHORITY\СИСТЕМА                FullControl Allow
BUILTIN\Администраторы              FullControl Allow
RAM\user                            FullControl Allow



=== pygamesteel.py ===

User                        Rights  Type
----                        ------  ----
NT AUTHORITY\СИСТЕМА   FullControl Allow
BUILTIN\Администраторы FullControl Allow
RAM\user               FullControl Allow



=== README.md ===

User                        Rights  Type
----                        ------  ----
NT AUTHORITY\СИСТЕМА   FullControl Allow
BUILTIN\Администраторы FullControl Allow
RAM\user               FullControl Allow



=== report.md ===

User                        Rights  Type
----                        ------  ----
NT AUTHORITY\СИСТЕМА   FullControl Allow
BUILTIN\Администраторы FullControl Allow
RAM\user               FullControl Allow



=== screen ===

User                     Rights  Type
----                     ------  ----
Все                 FullControl Allow
RAM\smallman  Read, Synchronize Allow
RAM\readgroup Read, Synchronize Allow
```
Теперь только уникальные пользователи с их правами
```
PS C:\Users\user\PycharmProjects\lanit_labs\lab2> $allPermissions = @{}
(.venv) PS C:\Users\user\PycharmProjects\lanit_labs\lab2> Get-ChildItem -Force | ForEach-Object {
>>     $acl = Get-Acl $_.FullName -ErrorAction SilentlyContinue
>>     if ($acl) {
>>         $acl.Access | ForEach-Object {
>>             $key = "$($_.IdentityReference)"
>>             if (-not $allPermissions.ContainsKey($key)) {
>>                 $allPermissions[$key] = @()
>>             }
>>             $perm = "$($_.FileSystemRights) на $($_.Name)"
>>             if ($perm -notin $allPermissions[$key]) {
>>                 $allPermissions[$key] += $perm
>>             }
>>         }
>>     }
>> }
(.venv) PS C:\Users\user\PycharmProjects\lanit_labs\lab2> 
(.venv) PS C:\Users\user\PycharmProjects\lanit_labs\lab2> Write-Host "=== Сводка по пользователям и их правам ===" -ForegroundColor Green
=== Сводка по пользователям и их правам ===
(.venv) PS C:\Users\user\PycharmProjects\lanit_labs\lab2> $allPermissions.GetEnumerator() | Sort-Object Name | ForEach-Object {
>>     Write-Host "Пользователь: $($_.Key)" -ForegroundColor Yellow
>>     $_.Value | ForEach-Object { Write-Host "  - $_" }
>>     Write-Host ""
>> }
Пользователь: BUILTIN\Администраторы
  - FullControl на 

Пользователь: NT AUTHORITY\СИСТЕМА
  - FullControl на 

Пользователь: RAM\readgroup
  - Read, Synchronize на 

Пользователь: RAM\smallman
  - Write, Read, Synchronize на 
  - Read, Synchronize на 

Пользователь: RAM\user
  - FullControl на 

Пользователь: Все
  - FullControl на 
```
12. Вывожу все запущенные процессы.
Там их 266 штук

## Эпилог
В конце делаю снимок и отправку.
Много кода написано, отвечено, прав изменено.
Много чего переведено на Windows