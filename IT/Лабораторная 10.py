from datetime import date
def turn_to_date(st):
    return date(int(st[6:]), int(st[3:5]), int(st[:2]))


class Document:
    def __init__(self, number, name, content, start_date:date, finish_date:date, person):
        self.number = number
        self.name = name
        self.content = content
        self.start_date = turn_to_date(start_date)
        self.finish_date = turn_to_date(finish_date)
        self.person = person
    def __str__(self):
        return f" {self.name}: №{self.number} от {self.start_date} до {self.finish_date} ({self.person}) -- {self.content}"

class DocumentList:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return (f"Список документов: {self.list}")

    def add_to_list(self,task):
        self.list.append(task)

    def show_by_name(self, name):
        display = []
        for document in self.list:
            if document.person == str(name):
                display.append(document)
        return display

    def show_by_date(self, st, fn):
        display = []
        for document in self.list:
            if  turn_to_date(st)<= document.start_date <= turn_to_date(fn):
                display.append(document)
        return display


document_1 = Document("1", "Поручение","Провести А-В тестирование","12.10.2025","15.10.2025","Иванов А.А.")
document_2 = Document("2", "Поручение","Провести data cleaning","10.11.2025","12.12.2025","Иванов А.А.")
document_3 = Document("3", "Поручение","Объяснить гипотезу","12.10.2025","12.10.2025","Петров А.А.")
document_4 = Document("4", "Поручение","Провести А-В тестирование","08.08.2025","01.01.2026","Петров А.В.")
document_5 = Document("5", "Поручение","Провести А-В тестирование","22.11.2025","13.11.2025","Иванов А.А.")
document_6 = Document("6", "Поручение","Подготовить датасет","14.02.2026","22.10.2026","Богданов А.А.")
document_7 = Document("7", "Поручение","Обучить модель","02.07.2024","13.07.2024","Иванов А.А.")
document_8 = Document("8", "Поручение","Обучить модель","12.10.2025","13.10.2025","Богданов А.А.")
document_9 = Document("9", "Поручение","Провести тест модели","11.05.2024","23.06.2024","Петров А.А.")
document_10 = Document("10", "Поручение","Провести валидацию модели","12.10.2025","13.10.2025","Иванов А.А.")

list_for_person = []

documents = DocumentList(list_for_person)


documents.add_to_list(document_1)
documents.add_to_list(document_2)
documents.add_to_list(document_3)
documents.add_to_list(document_4)
documents.add_to_list(document_5)
documents.add_to_list(document_6)
documents.add_to_list(document_7)
documents.add_to_list(document_8)
documents.add_to_list(document_9)
documents.add_to_list(document_10)

answers = documents.show_by_name(input("Введите ФИО: "))
for answer in answers:
    print(answer)
print("\n" + "-"*100 + "\n")

start_date = input("Введите начальную дату: (вида ДД.ММ.ГГГГ) ")
finish_date = input("Введите конечную дату: (вида ДД.ММ.ГГГГ) ")
dates = documents.show_by_date(start_date, finish_date)
for event in dates:
    print(event)






