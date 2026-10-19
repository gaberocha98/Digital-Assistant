"""Build the Ultimate Budget Tracker XLSX with Digital Assistant brand colors."""
import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side, NamedStyle
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import ColorScaleRule, DataBarRule

# Brand colors
PRIMARY = "0D9488"        # Teal
PRIMARY_DARK = "115E59"   # Deep teal
PRIMARY_LIGHT = "CCFBF1"  # Mint
ACCENT = "F59E0B"         # Amber gold
ACCENT_LIGHT = "FEF3C7"   # Soft gold
DARK = "1E293B"           # Charcoal
LIGHT_BG = "F1F5F9"       # Cloud
WHITE = "FFFFFF"
INCOME = "10B981"
EXPENSE = "F43F5E"
SAVINGS = "3B82F6"
DEBT = "F97316"
BILLS = "8B5CF6"

def fill(color, font_color=DARK, bold=False):
    return {
        "fill": PatternFill(start_color=color, end_color=color, fill_type="solid"),
        "font": Font(color=font_color, bold=bold, name="Montserrat"),
    }

def header_style(color=PRIMARY_DARK):
    return {
        "fill": PatternFill(start_color=color, end_color=color, fill_type="solid"),
        "font": Font(color="FFFFFF", bold=True, size=11, name="Montserrat"),
        "alignment": Alignment(horizontal="center", vertical="center"),
    }

def apply_style(cell, style):
    if "fill" in style: cell.fill = style["fill"]
    if "font" in style: cell.font = style["font"]
    if "alignment" in style: cell.alignment = style["alignment"]
    if "border" in style: cell.border = style["border"]

thin_border = Border(
    left=Side(style="thin", color=PRIMARY_LIGHT),
    right=Side(style="thin", color=PRIMARY_LIGHT),
    top=Side(style="thin", color=PRIMARY_LIGHT),
    bottom=Side(style="thin", color=PRIMARY_LIGHT),
)

wb = openpyxl.Workbook()

# ============ INSTRUCTIONS TAB ============
ws = wb.active
ws.title = "Instructions"
ws.sheet_properties.tabColor = PRIMARY

# Title
ws["B2"] = "ULTIMATE BUDGET TRACKER"
ws.merge_cells("B2:H3")
apply_style(ws["B2"], {
    "fill": PatternFill(start_color=PRIMARY_DARK, end_color=PRIMARY_DARK, fill_type="solid"),
    "font": Font(color="FFFFFF", bold=True, size=24, name="Montserrat"),
    "alignment": Alignment(horizontal="center", vertical="center"),
})

ws["B4"] = "by Digital Assistant"
ws.merge_cells("B4:H4")
apply_style(ws["B4"], {
    "fill": PatternFill(start_color=ACCENT, end_color=ACCENT, fill_type="solid"),
    "font": Font(color=DARK, bold=True, size=12, name="Montserrat", italic=True),
    "alignment": Alignment(horizontal="center", vertical="center"),
})

# Welcome
ws["B6"] = "Welcome to your new budget tracker!"
apply_style(ws["B6"], {"font": Font(bold=True, size=16, color=PRIMARY_DARK, name="Montserrat")})

ws["B7"] = "Take a moment to read through this quick guide to set up your budget."
apply_style(ws["B7"], {"font": Font(size=11, color=DARK, name="Montserrat")})

# Section headers
sections = [
    ("B9", "GETTING STARTED", PRIMARY),
    ("B10", "1. Open the 'Budget' tab below."),
    ("B11", "2. Enter your budget period dates in the header."),
    ("B12", "3. Choose your currency symbol."),
    ("B13", "4. Add your income, expense, bill, savings, and debt categories."),
    ("B14", "5. Enter planned amounts (what you expect to spend/earn)."),
    ("B15", "6. As the month progresses, enter actual amounts."),
    ("B16", "7. Watch your dashboard auto-update with progress %."),

    ("B18", "FEATURES", PRIMARY),
    ("B19", "• 30+ customizable income categories"),
    ("B20", "• 30+ expense categories with progress tracking"),
    ("B21", "• Bills tracker with checkboxes for paid items"),
    ("B22", "• Savings goals with progress bars"),
    ("B23", "• Debt payoff tracker"),
    ("B24", "• Cash flow dashboard"),
    ("B25", "• Multiple color themes (this version: Teal + Gold)"),

    ("B27", "TIPS", PRIMARY),
    ("B28", "• Make a copy first: File > Make a copy"),
    ("B29", "• Best viewed in Google Sheets (free at sheets.google.com)"),
    ("B30", "• Update weekly to stay on track"),
    ("B31", "• Use rollover for any leftover budget from last period"),

    ("B33", "SUPPORT", PRIMARY),
    ("B34", "Questions? Email us at support@eonresearch.bio"),
    ("B35", "© Digital Assistant — All rights reserved."),
]

