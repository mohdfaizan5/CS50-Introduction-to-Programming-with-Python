from fpdf import FPDF

class Pdf:

    def __init__(self, name):

        self.pdf = FPDF()
        # Default thing to keep
        # self.pdf = FPDF(orientation="P", format="A4")

        # Adding the page
        self.pdf.add_page()

        # Setting the font before writing, else it will create an error
        self.pdf.set_font('helvetica', 'B', 50)

        # Printing the top "CS50 Shirtificate"
        self.pdf.cell(0, 60, "CS50 Shirtificate", new_x = "LMARGIN",new_y = "NEXT",align='C')

        # Adding image
        self.pdf.image("/workspaces/79694828/p8/shirtificate.png", w=self.pdf.epw)#, align="C")

        #
        self.pdf.set_font_size(30)

        self.pdf.set_text_color(255,255,255)

        self.pdf.text(x=47, y=150, txt=f"{name} took CS50")

    # Method to save the file:
    def save(self, name):

        # Printing the top "CS50 Shirtificate"
        # self.pdf.cell(0, 50, name, new_x = "LMARGIN",new_y = "NEXT",align='C')

        # Printing the output
        self.pdf.output(name)

# Taking input from user
usr_name = input("Name: ")
a = Pdf(usr_name)
a.save("shirtificate.pdf")