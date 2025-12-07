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
    python -m venv foxpro
    foxpro\Scripts\activate
    ```
    ```
    python -m pip install -r requirements.txt
    ```

## 🚦 Usage
### Initial Setup
1. **Create .env file following the provided example**

    ```
    example_env.txt
    ```
2. **Set date to the last day the data is updated**

    ```
    log.json
    ```
3. **Run Program**

    ```
    python main.py
    ```

### Subsequent Runs
1. **Date in log.json are updated automatically so you can just skip to the main program**

    ```
    python main.py
    ```
