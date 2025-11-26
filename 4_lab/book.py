from enum import Enum


class BookStatus(Enum):
    AVAILABLE = "Доступна"
    BORROWED = "Взята"
    LOST = "Втрачена"


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.description = f"|Назва: {self.title};\n|Автор: {self.author};"
        self.status: BookStatus = BookStatus.AVAILABLE
    
    def __str__(self):
        return self.description