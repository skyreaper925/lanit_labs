## Задание

- [x] 1. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ who | wc -I
$ id
$ whoami
$ hostnamectl
```

- [x] 2. Выведите утилитой `tree` список вложенности дерева директорий для каталога своего пользователя.
Далее используйте `ls -a` и укажите отличие от `ls -l`.
- [x] 3. Используйте утилиту `file` и `df` для определения какая файловая система на разделе `/dev/sda1`.
- [x] 4. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ which vi
$ locate hello.py
$ sudo updatedb
$ locate hello
$ touch screen
$ find ~ -name screen
$ locate screen
$ sudo updated
$ locate screen
```

- [x]  5. Используйте конструкцию и вставьте ее в созданный файл ранее. 
Подключите `pygame` - используем исключительно для стилизации окна.

```py
import pygame
pygame.init()

# Устанавливаем размеры окна
screen_width = 800
screen_height = 600
window_size = (screen_width, screen_height)
pygame.display.set_mode(window_size) # Создаем окно

# Задаем цвет фона
bg_color = (255, 255, 255)
pygame.draw.rect(screen, bg_color, [0, 0, screen_width, screen_height], 1)

# Выводим текст на экран
font = pygame.font.SysFont(None, 75)
text = font.render("Hello appsec world*", True, (0, 255, 0))
text_rect = text.get_rect()
text_rect.center = (400, 300)
screen.blit(text, text_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
pygame.display.flip() # Обновляем экран
```

- [x] 6. Сделайте `commit` и `push` в свой репозиторий с изменениями в `master branch`. На следующих лабораторных 
  работах мы вернемся к этому файлу.
- [x] 7. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ groups
$ useradd smallman
$ userdel smallman -rf
$ useradd smallman
$ passwd smallman
$ usermod smallman -c 'Hach Hachov Hacherovich,239,45-67,499-239-45-33'
$ passwd smallman
$ id smallman
$ groupadd -g 1500 readgroup
$ usermod -aG readgroup smallman
$ chmod 666 screen 
```


- [x] 8. Выведите группу прав для `screen` и измените, что бы файл был доступен только для чтения созданному 
         пользователю и выведите права этого пользователя для измененного файла только используя `readgroup`.
- [x] 9. Используйте `POSIX ACL`. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ touch nmapres.txt
$ setfacl -m u:smallman:rw nmapres.txt
$ setfacl -m g:readgroup:r nmapres.txt
$ getfacl nmapres.txt
```

- [x] 10. Сохраните файл внутри локального репозитория, так как следующая работа будет подразумевать запись в нее 
  данных о nmap.
- [x] 11. Для закрепления выведите все списки групп пользователей на вашей ОС и права на каталоги верхнего уровня.
- [x] 12. Выведите все права для файлов и директорий локального репозитория которые имеют различные пользователи  
          (без использования длинных путей)
- [x] 13. Выведите процессы которые у вас запущены в термине и вне его.
- [x] 14. Оформить `README.md` по аналогии и использовать `shield`, etc.
- [x] 15. Составить `gist` отчёт и отправить ссылку личным сообщением

***