# MiniProject1 - Customer Analytics EDA

## Overview
This project performs Exploratory Data Analysis (EDA) on a synthetic customer analytics dataset.

## Project Structure

- `data/` – contains the raw dataset file `customer_analytics.csv`.
- `notebooks/` – Jupyter notebooks used for exploration and analysis.
- `reports/` – scripts and generated PDF reports from the analysis.
- `requirements.txt` – Python dependencies required for running the code.

## Workflow

1. Data inspection and cleaning
2. Univariate and bivariate analysis
3. Correlation exploration and visualization
4. Compilation of results into a comprehensive PDF report

## Key Scripts

- `reports/generate_internship_report.py` – loads the data, cleans it, computes statistics, creates visualizations, reads notebook code, and compiles everything into a PDF using the `FPDF` library.
- `notebooks/MiniProject1_EDA.ipynb` – main notebook containing detailed exploratory analysis.

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Jupyter Notebook for interactive exploration:
   ```bash
   jupyter notebook
   ```
3. Or generate the final PDF report directly:
   ```bash
   python reports/generate_internship_report.py
   ```

Generated PDF will appear at `reports/Internship_MiniProject_Report_Final.pdf`.

## Notes

The report script handles missing values and duplicates automatically, and
outputs summary statistics, visualizations, and appended notebook code. Adjust
paths or parameters as needed for different datasets.
