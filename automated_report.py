import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# -------------------------------
# 1. Read Data
# -------------------------------
# Make sure you have a CSV file named "sample_data.csv" in the same folder
# Example content:
# Name,Score
# Alice,85
# Bob,78
# Charlie,92
# David,67
# Emma,74

df = pd.read_csv("sample_data.csv")

# -------------------------------
# 2. Analyze Data
# -------------------------------
summary = df.describe()

# Create a bar chart of scores
plt.figure(figsize=(6,4))
df["Score"].plot(kind="bar", color="skyblue")
plt.title("Scores of Participants")
plt.xlabel("Index")
plt.ylabel("Score")
plt.tight_layout()
plt.savefig("scores_chart.png")
plt.close()

# -------------------------------
# 3. Generate PDF Report
# -------------------------------
report = SimpleDocTemplate("Final_Report.pdf", pagesize=A4)
styles = getSampleStyleSheet()
flow = []

# Title
flow.append(Paragraph("<b>Automated Report</b>", styles["Title"]))
flow.append(Spacer(1, 20))

# Summary Table
flow.append(Paragraph("Summary Statistics:", styles["Heading2"]))

# Convert summary DataFrame to table
table_data = [summary.columns.to_list()] + summary.round(2).values.tolist()
summary_table = Table(table_data)
summary_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey)
]))
flow.append(summary_table)
flow.append(Spacer(1, 20))

# Chart
flow.append(Paragraph("Scores Chart:", styles["Heading2"]))
flow.append(Image("scores_chart.png", width=400, height=250))
flow.append(Spacer(1, 40))

# Completion Certificate Section
certificate_text = """
<b>Completion Certificate</b><br/><br/>
This is to certify that the internship has been successfully completed.<br/><br/>
Completion Date: <b>14-Sep-2025</b><br/>
Issued by: <b>CODTECH</b>
"""
flow.append(Paragraph(certificate_text, styles["Normal"]))

# Build PDF
report.build(flow)

print("✅ Report generated successfully: Final_Report.pdf")
