# Звіт до роботи
## Тема: _Основні парадигми ООП_
### Мета роботи: _Ознайомитись з ключовими поняттями об'єктно-орієнтованого програмування (ООП) у Python та навчитися реалізовувати їх у власних класах на прикладі практичних симуляцій_

---

### Виконання роботи

Всі приклади виконано у Jupyter Notebook — [note.ipynb](note.ipynb)

#### 1. Інкапсуляція (Encapsulation)

Реалізовано клас `CheckStudentBored`, що демонструє приховування внутрішньої реалізації:

```python
class CheckStudentBored:
    def __init__(self, name, words_threshold=50):
        self.__name = name                          # приватний атрибут
        self.__words_threshold = words_threshold    # приватний атрибут
    
    def __generate_lecture_words(self):             # приватний метод
        import random
        return random.randint(0, 100)
    
    def check_if_student_bored(self):               # публічний інтерфейс
        if self.__generate_lecture_words() > self.__words_threshold:
            return f"Студент {self.__name} занудьгував на лекції."
        return f"Студент {self.__name} НЕ занудьгував на лекції."
```

**Ключові принципи:**
- Приватні атрибути (`__name`) — недоступні ззовні класу
- Публічний інтерфейс ховає деталі реалізації
- Внутрішня логіка не доступна для прямого виклику

---

#### 2. Наслідування (Inheritance)

Реалізовано ієрархію класів для симуляції **станції безперебійного живлення**:

```
EnergyDevice (базовий клас)
├── SolarPanel      — сонячні панелі
├── WindTurbine     — вітряки  
└── DieselGenerator — дизельний генератор
```

```python
class EnergyDevice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.__max_capacity = capacity

    @property
    def info(self):
        return f"Пристрій: {self.name}, Ємність: {self.__max_capacity}"

class SolarPanel(EnergyDevice):
    def __init__(self, name, capacity, panel_count):
        super().__init__(name, capacity)
        self.panel_count = panel_count
    
    def generate(self, sunlight_hours):
        return self.capacity * self.panel_count * sunlight_hours
```

**Ключові принципи:**
- Дочірній клас наслідує атрибути та методи батьківського
- `super().__init__()` — виклик конструктора батька
- Дочірні класи можуть розширювати та перевизначати поведінку

---

#### 3. Поліморфізм (Polymorphism)

Один інтерфейс — різна реалізація для кожного типу пристрою:

```python
devices = [
    SolarPanel("Сонячна панель", 5, panel_count=10),
    WindTurbine("Вітряк", 8, wind_speed=15),
    DieselGenerator("Генератор", 20, fuel_liters=100)
]

# Один виклик — різна поведінка для кожного об'єкту
for device in devices:
    print(device.generate())
```

---

#### 4. Абстракція (Abstraction)

Використання абстрактних базових класів через модуль `abc`:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
```

---

#### Підсумкова таблиця парадигм ООП

| Парадигма | Ключове поняття | Приклад у роботі |
|-----------|----------------|------------------|
| **Інкапсуляція** | Приховування даних | `__name`, `__generate_lecture_words()` |
| **Наслідування** | Розширення класів | `SolarPanel(EnergyDevice)` |
| **Поліморфізм** | Єдиний інтерфейс | `device.generate()` для різних типів |
| **Абстракція** | Визначення контракту | `ABC`, `@abstractmethod` |

---

### Висновок

В ході виконання лабораторної роботи:
- Освоєно всі чотири ключові парадигми ООП: **інкапсуляцію**, **наслідування**, **поліморфізм** та **абстракцію**
- Практично реалізовано ієрархію класів для реальних сценаріїв (симуляція бори та енергосистеми)
- Зрозуміло різницю між приватними (`__`) та захищеними (`_`) атрибутами
- Навчились використовувати `super()` для виклику методів батьківського класу
- Застосовано абстрактні класи для визначення обов'язкового інтерфейсу

Мета роботи досягнута: практично освоєно всі основні парадигми ООП у Python.

---