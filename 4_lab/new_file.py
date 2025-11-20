class IncorrectClass:
    def __init__(self):
        print("Ми створили цей об'єкту у файлі new_file.py.")

print(f"{__name__} виконується.")
if __name__ == "__main__":
    a = IncorrectClass()