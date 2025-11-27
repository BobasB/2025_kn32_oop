# UML діаграма класів проекту "Бібліотека"

```mermaid
classDiagram
    direction TB
    
    %% Enum класи
    class BookStatus {
        <<enumeration>>
        AVAILABLE : "Доступна"
        BORROWED : "Взята"
        LOST : "Втрачена"
    }
    
    class Action {
        <<enumeration>>
        BORROWED : "взяв"
        RETURNED : "повернув"
    }
    
    %% Основні класи
    class Book {
        +title : str
        +author : str
        +description : str
        +status : BookStatus
        +__init__(title, author)
        +__str__() str
    }
    
    class Student {
        +name : str
        +student_id : int
        +description : str
        +borrowed_books : list~Book~
        +__init__(name)
        +list_borrowed_books() property
        +__str__() str
    }
    
    class Stats {
        +start_date : datetime
        -_borrow_records : dict~tuple, datetime~
        -_reading_days : dict~int, int~
        -_reading_days_per_book : dict~int, dict~
        -_history : list~dict~
        +__init__(start_date)
        +day_to_date(day) datetime
        +format_date(date) str
        +record_borrow(student, book, day)
        +record_return(student, book, day)
        +get_student_reading_days(student) int
        +get_student_reading_days_per_book(student) dict
        +print_student_stats(student)
        +print_all_stats(students)
    }
    
    class Library {
        +books : list~Book~
        +available_books : list~Book~
        +students : list~Student~
        +stats : Stats
        +__init__()
        +add_book(book)
        +list_books() property
        +list_available_books() property
        +list_students() property
        +register_student(student)
        +lend_book(book, student, day)
        +return_book(book, student, day)
    }
    
    %% Зв'язки
    Book --> BookStatus : uses
    Stats --> Action : uses
    Stats --> Student : uses
    Stats --> Book : uses
    Library --> Book : contains *
    Library --> Student : contains *
    Library --> Stats : has 1
    Student --> Book : borrows *
```

## Опис зв'язків

| Зв'язок | Тип | Опис |
|---------|-----|------|
| Library → Book | Композиція (1:*) | Бібліотека містить багато книг |
| Library → Student | Композиція (1:*) | Бібліотека містить багато студентів |
| Library → Stats | Композиція (1:1) | Бібліотека має один об'єкт статистики |
| Student → Book | Асоціація (*:*) | Студент може мати багато книг |
| Book → BookStatus | Залежність | Книга використовує статус |
| Stats → Action | Залежність | Статистика використовує типи дій |

## Діаграма послідовності: Взяття книги

```mermaid
sequenceDiagram
    participant Main
    participant Library
    participant Book
    participant Student
    participant Stats
    
    Main->>Library: lend_book(book, student, day)
    Library->>Library: перевірка книги
    Library->>Library: перевірка студента
    Library->>Book: перевірка status
    Book-->>Library: BookStatus.AVAILABLE
    Library->>Student: borrowed_books.append(book)
    Library->>Book: status = BookStatus.BORROWED
    Library->>Stats: record_borrow(student, book, day)
    Stats->>Stats: зберегти дату взяття
    Stats-->>Library: done
    Library-->>Main: книга видана
```

## Діаграма послідовності: Повернення книги

```mermaid
sequenceDiagram
    participant Main
    participant Library
    participant Book
    participant Student
    participant Stats
    
    Main->>Library: return_book(book, student, day)
    Library->>Library: перевірка студента
    Library->>Student: перевірка borrowed_books
    Student-->>Library: книга є
    Library->>Student: borrowed_books.remove(book)
    Library->>Book: status = BookStatus.AVAILABLE
    Library->>Stats: record_return(student, book, day)
    Stats->>Stats: обчислити дні читання
    Stats->>Stats: оновити статистику
    Stats-->>Library: done
    Library-->>Main: книга повернена
```
