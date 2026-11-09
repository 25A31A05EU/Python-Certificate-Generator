from PIL import Image, ImageDraw, ImageFont
from datetime import date
import os
import random
import string

W, H = 1600, 1100

def font(size, bold=False):
    try:
        return ImageFont.truetype(
            "/system/fonts/Roboto-Bold.ttf" if bold
            else "/system/fonts/Roboto-Regular.ttf", size
        )
    except:
        return ImageFont.load_default()

def center(draw, text, y, f, color):
    box = draw.textbbox((0, 0), text, font=f)
    x = (W - (box[2] - box[0])) // 2
    draw.text((x, y), text, font=f, fill=color)

def generate(name, course, organization):
    img = Image.new("RGB", (W, H), "#172554")
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle(
        (35, 35, 1565, 1065),
        radius=30, outline="#FACC15", width=8
    )

    center(draw, "CERTIFICATE", 150, font(85, True), "#FACC15")
    center(draw, "OF ACHIEVEMENT", 260, font(42, True), "white")
    center(draw, "This certificate is presented to", 400,
           font(30), "white")
    center(draw, name.upper(), 500, font(65, True), "#FACC15")
    center(draw, "For successfully completing", 620,
           font(30), "white")
    center(draw, course, 690, font(43, True), "#38BDF8")
    center(draw, organization, 830, font(30, True), "white")

    today = date.today().strftime("%d-%m-%Y")
    cert_id = "CERT-" + "".join(
        random.choices(string.ascii_uppercase + string.digits, k=8)
    )

    draw.text((150, 960), "Date: " + today,
              font=font(24), fill="white")
    draw.text((1100, 960), "Authorized Signature",
              font=font(24), fill="white")
    draw.text((150, 1010), "ID: " + cert_id,
              font=font(20), fill="#FACC15")

    os.makedirs("certificates", exist_ok=True)
    filename = "".join(
        c for c in name if c.isalnum() or c in " _-"
    ).strip().replace(" ", "_") or "Student"

    path = os.path.join(
        "certificates", filename + "_certificate.png"
    )
    img.save(path)
    print("Certificate saved:", path)
    print("Certificate ID:", cert_id)

print("=== CERTIFICATE GENERATOR ===")

name = input("Enter student name: ").strip()
course = input("Enter course name: ").strip()
organization = input("Enter organization: ").strip()

if name and course and organization:
    generate(name, course, organization)
else:
    print("Please enter all details.")
