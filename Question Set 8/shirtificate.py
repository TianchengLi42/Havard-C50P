from fpdf import FPDF
from PIL import Image
image = Image.open('shirtificate.png')


class PDF(FPDF):
    def __init__(self, header_text="", footer_text=""):
        super().__init__(unit="mm", format="A4")
        self.header_text = header_text
        self.footer_text = footer_text

    def add_image_page(self, image_path):
        page_width, page_height = 210, 297
        with Image.open(image_path) as img:
            img_width, img_height = img.size
        # Convert px to mm
        img_width_mm = img_width * 0.264583
        img_height_mm = img_height * 0.264583
        # Scale proportionally
        scale = min(page_width / img_width_mm, page_height / img_height_mm)
        display_width = img_width_mm * scale
        display_height = img_height_mm * scale
        x_offset = (page_width - display_width) / 2
        y_offset = (page_height - display_height) / 2
        self.add_page()
        self.image(image_path, x=x_offset, y=y_offset, w=display_width, h=display_height)

    def header(self):
        if self.header_text:
            self.set_font("Helvetica", "B", 14)
            self.cell(0, 10, self.header_text, ln=True, align="C")
            self.ln(5)

    def footer(self):
        if self.footer_text:
            self.set_y(-2)
            self.set_font("Helvetica", "I", 10)
            self.cell(0, 10, f"{self.footer_text}", ln=True, align="C")


def main():
    pdf = PDF(header_text="CS50 Shirtificate", footer_text="John took CS50")
    pdf.add_image_page("shirtificate.png")
    pdf.output("shirt_certificate.pdf")


if __name__ == "__main__":
    main()