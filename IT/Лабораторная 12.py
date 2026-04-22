from abc import ABC, abstractmethod

class YoungMan(ABC):
    def __init__(self, name, age, military):
        self._name = name
        self._age = age
        self._military = military
        self._contract = False
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age
    def set_age(self, age):
        self._age = age

    def get_military(self):
        return self._military
    def set_military(self, military):
        self._military = military
    @abstractmethod
    def contract(self):
        pass
    @abstractmethod
    def medical_examination(self):
        pass

class Student(YoungMan):
    def __init__(self, name, age, grade, military="не годен"):
        super().__init__(name, age, military)
        self._grade = grade
        self._military = military

    def medical_examination(self):
        if self._grade < 3:
            self._military = "годен"
        else:
            self._military = "не годен"

    def contract(self):
        if self._military == "годен":
            self._contract = True
            print(f"{self._name} заключил контракт")

class Soldier(YoungMan):
    def __init__(self, name, age, health_issues, military="годен"):
        super().__init__(name, age, military)
        self._health_issues = health_issues
        self._military = military

    def medical_examination(self):
        if self._health_issues == "нет":
            self._military = "подтверждена годность"
        else:
            self._military = "не годен"

    def contract(self):
        if self._military == "подтверждена годность":
            self._contract = True
            print(f"{self._name} заключил контракт повторно")

class Serve(YoungMan):
    def __init__(self, name, age, time_left, military="годен"):
        super().__init__(name, age, military)
        self._time_left = time_left
        self._military = military

    def medical_examination(self):
        if self._time_left > 5:
            self._military = "подтверждена годность"
        else:
            self._military = "не годен"

    def contract(self):
        if self._military == "подтверждена годность":
            self._contract = True
            print(f"{self._name} заключил контракт")

class PeopleDB:
    def __init__(self):
        self.people = []
    def add_person(self, person):
        self.people.append(person)
    def __str__(self):
        result = ""
        for person in self.people:
            result += f"{person.get_name()}. {person.get_age()} лет. {person.get_military()}\n"
        return result
person1 = Student('Водолаз Владимир',18,2)
person2 = Student('Сенчихин Илья', 18, 5)
person3 = Soldier('Иванов Иван', 25, 'нет')
person4 = Soldier('Денисов Денис', 21, 'плоскостропие')
person5 = Serve('Петров Петр',25, 6)

military_data = PeopleDB()
military_data.add_person(person1)
military_data.add_person(person2)
military_data.add_person(person3)
military_data.add_person(person4)
military_data.add_person(person5)

print(military_data)

for person in military_data.people:
    person.medical_examination()

print(military_data)

for person in military_data.people:
    if person.get_military() == 'годен'\
            or person.get_military() == 'подтверждена годность':
        person.contract()







