# CSV Analyzer with Django

This project is a web application for analyzing CSV files using Django. It allows users to upload a CSV file and provides various evaluation metrics for numerical columns, such as mean, standard deviation, heatmap, and density curve. The application uses pandas and seaborn for data analysis and visualization, and Django forms for handling file input. Tailwind CSS is used for styling.

## Features

- Upload a CSV file through a Django form.
- Analyze numerical columns with metrics including:
  - Mean
  - Standard Deviation
  - Heatmap
  - Density Curve
- Interactive and visually appealing output using Tailwind CSS.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Node.js and npm (for Tailwind CSS)

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/JainishParekh/CSV-Analysis.git
cd CSV-Analysis
```

### 2. Set Up the Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install Python Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Install Node.js Dependencies

Navigate to the Tailwind CSS setup folder (if separate) and install dependencies:

```bash
npm install
```

### 5. Run Migrations

Apply the migrations to set up the database:

```bash
python manage.py migrate
```

### 6. Start the Tailwind CSS Server

If Tailwind CSS is configured separately, start the Tailwind server:

```bash
python manage.py tailwind start
```

### 7. Run the Django Development Server

Start the Django development server:

```bash
python manage.py runserver
```

### 8. Access the Application

Open your web browser and navigate to:

```
http://127.0.0.1:8000/
```

### 9. Upload a CSV File

Use the provided form to upload a CSV file named `upload_file.csv` for testing. The application will analyze the numerical columns and display various metrics and visualizations.


## Acknowledgments

- Django: Web framework used for developing the application.
- pandas: Library used for data manipulation and analysis.
- seaborn: Library used for data visualization.
- Tailwind CSS: Utility-first CSS framework used for styling.
