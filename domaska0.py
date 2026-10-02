class Employee:
    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self) -> str:
        return f"Заробітна плата {self.name}: {self.salary} {self.position}"


if __name__ == "__main__":

    employee1 = Employee(name="Тарас", position="Босс", salary=99999999)
    print(employee1.get_salary_info())