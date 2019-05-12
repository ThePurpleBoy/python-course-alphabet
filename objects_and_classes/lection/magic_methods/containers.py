import random
from typing import List


from lection.magic_methods.lifetime import Programmer


class ITCompany:
    members: List[Programmer]

    def __init__(self, name, years, members=None):
        self.name = name
        self.years = years
        self.members = members if members is not None else []
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.current < len(self.members):
            res = self.members[self.current]
            self.current += 1
            return res
        else:
            self.current = 0
            raise StopIteration

    def __contains__(self, item):
        return item in self.members


if __name__ == "__main__":
    names = ["Den", "Illya", "Alex", "Oksana", "Peter", "Vasya"]
    languages = ["Python", "PHP", "C++", "C#", "Java", "1C", "Go", "Ruby", "Rust", "R"]
    positions = ["trainee", "junior", "middle", "senior", "tech lead"]

    programmers = []

    for _ in range(5):
        programmer = Programmer(
            name=random.choice(names),
            language=random.choice(languages),
            position=random.choice(positions)
        )
        programmers.append(programmer)

    company = ITCompany(name="Ralabs", members=programmers, years=6)

    
