import random
import new_file
from library import Library
from book import Book
from student import Student

print(f"{__name__} виконується.")
if __name__ == "__main__":
    print("Запуск головної програми в main.py.")
    it_collage_library = Library()
    
    for name in ["Хірург", "Майстер і Маргарита", "1984", "Гаррі Поттер", "Історія Львова"]:
        book = Book(name, "Unknown")
        it_collage_library.add_book(book)

    for student in ["Богдан", "Анна", "Марія", "Руслан"]:
        new_student = Student(student)
        it_collage_library.register_student(new_student)

    print(">>> Список книг у бібліотеці:")
    for book in it_collage_library.list_books:
        print(f"{book}\n|Статус: Доступна\n---")

    print(">>> Список зареєстрованих студентів:")
    for student in it_collage_library.list_students:
        print(f"{student}\n---")

    # симулюємо роботу бібліотеки впродовж місяця
    for day in range(1, 31):
        print(f"=== День {day} ===")
        # Випадково вибираємо студента який буде брати книгу
        student = random.choice(it_collage_library.list_students)
        book = random.choice(it_collage_library.list_books)
        print(f"Студент '{student.name}' прийшов до бібліотеки та обрав книгу '{book.title}'.")
        if random.random() < 0.3: # з імовірністю 30% студент візьме книгу
            # Студент бере книгу
            it_collage_library.lend_book(book, student, day)
        else:
            # Студент повертає книгу, якщо є якась книга тоді він прийшов її повернути
            if student.borrowed_books:
                book_to_return: Book = random.choice(student.borrowed_books)
                it_collage_library.return_book(book_to_return, student, day)
        print("Студент пішов з бібліотеки.\n")
    
    # Виводимо загальну статистику після завершення симуляції
    it_collage_library.stats.print_all_stats(it_collage_library.list_students)
        