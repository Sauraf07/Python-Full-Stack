from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm

FILE_NAME = "Weekly_Progress_Report_Priyam_Week01.pdf"

styles = getSampleStyleSheet()
title_style = ParagraphStyle("Title", parent=styles["Title"], fontSize=18, spaceAfter=10)
h_style = ParagraphStyle("H", parent=styles["Heading2"], fontSize=12.5, spaceBefore=10, spaceAfter=6)
subh_style = ParagraphStyle("SubH", parent=styles["Heading3"], fontSize=11.5, spaceBefore=6, spaceAfter=4)
body = ParagraphStyle("Body", parent=styles["BodyText"], fontSize=11, leading=14)

doc = SimpleDocTemplate(
    FILE_NAME,
    pagesize=A4,
    leftMargin=2 * cm,
    rightMargin=2 * cm,
    topMargin=2 * cm,
    bottomMargin=2 * cm,
)

name = "Priyam Kumar Mishra"
domain = "Python Internship"
date = "2026-04-07"
week = "01"
project = "Quiz Game"

story = []

# Title
story.append(Paragraph("Weekly Progress Report (Alternate Version)", title_style))
story.append(Spacer(1, 6))

# Header table (different look)
header_data = [
    ["Name", name],
    ["Domain", domain],
    ["Date of Submission", date],
    ["Week Number / Week Ending", f"Week {week}"],
]
tbl = Table(header_data, colWidths=[5.2 * cm, 11.0 * cm])
tbl.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#f0f0f0")),
    ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
    ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
    ("FONTSIZE", (0, 0), (-1, -1), 10.5),
    ("ALIGN", (0, 0), (0, -1), "LEFT"),
    ("ALIGN", (1, 0), (1, -1), "LEFT"),
    ("GRID", (0, 0), (-1, -1), 0.6, colors.grey),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("ROWBACKGROUNDS", (1, 0), (1, -1), [colors.white, colors.HexColor("#fbfbfb")]),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
]))
story.append(tbl)
story.append(Spacer(1, 12))

# 1) Summary
story.append(Paragraph("1) Summary of Work Done", h_style))
story.append(Paragraph(
    "During this first week, I focused on getting started with Python by learning the basics and understanding "
    "how Python programs are written and executed. Along with this, I finalized my project choice as "
    f"<b>{project}</b> and outlined how the project will work from user interaction to scoring.",
    body
))

# 2) Key Progress
story.append(Paragraph("2) Key Progress / Completed Tasks", h_style))

story.append(Paragraph("A. Python Basics (Introduction)", subh_style))
items_a = [
    "Learned the basic structure of a Python program and the use of the Python interpreter.",
    "Practiced beginner concepts like variables and data types, taking user input and displaying output, and simple conditions using if-else.",
    "Wrote small practice programs to improve familiarity with syntax and indentation.",
]
story.append(ListFlowable([ListItem(Paragraph(x, body)) for x in items_a],
                         bulletType="bullet", leftIndent=18))

story.append(Spacer(1, 6))
story.append(Paragraph("B. Project Selection and Understanding", subh_style))
story.append(Paragraph(f"<b>Selected Project:</b> {project}", body))
items_b = [
    "Understood the goal of the Quiz Game: show questions, accept answers, and calculate score.",
    "Broke the project into a simple flow: store questions and answers, display questions one by one, take user response, update score and show final result.",
]
story.append(ListFlowable([ListItem(Paragraph(x, body)) for x in items_b],
                         bulletType="bullet", leftIndent=18))

# 3) Issues
story.append(Paragraph("3) Issues / Difficulties Faced", h_style))
items_c = [
    "Initially faced difficulty with writing correct conditional logic and maintaining proper indentation.",
    "Needed extra practice to avoid syntax errors and to understand program flow step-by-step.",
]
story.append(ListFlowable([ListItem(Paragraph(x, body)) for x in items_c],
                         bulletType="bullet", leftIndent=18))

# 4) Learning materials
story.append(Paragraph("4) Learning Materials Used", h_style))
items_d = [
    "Python beginner notes/tutorials for fundamentals.",
    "Practice examples from Python documentation and basic coding exercises.",
]
story.append(ListFlowable([ListItem(Paragraph(x, body)) for x in items_d],
                         bulletType="bullet", leftIndent=18))

# 5) Next week plan
story.append(Paragraph("5) Plan for Next Week", h_style))
items_e = [
    "Improve understanding of loops (for, while), functions, and lists/dictionaries for storing quiz questions.",
    "Begin coding the Quiz Game MVP: hardcode 5–10 questions first, implement scoring, and add basic input validation.",
]
story.append(ListFlowable([ListItem(Paragraph(x, body)) for x in items_e],
                         bulletType="bullet", leftIndent=18))

# 6) Remarks
story.append(Paragraph("6) Remarks", h_style))
story.append(Paragraph(
    "Week 01 was mainly focused on building the foundation. I am now more comfortable with basic Python syntax "
    "and ready to start implementing the first version of the Quiz Game project.",
    body
))

doc.build(story)
print(f"PDF created: {FILE_NAME}")