class Worker:

    def __init__(self):
        self.salary = 0
        self.job = 0

    def take_salary(self, num):
        self.salary += num
        return self.salary


class Accountant():

    def __init__(self):
        pass

    def give_salary(self, worker):
        return worker.take_salary(1000*worker.job)

class Pupa(Worker):

    def __init__(self):
        super().__init__()

    def do_work(self, spisok1, spisok2):
        pupa_work = []
        for i in range(len(spisok1)):
            pupa_work.append(spisok1[i] + spisok2[i])
            self.job += 1
        return pupa_work
    
class Lupa(Worker):

    def __init__(self):
        super().__init__()

    def do_work(self, spisok1, spisok2):
        lupa_work = []
        for i in range(len(spisok1)):
            lupa_work.append(spisok1[i] - spisok2[i])
            self.job += 1
        return lupa_work