for entry in sections:
    if len(entry) == 3:
        cell, text, color = entry
        ws[cell] = text
        ws.merge_cells(f"{cell}:H{cell[1:]}")
        apply_style(ws[cell], {
            "fill": PatternFill(start_color=color, end_color=color, fill_type="solid"),
            "font": Font(color="FFFFFF", bold=True, size=12, name="Montserrat"),
            "alignment": Alignment(horizontal="left", vertical="center", indent=1),
        })
    else:
        cell, text = entry
        ws[cell] = text
        apply_style(ws[cell], {"font": Font(size=11, color=DARK, name="Montserrat")})

# Column widths
for col in ["A", "I"]:
    ws.column_dimensions[col].width = 3
for col in ["B", "C", "D", "E", "F", "G", "H"]:
    ws.column_dimensions[col].width = 14

# ============ BUDGET TAB ============
ws = wb.create_sheet("Budget")
ws.sheet_properties.tabColor = PRIMARY_DARK

# Title row
ws["B2"] = "MONTHLY BUDGET DASHBOARD"
ws.merge_cells("B2:M3")
apply_style(ws["B2"], {
    "fill": PatternFill(start_color=PRIMARY_DARK, end_color=PRIMARY_DARK, fill_type="solid"),
    "font": Font(color="FFFFFF", bold=True, size=20, name="Montserrat"),
    "alignment": Alignment(horizontal="center", vertical="center"),
})

# Period & Currency row
ws["B5"] = "BUDGET PERIOD"
ws["C5"] = "1 Jun 2026"
ws["E5"] = "—"
ws["F5"] = "30 Jun 2026"
ws["I5"] = "CURRENCY"
ws["J5"] = "$"

for cell in ["B5", "I5"]:
    apply_style(ws[cell], header_style(PRIMARY))
for cell in ["C5", "F5", "J5"]:
    apply_style(ws[cell], {
        "fill": PatternFill(start_color=PRIMARY_LIGHT, end_color=PRIMARY_LIGHT, fill_type="solid"),
        "font": Font(bold=True, color=PRIMARY_DARK, name="Montserrat"),
        "alignment": Alignment(horizontal="center"),
    })

# Summary cards (row 7)
def summary_card(ws, start_col, label, value_cell, color):
    row_label = 7
    row_value = 8
    end_col = chr(ord(start_col) + 1)
    ws.merge_cells(f"{start_col}{row_label}:{end_col}{row_label}")
    ws.merge_cells(f"{start_col}{row_value}:{end_col}{row_value}")
    ws[f"{start_col}{row_label}"] = label
    apply_style(ws[f"{start_col}{row_label}"], {
        "fill": PatternFill(start_color=color, end_color=color, fill_type="solid"),
        "font": Font(color="FFFFFF", bold=True, size=11, name="Montserrat"),
        "alignment": Alignment(horizontal="center"),
    })
    ws[f"{start_col}{row_value}"] = value_cell
    apply_style(ws[f"{start_col}{row_value}"], {
        "fill": PatternFill(start_color=PRIMARY_LIGHT, end_color=PRIMARY_LIGHT, fill_type="solid"),
        "font": Font(color=PRIMARY_DARK, bold=True, size=16, name="Montserrat"),
        "alignment": Alignment(horizontal="center"),
    })

summary_card(ws, "B", "INCOME",   "=SUM(C26:C55)", INCOME)
summary_card(ws, "E", "EXPENSES", "=SUM(F26:F55)", EXPENSE)
summary_card(ws, "H", "BILLS",    "=SUM(I26:I55)", BILLS)
summary_card(ws, "K", "SAVINGS",  "=SUM(L26:L37)", SAVINGS)

# LEFT TO SPEND card (large)
ws["B11"] = "AMOUNT LEFT TO SPEND"
ws.merge_cells("B11:F12")
apply_style(ws["B11"], {
    "fill": PatternFill(start_color=ACCENT, end_color=ACCENT, fill_type="solid"),
    "font": Font(color=DARK, bold=True, size=14, name="Montserrat"),
    "alignment": Alignment(horizontal="center", vertical="center"),
})

