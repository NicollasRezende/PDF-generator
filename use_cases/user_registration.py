from interface_adapters.user_repository import UserRepository
from interface_adapters.pdf_generator import PDFGenerator

class UserRegistration:
    def __init__(self, user_repo: UserRepository, pdf_gen: PDFGenerator):
        self.user_repo = user_repo
        self.pdf_gen = pdf_gen

    def register_user(self, user):
        user_id = self.user_repo.add_user(user)
        self.pdf_gen.generate_pdf(user_id)
        return user_id
