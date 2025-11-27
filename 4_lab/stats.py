from enum import Enum
from student import Student
from book import Book


class Action(Enum):
    """Enum для типів дій з книгою"""
    BORROWED = "взяв"
    RETURNED = "повернув"


class Stats:
    """Клас для збору статистики про читання книг студентами"""
    
    def __init__(self):
        # Словник для зберігання дня коли студент взяв книгу
        # Ключ: (student_id, book_title), значення: день взяття
        self._borrow_records: dict[tuple, int] = {}
        
        # Словник для зберігання загальної кількості днів читання по студентах
        # Ключ: student_id, значення: загальна кількість днів читання
        self._reading_days: dict[int, int] = {}
        
        # Словник для зберігання днів читання по книгах для кожного студента
        # Ключ: student_id, значення: словник {book_title: кількість днів}
        self._reading_days_per_book: dict[int, dict[str, int]] = {}
        
        # Історія читання
        self._history: list[dict] = []
    
    def record_borrow(self, student: Student, book: Book, day: int):
        """Записує день коли студент взяв книгу"""
        key = (student.student_id, book.title)
        self._borrow_records[key] = day
        self._history.append({
            "student": student.name,
            "book": book.title,
            "action": Action.BORROWED,
            "day": day
        })
        print(f"[Stats] Записано: '{student.name}' взяв книгу '{book.title}' на день {day}")
    
    def record_return(self, student: Student, book: Book, day: int):
        """Записує повернення книги та обчислює кількість днів читання"""
        key = (student.student_id, book.title)
        
        if key in self._borrow_records:
            borrow_day = self._borrow_records[key]
            days_read = day - borrow_day
            
            # Додаємо дні читання до загальної статистики студента
            if student.student_id not in self._reading_days:
                self._reading_days[student.student_id] = 0
            self._reading_days[student.student_id] += days_read
            
            # Додаємо дні читання по книзі для студента
            if student.student_id not in self._reading_days_per_book:
                self._reading_days_per_book[student.student_id] = {}
            if book.title not in self._reading_days_per_book[student.student_id]:
                self._reading_days_per_book[student.student_id][book.title] = 0
            self._reading_days_per_book[student.student_id][book.title] += days_read
            
            self._history.append({
                "student": student.name,
                "book": book.title,
                "action": Action.RETURNED,
                "day": day,
                "days_read": days_read
            })
            
            print(f"[Stats] '{student.name}' повернув книгу '{book.title}' на день {day}. "
                  f"Читав {days_read} днів.")
            
            # Видаляємо запис про взяття
            del self._borrow_records[key]
        else:
            print(f"[Stats] Помилка: немає запису про взяття книги '{book.title}' студентом '{student.name}'")
    
    def get_student_reading_days(self, student: Student) -> int:
        """Повертає загальну кількість днів читання для студента"""
        return self._reading_days.get(student.student_id, 0)
    
    def get_student_reading_days_per_book(self, student: Student) -> dict[str, int]:
        """Повертає словник з кількістю днів читання по кожній книзі для студента"""
        return self._reading_days_per_book.get(student.student_id, {})
    
    def print_student_stats(self, student: Student):
        """Виводить статистику для конкретного студента"""
        days = self.get_student_reading_days(student)
        books_stats = self.get_student_reading_days_per_book(student)
        print(f"=== Статистика студента '{student.name}' ===")
        print(f"| Загальна кількість днів читання: {days}")
        if books_stats:
            print(f"| Читання по книгах:")
            for book_title, book_days in books_stats.items():
                print(f"|   - '{book_title}': {book_days} днів")
    
    def print_all_stats(self, students: list[Student]):
        """Виводить статистику для всіх студентів"""
        print("\n" + "=" * 50)
        print(">>> ЗАГАЛЬНА СТАТИСТИКА ЧИТАННЯ <<<")
        print("=" * 50)
        for student in students:
            days = self.get_student_reading_days(student)
            books_stats = self.get_student_reading_days_per_book(student)
            print(f"| {student.name}: {days} днів читання")
            if books_stats:
                for book_title, book_days in books_stats.items():
                    print(f"|   - '{book_title}': {book_days} днів")
        print("=" * 50)