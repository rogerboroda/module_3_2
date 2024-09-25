def send_email(message, recipient, sender = "university.help@gmail.com"):
     if '@' not in recipient or '@' not in sender or not \
             recipient.endswith((".com", ".ru", ".net")) or not \
             sender.endswith((".com", ".ru", ".net")):
          print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
     elif recipient == sender:
          print("Нельзя отправить письмо самому себе!")
     elif sender == "university.help@gmail.com":
          print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
     elif sender != "university.help@gmail.com":
          print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')



# Вывод на консоль:
# Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
# НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
# Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
# Нельзя отправить письмо самому себе!