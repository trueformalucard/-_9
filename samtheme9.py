class Tomato:
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зеленый', 3: 'красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        """Переводит томат на следующую стадию созревания"""
        if self._state < 3:
            self._state += 1
            print(f"Томат {self._index} перешел в стадию '{self.states[self._state]}'")
        else:
            print(f"Томат {self._index} уже полностью созрел!")

    def is_ripe(self):
        """Проверяет, созрел ли томат"""
        return self._state == 3


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(num_tomatoes)]
    def grow_all(self):
        """Переводит все томаты на следующую стадию созревания"""
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        """Проверяет, все ли томаты созрели"""
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        """Очищает список томатов после сбора урожая"""
        self.tomatoes = []
        print("Урожай собран! Список томатов очищен.")


class Gardener:
    @staticmethod
    def knowledge_base():
        """Выводит справку по садоводству"""
        print("Справка по садоводству:")
        print("- Садовник ухаживает за кустом томатов")
        print("- Томаты проходят стадии: отсутствует → цветение → зеленый → красный")
        print("- Собирать урожай можно только когда все томаты красные")
        print()

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        """Садовник работает - ухаживает за растением"""
        print(f"{self.name} ухаживает за растением...")
        self._plant.grow_all()

    def harvest(self):
        """Сбор урожая, если все томаты созрели"""
        if self._plant.all_are_ripe():
            print(f"{self.name} собирает урожай! Все томаты созрели.")
            self._plant.give_away_all()
            return True
        else:
            print(f"{self.name}: Томаты еще не созрели! Нужно продолжать ухаживать.")
            return False



if __name__ == "__main__":
    Gardener.knowledge_base()

    bush = TomatoBush(3)
    gardener = Gardener("Василий", bush)

    print("Создан куст с 3 томатами и садовник Василий")
    print("=" * 50)


    print("Первый день:")
    gardener.work()
    print()


    print("Попытка сбора урожая:")
    gardener.harvest()
    print()


    print("Второй день:")
    gardener.work()
    print()

    print("Третий день:")
    gardener.work()
    print()

    print("Финальная попытка сбора:")
    gardener.harvest()