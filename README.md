# Production Supervisor Morning Routine Automation

A comprehensive automation solution that streamlines the daily morning routine for production supervisors by integrating FoxPro data extraction with Microsoft Excel reporting.

## 🚀 Overview

This project automates the data collection and reporting workflow for production supervisors. It seamlessly bridges legacy FoxPro systems with modern Excel reporting by:
- Executing FoxPro PRG files to extract production data
- Processing and transforming extracted data
- Automatically updating Microsoft Excel workbooks with fresh data

## 📋 Prerequisites

- **Python**: Version 3.9 or higher
- **FoxPro** (optional): Required only for live data extraction
- **Microsoft Excel**: For report generation and viewing
- **Bash shell**: For executing FoxPro scripts (Windows: Git Bash or WSL)

## 🛠️ Installation

1. **Clone the repository**

   ```
   git clone https://github.com/hhannsterr/project_foxpro.git 
   cd project_foxpro
   ```

2. **Install dependecies**

    ```
    pip install -r requirements.txt
    ```
    📁 Project Structure
    ```.
    ├── fetch_data.sh
    ├── main.py 
    └── data
    ```

## 🚦 Usage
### Option 1: Live Data Extraction (with FoxPro)
1. Extract data from FoxPro:

    ```
    ./fetch_data.sh
    ```

    This executes the FoxPro PRG files and exports data to data/raw/ as text files.

2. Process data and update Excel:

    ```
    python main.py
    ```

### Option 2: Use Example Data (without FoxPro)
If you don't have FoxPro installed, use the provided example data:

```
python main.py
```
