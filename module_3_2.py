def send_email(message, recipient, sender="university.help@gmail.com"):
    #проверка доменов
    correct_domain = ('.com', '.ru', '.net')
    #проверка на наличии корректной почты
    email_correct = sender.find("@"), recipient.find("@")
    valid = recipient.endswith(correct_domain, -4) == sender.endswith(correct_domain, -4)
    if email_correct:
        if valid is not True:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        elif recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        elif sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
