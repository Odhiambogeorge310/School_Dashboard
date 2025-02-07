# IMMACULATE SCHOOL DASHBOARD

## Description

This project is a Streamlit-based interactive dashboard for visualizing student data at Immaculate School. It allows users to filter students by gender, grade, stream, and citizenship while providing key insights and visual representations of the student distribution.

## Features

- **Data Filtering:** Users can filter students based on gender, grade, stream, and citizenship.
- **Key Performance Indicators (KPIs):** Displays counts of boys, girls, total students, citizens, and foreigners.
- **Data Visualizations:**
  - Pie charts for gender distribution.
  - Histograms for gender-based distribution.
  - Interactive selection of grade levels.
- **Dynamic Table:** Displays filtered student data.

## Requirements

- Python 3.x
- Streamlit
- Pandas
- NumPy
- Plotly

## Installation

1. Clone this repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run learners.py
   ```
2. Open the provided URL in your browser to interact with the dashboard.

## File Structure

- `learners.py` - Main script for the Streamlit dashboard.
- `learners.xlsx` - Excel file containing student data.

## Notes

- Ensure the `learners.xlsx` file is in the same directory as `learners.py`.
- The application caches the dataset for better performance.

## License

This project is for educational purposes only.

## Author

[GEORGE ODHIAMBO]