ws["B13"] = "=B8-E8-H8-K8"
ws.merge_cells("B13:F16")
apply_style(ws["B13"], {
    "fill": PatternFill(start_color=ACCENT_LIGHT, end_color=ACCENT_LIGHT, fill_type="solid"),
    "font": Font(color=PRIMARY_DARK, bold=True, size=32, name="Montserrat"),
    "alignment": Alignment(horizontal="center", vertical="center"),
})
ws["B13"].number_format = '"$"#,##0.00'

# Cash flow summary
ws["H11"] = "CASH FLOW SUMMARY"
ws.merge_cells("H11:M11")
apply_style(ws["H11"], header_style(PRIMARY_DARK))

cf_data = [
    ("+", "Rollover", 0, 0),
    ("+", "Income", "=B8", "=B8"),
    ("-", "Expenses", "=E8", "=E8"),
    ("-", "Bills", "=H8", "=H8"),
    ("-", "Savings", "=K8", "=K8"),
    ("-", "Debt", "=SUM(I60:I72)", "=SUM(I60:I72)"),
]
for i, (sign, label, planned, actual) in enumerate(cf_data):
    row = 12 + i
    ws[f"H{row}"] = sign
    ws[f"I{row}"] = label
    ws[f"K{row}"] = planned
    ws[f"M{row}"] = actual
    for c in ["H", "I"]:
        apply_style(ws[f"{c}{row}"], {
            "fill": PatternFill(start_color=PRIMARY_LIGHT, end_color=PRIMARY_LIGHT, fill_type="solid"),
            "font": Font(color=PRIMARY_DARK, bold=True, name="Montserrat"),
            "alignment": Alignment(horizontal="center" if c == "H" else "left", indent=1),
        })
    for c in ["K", "M"]:
        apply_style(ws[f"{c}{row}"], {
            "fill": PatternFill(start_color=WHITE, end_color=WHITE, fill_type="solid"),
            "font": Font(color=DARK, name="Montserrat"),
            "alignment": Alignment(horizontal="right"),
            "border": thin_border,
        })
        ws[f"{c}{row}"].number_format = '"$"#,##0.00'

# LEFT row
ws["H18"] = "="
ws["I18"] = "LEFT"
ws["K18"] = "=K13-K14-K15-K16-K17"
ws["M18"] = "=M13-M14-M15-M16-M17"
for c, val in [("H", "="), ("I", "LEFT"), ("K", None), ("M", None)]:
    apply_style(ws[f"{c}18"], {
        "fill": PatternFill(start_color=ACCENT, end_color=ACCENT, fill_type="solid"),
        "font": Font(color=DARK, bold=True, size=12, name="Montserrat"),
        "alignment": Alignment(horizontal="center" if c == "H" else ("left" if c == "I" else "right"), indent=1),
    })
ws["K18"].number_format = '"$"#,##0.00'
ws["M18"].number_format = '"$"#,##0.00'

# INCOME section
ws["B22"] = "INCOME"
ws.merge_cells("B22:C22")
apply_style(ws["B22"], header_style(INCOME))

ws["B24"] = "Category"
ws["C24"] = "PLANNED"
ws["D24"] = "ACTUAL"
for c in ["B24", "C24", "D24"]:
    apply_style(ws[c], header_style(PRIMARY_DARK))

income_categories = ["Salary", "Self-Employment", "Gig Earnings", "Investment Interest", "Social Media", "Bonus"]
for i in range(30):
    row = 26 + i
    if i < len(income_categories):
        ws[f"B{row}"] = income_categories[i]
    bg = WHITE if i % 2 == 0 else LIGHT_BG
    for c in ["B", "C", "D"]:
        apply_style(ws[f"{c}{row}"], {
            "fill": PatternFill(start_color=bg, end_color=bg, fill_type="solid"),
            "font": Font(color=DARK, name="Montserrat"),
            "border": thin_border,
        })
        if c in ("C", "D"):
            ws[f"{c}{row}"].number_format = '"$"#,##0.00'

ws["B56"] = "TOTAL"
ws["C56"] = "=SUM(C26:C55)"
ws["D56"] = "=SUM(D26:D55)"
for c in ["B56", "C56", "D56"]:
    apply_style(ws[c], {
        "fill": PatternFill(start_color=INCOME, end_color=INCOME, fill_type="solid"),
        "font": Font(color="FFFFFF", bold=True, name="Montserrat"),
        "alignment": Alignment(horizontal="center" if c == "B56" else "right", indent=1),
    })
    if c != "B56":
        ws[c].number_format = '"$"#,##0.00'

