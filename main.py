from entities.user import User
from use_cases.user_registration import UserRegistration
from interface_adapters.user_repository import UserRepository
from interface_adapters.pdf_generator import PDFGenerator

def main():
    user_repo = UserRepository()
    pdf_gen = PDFGenerator()
    user_registration = UserRegistration(user_repo, pdf_gen)

    name = input("Nome: ")
    email = input("Email: ")
    age = int(input("Idade: "))
    
    user = User(name, email, age)
    user_id = user_registration.register_user(user)
    print(f"Usuário registrado com ID {user_id}")

if __name__ == "__main__":
    main()
