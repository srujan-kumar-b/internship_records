import pandas as pd
import numpy as np
import os
import json
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF

# --------------------------------------------------
# PATH CONFIGURATION
# --------------------------------------------------

DATA_PATH = "../data/customer_analytics.csv"
NOTEBOOK_PATH = "../notebooks/MiniProject1_EDA.ipynb"

REPORT_FOLDER = "reports"
OUTPUT_PATH = f"{REPORT_FOLDER}/Internship_MiniProject_Report_Final.pdf"

os.makedirs(REPORT_FOLDER, exist_ok=True)

# --------------------------------------------------
# PDF CLASS
# --------------------------------------------------

class InternshipPDF(FPDF):

    show_header = True

    def header(self):
        if self.show_header and self.page_no() == 1:
            self.set_y(5)
            self.set_font('Arial', 'B', 14)
            self.cell(0, 8, 'Customer Analytics Internship Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-10)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 8, f'Page {self.page_no()}', 0, 0, 'C')

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv(DATA_PATH)

original_rows, original_cols = df.shape
missing_total = df.isnull().sum().sum()
duplicate_rows = df.duplicated().sum()

# --------------------------------------------------
# DATA CLEANING
# --------------------------------------------------

for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

df = df.drop_duplicates()
cleaned_rows = df.shape[0]

# --------------------------------------------------
# STATISTICS
# --------------------------------------------------

numerical_df = df.select_dtypes(include=np.number)
mean_values = numerical_df.mean().round(2)
std_values = numerical_df.std().round(2)

corr_matrix = numerical_df.corr().round(2)
corr_unstacked = corr_matrix.unstack()
corr_unstacked = corr_unstacked[corr_unstacked < 1]
strongest_corr = corr_unstacked.sort_values(ascending=False).head(1)

strong_pair = strongest_corr.index[0]
strong_value = strongest_corr.iloc[0]

# --------------------------------------------------
# GENERATE CHARTS
# --------------------------------------------------

sns.set_style("whitegrid")

def save_plot(name):
    path = f"{REPORT_FOLDER}/{name}"
    plt.savefig(path, bbox_inches="tight")
    plt.close()
    return path

plt.figure(figsize=(6,4))
sns.histplot(df["Age"], kde=True)
plt.title("Age Distribution")
age_chart = save_plot("age_distribution.png")

plt.figure(figsize=(6,4))
sns.histplot(df["AnnualIncome"], kde=True)
plt.title("Annual Income Distribution")
income_chart = save_plot("income_distribution.png")

plt.figure(figsize=(6,4))
sns.scatterplot(x="AnnualIncome", y="SpendingScore", data=df)
plt.title("Income vs Spending Score")
scatter_chart = save_plot("income_vs_spending.png")

plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
heatmap_chart = save_plot("correlation_heatmap.png")

# --------------------------------------------------
# READ NOTEBOOK CODE & README
# --------------------------------------------------

notebook_code = ""
readme_text = ""

if os.path.exists(NOTEBOOK_PATH):
    with open(NOTEBOOK_PATH, "r", encoding="utf-8") as f:
        notebook = json.load(f)
        for cell in notebook.get("cells", []):
            if cell.get("cell_type") == "code":
                notebook_code += "".join(cell.get("source", []))
                notebook_code += "\n\n"
else:
    notebook_code = "Notebook file not found."

readme_path = os.path.join("..", "readme.md")
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        readme_text = f.read()
else:
    readme_text = "README.md file not found."

# --------------------------------------------------
# CREATE PDF
# --------------------------------------------------

import unicodedata

def sanitize(text):
    return unicodedata.normalize("NFKD", text).encode("latin-1", "ignore").decode("latin-1")

pdf = InternshipPDF()
pdf.set_auto_page_break(auto=True, margin=10)
pdf.set_margins(15, 5, 15)   # Reduced top margin
pdf.add_page()
pdf.set_font("Arial", "", 12)

# -------------------- 1. DATASET OVERVIEW --------------------

pdf.set_font("Arial", "B", 12)
pdf.cell(0, 8, "1. Dataset Overview", ln=True)
pdf.set_font("Arial", "", 12)

pdf.multi_cell(0, 8,
    "This section provides an overview of the customer analytics dataset used "
    "for the exploratory data analysis (EDA). The dataset contains demographic "
    "and financial attributes of customers which are essential for understanding "
    "consumer spending behavior. During preprocessing, missing values were "
    "handled using statistical imputation techniques and duplicate records "
    "were removed to improve overall data quality and reliability."
)

pdf.ln(3)

pdf.multi_cell(0, 8, f"Original Records: {original_rows}")
pdf.multi_cell(0, 8, f"Missing Values Identified: {missing_total}")
pdf.multi_cell(0, 8, f"Duplicate Records Removed: {duplicate_rows}")
pdf.multi_cell(0, 8, f"Final Cleaned Records: {cleaned_rows}")

pdf.ln(8)

# -------------------- 2. STATISTICAL SUMMARY --------------------

pdf.set_font("Arial", "B", 12)
pdf.cell(0, 8, "2. Statistical Summary", ln=True)
pdf.set_font("Arial", "", 12)

pdf.multi_cell(0, 8,
    "Statistical measures were calculated for all numerical features to "
    "understand their distribution and variability. The mean values represent "
    "average customer characteristics, while the standard deviation highlights "
    "how spread out the data points are. These metrics help in identifying "
    "consistency patterns and potential outliers within customer income "
    "and spending behavior."
)

pdf.ln(3)

for col in mean_values.index:
    pdf.multi_cell(
        0, 8,
        f"{col} -> Mean: {mean_values[col]}, Std Dev: {std_values[col]}"
    )

pdf.ln(3)

pdf.multi_cell(
    0, 8,
    f"Strongest Correlation Identified: {strong_pair[0]} & {strong_pair[1]} "
    f"(Correlation Coefficient: {strong_value})"
)

pdf.ln(8)

# -------------------- 3. VISUALIZATIONS --------------------

pdf.set_font("Arial", "B", 12)
pdf.cell(0, 8, "3. Visualizations", ln=True)
pdf.set_font("Arial", "", 12)

pdf.ln(5)

img_width = 130
x_position = (pdf.w - img_width) / 2

pdf.image(age_chart, x=x_position, w=img_width)
pdf.ln(5)
pdf.image(income_chart, x=x_position, w=img_width)
pdf.ln(5)
pdf.image(scatter_chart, x=x_position, w=img_width)
pdf.ln(5)
pdf.image(heatmap_chart, x=x_position, w=img_width)

pdf.ln(8)

# -------------------- 4. CONCLUSION --------------------

pdf.set_font("Arial", "B", 12)
pdf.cell(0, 8, "4. Conclusion", ln=True)
pdf.set_font("Arial", "", 12)

pdf.multi_cell(0, 8,
    "The exploratory data analysis successfully identified meaningful patterns "
    "within the customer dataset. Visual analysis revealed clear income and "
    "spending trends among customers. Correlation findings highlighted "
    "significant relationships between key attributes. Overall, this analysis "
    "provides valuable insights that can support data-driven marketing "
    "strategies and customer segmentation decisions."
)

# -------------------- APPENDIX --------------------

pdf.show_header = False
pdf.add_page()
pdf.set_y(5)

pdf.set_font("Arial", "B", 12)
pdf.cell(0, 8, "Appendix A: Notebook Code", ln=True)

pdf.set_font("Courier", "", 8)

for line in notebook_code.splitlines():
    pdf.multi_cell(0, 5, sanitize(line))

# ---------- APPENDIX B ----------

# directly continue after Appendix A content
pdf.ln(5)
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 8, "Appendix B: README", ln=True)

pdf.set_font("Arial", "", 10)

for line in readme_text.splitlines():
    pdf.multi_cell(0, 5, sanitize(line))

pdf.output(OUTPUT_PATH)

print("✅ FINAL Internship Report Generated Successfully!")
print(f"📄 Saved at: {OUTPUT_PATH}")