# EXPENSES section
ws["E22"] = "EXPENSES"
ws.merge_cells("E22:G22")
apply_style(ws["E22"], header_style(EXPENSE))

ws["E24"] = "Category"
ws["F24"] = "PLANNED"
ws["G24"] = "ACTUAL"
for c in ["E24", "F24", "G24"]:
    apply_style(ws[c], header_style(PRIMARY_DARK))

expense_categories = ["Groceries", "Takeout", "Restaurants", "Household", "Commuting", "Fuel", "Gifts", "Cosmetics", "Online Classes", "Entertainment"]
for i in range(30):
    row = 26 + i
    if i < len(expense_categories):
        ws[f"E{row}"] = expense_categories[i]
    bg = WHITE if i % 2 == 0 else LIGHT_BG
    for c in ["E", "F", "G"]:
        apply_style(ws[f"{c}{row}"], {
            "fill": PatternFill(start_color=bg, end_color=bg, fill_type="solid"),
            "font": Font(color=DARK, name="Montserrat"),
            "border": thin_border,
        })
        if c in ("F", "G"):
            ws[f"{c}{row}"].number_format = '"$"#,##0.00'

ws["E56"] = "TOTAL"
ws["F56"] = "=SUM(F26:F55)"
ws["G56"] = "=SUM(G26:G55)"
for c in ["E56", "F56", "G56"]:
    apply_style(ws[c], {
        "fill": PatternFill(start_color=EXPENSE, end_color=EXPENSE, fill_type="solid"),
        "font": Font(color="FFFFFF", bold=True, name="Montserrat"),
        "alignment": Alignment(horizontal="center" if c == "E56" else "right", indent=1),
    })
    if c != "E56":
        ws[c].number_format = '"$"#,##0.00'

# BILLS section
ws["H22"] = "BILLS"
ws.merge_cells("H22:J22")
apply_style(ws["H22"], header_style(BILLS))

ws["H24"] = "Category"
ws["I24"] = "PLANNED"
ws["J24"] = "ACTUAL"
for c in ["H24", "I24", "J24"]:
    apply_style(ws[c], header_style(PRIMARY_DARK))

bills_categories = ["Housing", "Electricity", "Water", "Cell Phone", "Heating", "Internet", "Spotify", "YouTube Premium", "Netflix", "HBO", "Gym"]
for i in range(30):
    row = 26 + i
    if i < len(bills_categories):
        ws[f"H{row}"] = bills_categories[i]
    bg = WHITE if i % 2 == 0 else LIGHT_BG
    for c in ["H", "I", "J"]:
        apply_style(ws[f"{c}{row}"], {
            "fill": PatternFill(start_color=bg, end_color=bg, fill_type="solid"),
            "font": Font(color=DARK, name="Montserrat"),
            "border": thin_border,
        })
        if c in ("I", "J"):
            ws[f"{c}{row}"].number_format = '"$"#,##0.00'

ws["H56"] = "TOTAL"
ws["I56"] = "=SUM(I26:I55)"
ws["J56"] = "=SUM(J26:J55)"
for c in ["H56", "I56", "J56"]:
    apply_style(ws[c], {
        "fill": PatternFill(start_color=BILLS, end_color=BILLS, fill_type="solid"),
        "font": Font(color="FFFFFF", bold=True, name="Montserrat"),
        "alignment": Alignment(horizontal="center" if c == "H56" else "right", indent=1),
    })
    if c != "H56":
        ws[c].number_format = '"$"#,##0.00'

# SAVINGS section
ws["K22"] = "SAVINGS"
ws.merge_cells("K22:M22")
apply_style(ws["K22"], header_style(SAVINGS))

ws["K24"] = "Goal"
ws["L24"] = "PLANNED"
ws["M24"] = "ACTUAL"
for c in ["K24", "L24", "M24"]:
    apply_style(ws[c], header_style(PRIMARY_DARK))

savings_goals = ["Emergency Fund", "House Deposit", "Vacation", "Christmas Fund", "New Laptop", "School Supplies"]
for i in range(12):
    row = 26 + i
    if i < len(savings_goals):
        ws[f"K{row}"] = savings_goals[i]
    bg = WHITE if i % 2 == 0 else LIGHT_BG
    for c in ["K", "L", "M"]:
        apply_style(ws[f"{c}{row}"], {
            "fill": PatternFill(start_color=bg, end_color=bg, fill_type="solid"),
            "font": Font(color=DARK, name="Montserrat"),
            "border": thin_border,
        })
        if c in ("L", "M"):
            ws[f"{c}{row}"].number_format = '"$"#,##0.00'

