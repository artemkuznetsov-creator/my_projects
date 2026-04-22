import re
data = input("Введите текст: ")
result = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9_.+-]+', data)
print(result)

'''
Здравствуйте! Мои контактные данные для связи: Основной: ivan.petrov@example.ru Дубль: admin@site..ru (ошибка) Также есть старый ящик: ivan1985@old-service.ru Служебный: ivan.petrov@departament.gosuslugi.ru Запасной: temp-email@temp.co Неверный: @missinglogin.ru
'''