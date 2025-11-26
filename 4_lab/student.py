from book import Book

class Student:
    def __init__(self, name):
        self.name = name
        self.student_id = id(self)
        self.description = f"|Ім'я: {self.name};\n|ID студента: {self.student_id};"
        self.borrowed_books: list[Book] = []
    
    # Додаємо метод перегляду які книжки зараз має студент
    @property
    def list_borrowed_books(self):
        for b in self.borrowed_books:
            print(f"Взято книгу: {b}")
    
    def __str__(self):
        return self.description