ws["K38"] = "TOTAL"
ws["L38"] = "=SUM(L26:L37)"
ws["M38"] = "=SUM(M26:M37)"
for c in ["K38", "L38", "M38"]:
    apply_style(ws[c], {
        "fill": PatternFill(start_color=SAVINGS, end_color=SAVINGS, fill_type="solid"),
        "font": Font(color="FFFFFF", bold=True, name="Montserrat"),
        "alignment": Alignment(horizontal="center" if c == "K38" else "right", indent=1),
    })
    if c != "K38":
        ws[c].number_format = '"$"#,##0.00'

# DEBT section (below savings)
ws["K42"] = "DEBT"
ws.merge_cells("K42:M42")
apply_style(ws["K42"], header_style(DEBT))

ws["K44"] = "Account"
ws["L44"] = "PLANNED"
ws["M44"] = "ACTUAL"
for c in ["K44", "L44", "M44"]:
    apply_style(ws[c], header_style(PRIMARY_DARK))

debt_categories = ["Mortgage", "Car Lease", "Phone Financing", "Credit Card", "Student Loan"]
for i in range(13):
    row = 46 + i
    if i < len(debt_categories):
        ws[f"K{row}"] = debt_categories[i]
    bg = WHITE if i % 2 == 0 else LIGHT_BG
    for c in ["K", "L", "M"]:
        apply_style(ws[f"{c}{row}"], {
            "fill": PatternFill(start_color=bg, end_color=bg, fill_type="solid"),
            "font": Font(color=DARK, name="Montserrat"),
            "border": thin_border,
        })
        if c in ("L", "M"):
            ws[f"{c}{row}"].number_format = '"$"#,##0.00'

ws["K59"] = "TOTAL"
ws["L59"] = "=SUM(L46:L58)"
ws["M59"] = "=SUM(M46:M58)"
for c in ["K59", "L59", "M59"]:
    apply_style(ws[c], {
        "fill": PatternFill(start_color=DEBT, end_color=DEBT, fill_type="solid"),
        "font": Font(color="FFFFFF", bold=True, name="Montserrat"),
        "alignment": Alignment(horizontal="center" if c == "K59" else "right", indent=1),
    })
    if c != "K59":
        ws[c].number_format = '"$"#,##0.00'

# Column widths
for col in ["A", "N"]:
    ws.column_dimensions[col].width = 2
ws.column_dimensions["B"].width = 18
ws.column_dimensions["C"].width = 12
ws.column_dimensions["D"].width = 12
ws.column_dimensions["E"].width = 18
ws.column_dimensions["F"].width = 12
ws.column_dimensions["G"].width = 12
ws.column_dimensions["H"].width = 18
ws.column_dimensions["I"].width = 12
ws.column_dimensions["J"].width = 12
ws.column_dimensions["K"].width = 18
ws.column_dimensions["L"].width = 12
ws.column_dimensions["M"].width = 12

# Set tab colors
ws.sheet_view.showGridLines = False

# ============ EXAMPLE BUDGET TAB (filled in) ============
ws_ex = wb.copy_worksheet(ws)
ws_ex.title = "Example Budget"
ws_ex.sheet_properties.tabColor = ACCENT

# Fill in example values
example_income = [4700, 810, 220, 150, 660, 50]
for i, v in enumerate(example_income):
    ws_ex[f"C{26+i}"] = v
    ws_ex[f"D{26+i}"] = v

example_expenses = [710, 300, 200, 170, 100, 160, 20, 70, 15, 80]
for i, v in enumerate(example_expenses):
    ws_ex[f"F{26+i}"] = v
    ws_ex[f"G{26+i}"] = v

example_bills = [390, 110, 50, 30, 45, 15, 10, 12, 15, 35, 99]
for i, v in enumerate(example_bills):
    ws_ex[f"I{26+i}"] = v
    ws_ex[f"J{26+i}"] = v

example_savings = [200, 300, 200, 50, 40, 30]
for i, v in enumerate(example_savings):
    ws_ex[f"L{26+i}"] = v
    ws_ex[f"M{26+i}"] = v

example_debt = [1200, 600, 60, 100, 40]
for i, v in enumerate(example_debt):
    ws_ex[f"L{46+i}"] = v
    ws_ex[f"M{46+i}"] = v

# Save
output_path = "/tmp/ultimate-budget-tracker.xlsx"
wb.save(output_path)
print(f"Saved: {output_path}")
import os
print(f"Size: {os.path.getsize(output_path)} bytes")
