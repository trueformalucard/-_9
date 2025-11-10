# Тема 9.
Отчет по Теме #9 выполнил(а):
- Улыбышев Артемий Александрович
- ИВТ-23-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | +  | + | 
| Задание 2 | +  |
| Задание 3 | +  |
| Задание 4 | +  | 
| Задание 5 | +  |
знак "+" - задание выполнено; знак "-" - задание не выполнено;

## Самостоятельная работа №1
### Протестировать работу всех классов:

Вызвать справку

Создать объекты

Ухаживать за растениями

Пробовать собрать урожай раньше времени

Собрать урожай когда созреет 

```
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

```
### Результаты выполнения тестов.
![Меню](https://github.com/trueformalucard/-_9/blob/%D0%A2%D0%B5%D0%BC%D0%B0%2B9/1.png)
![Меню](https://github.com/trueformalucard/-_9/blob/%D0%A2%D0%B5%D0%BC%D0%B0%2B9/2.png)
![Меню](https://github.com/trueformalucard/-_9/blob/%D0%A2%D0%B5%D0%BC%D0%B0%2B9/3.png)
![Меню](https://github.com/trueformalucard/-_9/blob/%D0%A2%D0%B5%D0%BC%D0%B0%2B9/4.png)

## Выводы

states = {0: 'отсутствует', ...} - это общий для всех томатов список стадий созревания
self._index = index - у каждого томата свой уникальный номер
self._state = 0 - все томаты начинают с первой стадии "отсутствует"
[Tomato(i) for i in range(num_tomatoes)] - создаем несколько томатов с разными индексами
all(tomato.is_ripe() for tomato in self.tomatoes) - проверяем что ВСЕ томаты созрели
self.tomatoes = [] - просто очищаем список когда собираем урожай
@staticmethod - метод, который работает без создания объекта класса
self.name = name - имя садовника доступно извне
self._plant = plant - растение защищено от прямого доступа
Gardener.knowledge_base() - вызываем метод класса без создания объекта
gardener.work() и gardener.harvest() - проверяем взаимодействие между классами
Программа показывает весь процесс роста томатов от посадки до сбора урожая

## Лабораторная работа №1
### Создать класс для проверки имени. В свойствах указать только имя. В методе __init__() сделать проверку на угадывание имени. Показать что происходит при вызове атрибута, не указанного в классе.

```
class Ivan:
    __slots__ = ['name']
    
    def __init__(self, name):
        if name == 'Иван':
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, а Иван"

person1 = Ivan('Алексей')
person2 = Ivan('Иван')
print(person1.name)
print(person2.name)

person2.surname = 'Петров'

```
### Результат.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_9/theme9lab1.jpg)

## Выводы
__slots__ = ['name'] - ограничивает возможные атрибуты только именем
self.name = f"Да, я {name}" - устанавливает значение в зависимости от условия
person2.surname = 'Петров' - вызовет ошибку, так как атрибут не разрешен в __slots__

## Лабораторная работа №2
### Написать класс для мороженого, который проверяет добавлен ли топпинг и выводит соответствующее сообщение. Топпингом считать только строки.
```
class IceCream:
    def __init__(self, topping=None):
        self.topping = topping
    
    def check_topping(self):
        if isinstance(self.topping, str) and self.topping:
            print(f"Мороженое с {self.topping}")
        else:
            print("Обычное мороженое")

ice1 = IceCream("карамель")
ice2 = IceCream()
ice3 = IceCream(123)

ice1.check_topping()
ice2.check_topping()
ice3.check_topping()
```
### Результат.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_9/theme9lab2.jpg)

## Выводы
isinstance(self.topping, str) - проверяет что топпинг является строкой
and self.topping - дополнительно проверяет что строка не пустая
topping=None - значение по умолчанию, если топпинг не указан

## Лабораторная работа №3
### Создать класс с инкапсуляцией, включающий сеттер, геттер и деструктор. Продемонстрировать работу всех функций.
```
class Student:
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def __del__(self):
        print(f"Объект студента {self.__name} удален")

student = Student("Петя")
print(student.get_name())
student.set_name("Вася")
print(student.get_name())
del student
```
### Результат.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_9/theme9lab3.jpg)

## Выводы
self.__name - защищенный атрибут (инкапсуляция)
get_name() и set_name() - методы для доступа к защищенному атрибуту
__del__() - деструктор, вызывается при удалении объекта

## Лабораторная работа №4
### Создать три класса: Млекопитающие, Кошки, Собаки с использованием наследования. Добавить уникальные атрибуты для кошек и собак.
```
class Mammal:
    def __init__(self):
        self.type = "Млекопитающее"

class Cat(Mammal):
    def __init__(self):
        super().__init__()
        self.sound = "Мяу"

class Dog(Mammal):
    def __init__(self):
        super().__init__()
        self.sound = "Гав"

cat = Cat()
dog = Dog()
print(f"Кошка: {cat.type}, говорит: {cat.sound}")
print(f"Собака: {dog.type}, говорит: {dog.sound}")
```
### Результат.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_9/theme9lab4.jpg)

## Выводы
class Cat(Mammal) - наследование от класса Mammal
super().__init__() - вызов конструктора родительского класса
self.sound - уникальный атрибут для каждого дочернего класса

## Лабораторная работа №5
### Реализовать программу с полиморфизмом для приветствий на разных языках. Использовать статический метод.
```
class Russian:
    @staticmethod
    def greet():
        return "Привет"

class English:
    @staticmethod  
    def greet():
        return "Hello"

def show_greeting(language):
    print(f"На этом языке говорят: {language.greet()}")

russian = Russian()
english = English()

show_greeting(russian)
show_greeting(english)
```
### Результат.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_9/theme9lab5.jpg)

## Выводы
@staticmethod - декоратор для статического метода
language.greet() - полиморфизм: один метод работает для разных классов
Не нужен параметр self в статических методах

