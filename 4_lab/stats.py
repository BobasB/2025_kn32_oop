from enum import Enum
from datetime import datetime, timedelta
from student import Student
from book import Book


class Action(Enum):
    """Enum для типів дій з книгою"""
    BORROWED = "взяв"
    RETURNED = "повернув"


class Stats:
    """Клас для збору статистики про читання книг студентами"""
    
    def __init__(self, start_date: datetime = None):
        # Початкова дата симуляції (якщо не вказана - сьогодні)
        self.start_date = start_date or datetime.now()
        
        # Словник для зберігання дати коли студент взяв книгу
        # Ключ: (student_id, book_title), значення: дата взяття
        self._borrow_records: dict[tuple, datetime] = {}
        
        # Словник для зберігання загальної кількості днів читання по студентах
        # Ключ: student_id, значення: загальна кількість днів читання
        self._reading_days: dict[int, int] = {}
        
        # Словник для зберігання днів читання по книгах для кожного студента
        # Ключ: student_id, значення: словник {book_title: кількість днів}
        self._reading_days_per_book: dict[int, dict[str, int]] = {}
        
        # Історія читання
        self._history: list[dict] = []
    
    def day_to_date(self, day: int) -> datetime:
        """Конвертує номер дня симуляції в дату"""
        return self.start_date + timedelta(days=day - 1)
    
    def format_date(self, date: datetime) -> str:
        """Форматує дату для виводу"""
        return date.strftime("%d.%m.%Y")
    
    def record_borrow(self, student: Student, book: Book, day: int):
        """Записує дату коли студент взяв книгу"""
        key = (student.student_id, book.title)
        borrow_date = self.day_to_date(day)
        self._borrow_records[key] = borrow_date
        self._history.append({
            "student": student.name,
            "book": book.title,
            "action": Action.BORROWED,
            "date": borrow_date,
            "day": day
        })
        print(f"[Stats] Записано: '{student.name}' взяв книгу '{book.title}' {self.format_date(borrow_date)}")
    
    def record_return(self, student: Student, book: Book, day: int):
        """Записує повернення книги та обчислює кількість днів читання"""
        key = (student.student_id, book.title)
        return_date = self.day_to_date(day)
        
        if key in self._borrow_records:
            borrow_date = self._borrow_records[key]
            days_read = (return_date - borrow_date).days
            
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
                "date": return_date,
                "day": day,
                "borrow_date": borrow_date,
                "days_read": days_read
            })
            
            print(f"[Stats] '{student.name}' повернув книгу '{book.title}' {self.format_date(return_date)}. "
                  f"Читав з {self.format_date(borrow_date)} ({days_read} днів).")
            
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
        print(f">>> Період: {self.format_date(self.start_date)} - {self.format_date(datetime.now())}")
        print("=" * 50)
        for student in students:
            days = self.get_student_reading_days(student)
            books_stats = self.get_student_reading_days_per_book(student)
            print(f"| {student.name}: {days} днів читання")
            if books_stats:
                for book_title, book_days in books_stats.items():
                    print(f"|   - '{book_title}': {book_days} днів")
        print("=" * 50)