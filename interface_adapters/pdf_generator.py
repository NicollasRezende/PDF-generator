from fpdf import FPDF
from frameworks_and_drivers.database import DatabaseConnection

class PDFGenerator:
    def __init__(self):
        self.db = DatabaseConnection()

    def generate_pdf(self, user_id):
        user = self.db.get_user_by_id(user_id)
        
        if user:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="User Information", ln=True, align='C')
            pdf.cell(200, 10, txt=f"ID: {user['id']}", ln=True)
            pdf.cell(200, 10, txt=f"Name: {user['name']}", ln=True)
            pdf.cell(200, 10, txt=f"Email: {user['email']}", ln=True)
            pdf.cell(200, 10, txt=f"Age: {user['age']}", ln=True)
            pdf.output(f"user_{user_id}.pdf")
            print(f"PDF gerado para o usuário ID {user_id}!")
        else:
            print("Usuário não encontrado.")
