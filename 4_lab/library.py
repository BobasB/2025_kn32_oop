from book import Book, BookStatus
from student import Student

class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.available_books: list[Book] = []
        self.students: list[Student] = []
    
    def add_book(self, book: Book):
        """Метод для додавання книги до бібліотеки"""
        print(f"Додаємо книгу: {book.title}")
        self.books.append(book)
        self.available_books.append(book)
    
    @property
    def list_books(self):
        return self.books
    
    @property
    def list_available_books(self):
        return [book for book in self.books if book.status == BookStatus.AVAILABLE]
    
    @property
    def list_students(self):
        return self.students
    
    def register_student(self, student: Student):
        """Метод для реєстрації студента в бібліотеці"""
        print(f"Реєструємо студента: {student.name}")
        self.students.append(student)
    
    # Додаємо метод для видачі книги студенту
    def lend_book(self, book: Book, student: Student):
        # Знаходимо книгу за назвою
        if book not in self.books:
            print(f"Книга '{book.title}' не знайдена в бібліотеці.")
            return
        
        # Перевіряємо чи студент зареєстрований
        if student not in self.students:
            print(f"Студент з ID '{student.student_id}' не зареєстрований в бібліотеці.")
            return
        
        # Видаємо книгу студенту
        if book.status != BookStatus.AVAILABLE:
            print(f"Книга '{book.title}' наразі недоступна для видачі.")
            return
        
        student.borrowed_books.append(book)
        self.available_books.remove(book)
        book.status = BookStatus.BORROWED
        print(f"Книга '{book.title}' видана студенту '{student.name}'.")
    
    # Додаємо метод для повернення книги до бібліотеки
    def return_book(self, book: Book, student: Student):
        # Перевіряємо чи студент зареєстрований
        if student not in self.students:
            print(f"Студент з ID '{student.student_id}' не зареєстрований в бібліотеці.")
            return
        
        # Перевіряємо чи студент має цю книгу
        if book not in student.borrowed_books:
            print(f"Студент '{student.name}' не має книги '{book.title}' для повернення.")
            return
        
        # Повертаємо книгу до бібліотеки
        student.borrowed_books.remove(book)
        self.available_books.append(book)
        book.status = BookStatus.AVAILABLE
        print(f"Книга '{book.title}' повернена до бібліотеки від студента '{student.name}'.")
