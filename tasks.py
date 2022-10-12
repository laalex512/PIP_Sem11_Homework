
# from operator import contains


class Person:

    def __init__(self, name, surName, lastName, phoneDict):
        self.name = name
        self.surName = surName
        self.lastName = lastName
        self.phoneDict = phoneDict

    def getPhone(self):
        return self.phoneDict.get("private")

    def getName(self):
        return self.lastName + " " + self.name + " " + self.surName

    def getWorkPhone(self):
        return self.phoneDict.get("work")

    def getSmsText(self):
        return f"Уважаемый {self.name} {self.surName}! Примите участие в акции!"


class Company:

    def __init__(self, nameComp, typeComp, phoneDict, *person):
        self.nameComp = nameComp
        self.typeComp = typeComp
        self.phoneDict = phoneDict
        self.personList = []
        for i in person:
            self.personList.append(i)

    def getPhone(self):
        contact = self.phoneDict.get("contact")
        if not contact:
            for i in self.personList:
                contact = i.getWorkPhone()
                if contact:
                    break
        return contact

    def getName(self):
        return self.nameComp

    def getSmsText(self):
        return f"Для компании {self.nameComp} есть предложение! Примите участие в акции для {self.typeComp}"


def sendSms(*client):
    messageList = []
    for i in client:
        if i.getPhone():
            messageList.append(
                f"Отправлено смс на номер {i.getPhone()}:  {i.getSmsText()}")
        else:
            messageList.append(f"Не удалось отправить сообщение {i.getName()}")
    for i in messageList:
        print(i)


# person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
# person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
# person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
# person4 = Person("John", "Unknown", "Doe", {})
# company1 = Company("Bell", "OOO", {"contact": 111}, person3, person4)
# company2 = Company("Cell", "AO", {"non_contact": 222}, person2, person3)
# company3 = Company("Dell", "Ltd", {"non_contact": 333})

person1 = Person("Stepan", "Petrovich", "Jobsov", {"private": 555})
person2 = Person("Borya", "Ivanovich", "Gaitsov",
                 {"private": 777, "work": 888})
person3 = Person("Semen", "Robertovich", "Vozniackiy", {"work": 789})
person4 = Person("Leonid", "Arsenovich", "Torvaldson", {})
company1 = Company("Apple", "OOO", {"contact": 111}, person1, person3)
company2 = Company("PlastOkno", "AO", {"non_contact": 222}, person2)
company3 = Company("PingvinFarm", "Ltd", {"non_contact": 333}, person4)

sendSms(person1, person2, person3, person4, company1, company2, company3)
