class User:
    def __init__(self, name):
        self.__name = name  # Encapsulación para el nombre del usuario

    @property
    def name(self):
        return self.__name

    def search_book(self, book_name):
        print(f"{self.name} is searching for the book: {book_name}")  # Mostrar que el usuario está buscando un libro

    def select_book(self, book_name):
        print(f"{self.name} selected the book: {book_name}")  # Mostrar que el usuario seleccionó un libro


class Catalogue:
    def __init__(self):
        self.__books = []  # Encapsulación para la lista de libros en el catálogo

    def add_book(self, book_name):
        self.__books.append(book_name)
        print(f"Book '{book_name}' added to the catalogue.")  # Libro agregado al catálogo

    def check_available_books(self):
        print("Available books in the catalogue:")  # Mostrar libros disponibles en el catálogo
        for book in self.__books:
            print(f"- {book}")


class AvailableBooks(Catalogue):  # Herencia de la clase Catalogue
    def __init__(self):
        super().__init__()

    def check_availability(self, book_name):
        if book_name in self._Catalogue__books:  # Acceder a la lista de libros heredada
            print(f"The book '{book_name}' is available.")  # El libro está disponible
            return True
        else:
            print(f"The book '{book_name}' is not available.")  # El libro no está disponible
            return False


class Loan:
    def __init__(self):
        self.__loans = []  # Encapsulación para los préstamos actuales

    def borrow_book(self, user, book_name, available_books):
        try:  # Manejo de errores
            if available_books.check_availability(book_name):
                self.__loans.append({"user": user.name, "book": book_name})
                available_books._Catalogue__books.remove(book_name)  # Remover de la lista de libros disponibles
                print(f"{user.name} has borrowed the book: {book_name}")  
                raise ValueError(f"{book_name} is not available.")  # Error si el libro no está disponible
        except ValueError as e:
            print(e)

    def return_book(self, user, book_name, available_books):
        for loan in self.__loans:
            if loan["user"] == user.name and loan["book"] == book_name:
                self.__loans.remove(loan)
                available_books.add_book(book_name)
                print(f"{user.name} has returned the book: {book_name}")  # Mostrar que el usuario devolvió el libro
                return
        print(f"No record found for {user.name} borrowing {book_name}.")  # No se encontró registro del préstamo

    def check_penalties(self, user):
        print(f"Checking penalties for {user.name}...")  # Verificando penalizaciones para el usuario
        print("No penalties found.")  # No se encontraron penalizaciones


class PremiumUser(User):  # Polimorfismo
    def search_book(self, book_name):
        print(f"{self.name} (Premium User) is searching for the book: {book_name}")  


if __name__ == "__main__":
    catalogue = Catalogue()
    available_books = AvailableBooks()
    loan_system = Loan()

    while True:
        print("\n--- Menú del Sistema de Biblioteca ---")  # Menú principal
        print("1. Agregar un libro al catálogo")
        print("2. Ver libros disponibles")
        print("3. Prestar un libro")
        print("4. Devolver un libro")
        print("5. Verificar penalizaciones")
        print("6. Salir")

        try:
            option = int(input("Seleccione una opción: "))  # Obtener selección del usuario

            if option == 1:
                book_name = input("Ingrese el nombre del libro para agregar: ")
                catalogue.add_book(book_name)
                available_books.add_book(book_name)

            elif option == 2:
                catalogue.check_available_books()

            elif option == 3:
                user_name = input("Ingrese su nombre: ")
                user = User(user_name)
                book_name = input("Ingrese el nombre del libro que desea prestar: ")
                loan_system.borrow_book(user, book_name, available_books)

            elif option == 4:
                user_name = input("Ingrese su nombre: ")
                user = User(user_name)
                book_name = input("Ingrese el nombre del libro que desea devolver: ")
                loan_system.return_book(user, book_name, available_books)

            elif option == 5:
                user_name = input("Ingrese su nombre: ")
                user = User(user_name)
                loan_system.check_penalties(user)

            elif option == 6:
                print("Saliendo del sistema. ¡Hasta luego!")  
                break

            else:
                print("Opción inválida. Por favor, intente nuevamente.")  

        except ValueError:
            print("Por favor, ingrese un número válido.")  