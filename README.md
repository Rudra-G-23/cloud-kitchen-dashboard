# 🧑‍🍳 Cloud Kitchen Dashboard

An interactive dashboard built with **Streamlit** and **Plotly** to understand and analyze the Profit and Loss (PnL) of a Cloud Kitchen network. 

**Live**: https://cloud-kitchen-dashboard.streamlit.app

## 🚀 Features

- **Advanced Data Filtering**: Filter metrics by Month, Year, Store, City, Revenue Cohort, CM Cohort, EBITDA Range, and more.
- **Kitchen Level PnL**: View high-level metrics like Net Revenue, Gross Margin (GM), Contribution Margin (CM), and EBITDA. Dive deeper with tabular data for store-wise and month-wise summaries.
- **Variance Level PnL**: Analyze financial variance grouped by predefined categories (Low to High) and visualize it across different revenue cohorts and store counts.
- **Interactive Visualizations**: A comprehensive suite of interactive graphs, including:
  - Monthly Revenue Trends (Line Charts)
  - GM vs CM vs EBITDA comparisons (Bar Charts)
  - Revenue vs EBITDA (Scatter Plots)
  - Variance Heatmaps and Box Plots
  - Store-level breakdowns (Sunburst & Treemap charts)
- **Data Export**: Export your filtered datasets as CSV for external analysis.

## 📈 Dashboard 

https://github.com/user-attachments/assets/70c335cf-664a-4320-92c2-2876a2b55fb6


## 🛠️ Technology Stack

- **Python 3.11+**
- **Streamlit**: For building the interactive web application.
- **Pandas**: For robust data manipulation and aggregation.
- **Plotly**: For rich, interactive data visualizations.
- **OpenPyXL**: For reading Excel dataset files.

## 📦 Installation & Setup

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/Rudra-G-23/cloud-kitchen-dashboard.git
   cd cloud-kitchen-dashboard
   ```

2. **Set up a virtual environment (optional but recommended)**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install the dependencies**:
   This project uses a `pyproject.toml`. You can install the dependencies via `pip`:
   ```bash
   pip install -e .
   ```
   *Alternatively, install the required packages manually:*
   ```bash
   pip install streamlit pandas plotly openpyxl matplotlib numpy seaborn
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

## 📊 Data Source

The app relies on kitchen PnL data stored in an Excel file (`kittchen-pnl-data.xlsx`).
- By default, it looks for the file locally in the project directory.
- If the local file is not found, it gracefully falls back to fetching the data from the remote GitHub repository.

## 📁 Project Structure

- `app.py`: The main Streamlit application script containing all the data processing, UI layouts, and charts.
- `pyproject.toml`: The project configuration and dependency specification.
- `kittchen-pnl-data.xlsx`: The dataset used for populating the dashboard.
- `kitchen-analysis.ipynb`: A Jupyter Notebook for exploratory data analysis (EDA).

## 📄 License

This project is licensed under the terms specified in the `LICENSE` file.


Connect with me: https://rudra-g-23.github.io/
