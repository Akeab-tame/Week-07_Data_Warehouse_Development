# Ethiopian Medical Business Data Warehouse

## Project Summary
This project focuses on developing a data warehouse to store information on Ethiopian medical businesses scraped from Telegram channels. The process includes building data scraping and collection pipelines, cleaning and transforming data, applying object detection with YOLO, and designing and implementing the data warehouse. The aim is to centralize the data for analysis, facilitating better decision-making.

## Overview
The goal of this data warehouse is to centralize and streamline data analysis, enabling the identification of trends, patterns, and correlations within the Ethiopian medical business sector. The project utilizes ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform) frameworks to ensure that data is properly cleaned, consistent, and ready for analysis.

## Table of Contents
- [Introduction](#Introduction)
- [Business Need](#business-need)
- [Objective](#Objective)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Data Scraping and Collection](#data-scraping-and-collection)
- [Data Cleaning and Transformation](#data-cleaning-and-transformation)
- [Object Detection using YOLO](#object-detection-using-yolo)
- [API Development with FastAPI](#api-development-with-fastapi)
- [Learning Outcomes](#learning-outcomes)
- [Competency Mapping](#competency-mapping)
- [References](#references)

## Introduction
Kara Solutions, a data science company, has assigned the task of building a scalable data warehouse to store data scraped from Telegram channels related to Ethiopian medical businesses. This warehouse will allow for comprehensive analysis and insights generation.

## Business Need

Kara Solutions requires a centralized data warehouse to store and analyze data on Ethiopian medical businesses. This structure will support detailed analysis to uncover valuable insights, improve decision-making, and optimize reporting and query efficiency.

## Objective
The key objectives of this project are:

- Building data scraping and collection pipelines
- Creating data cleaning and transformation processes
- Implementing object detection with YOLO
- Designing and deploying a data warehouse
- Integrating and enriching data for analysis
- Integrate and enrich data for comprehensive analysis.

## Project Structure

```bash
Data_warehouse_Development/
├── my_project/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py 
│   └── crud.py
│   
├── src/
│     ├── cleaning_raw_data.py
│     ├── main.py
│     ├── image_to csv_file.ipynb
│     ├── store_raw_data_sql.py //database.py
│     ├── image_scrapper.py 
├── requirements.txt
└── logs/
│    └── dbt.log
│    └── data_cleaning.log
│
├── telegram_data_scrapper/
├──   ├── Photos
│     ├── tele_scraper.py
│     ├── tele_scraper_lastid.py
│     ├── output/
│          └── data/...           
```
## Technologies Used

- Python
- BeautifulSoup
- Scrapy
- Selenium
- YOLO (You Only Look Once)
- PostgreSQL
- FastAPI
- DBT (Data Build Tool)
- SQLAlchemy
- Pydantic

## Setup and Installation

1. **Clone the repository:**
```bash
    git clone https://github.com/Akeab-tame/Week-07_Data_Warehouse_Development.git
    cd your-repo-name
```

2. **Install dependencies:**
```bash
    pip install -r requirements.txt
```

3. **Set up the database:**
    Configure your database connection in `database.py`.

## Tasks and Steps

## Data Scraping and Collection

1. **Telegram Scraping:**
    - Use the Telegram API or custom scripts to extract data from public Telegram channels.
    - Example channels:
        - [DoctorsET](https://t.me/DoctorsET)
        - [Chemed Telegram Channel](https://t.me/lobelia4cosmetics)
        - [EAHCI](https://t.me/EAHCI)

2. **Image and Data Scraping:**
    - Collect images from channels like [Chemed Telegram Channel](https://t.me/lobelia4cosmetics) for object detection.
    - Use Python packages like `telethon` for extraction.

## Data Cleaning and Transformation

1. **Data Cleaning:**
    - Remove duplicates, handle missing values, standardize formats, and validate data.

2. **DBT for Data Transformation:**
    - Install and set up DBT.
    - Define and run DBT models for data transformation.
    - Test and document transformations with DBT.

## Object Detection using YOLO

1. **Setting Up YOLO:**
    - Install dependencies like OpenCV, TensorFlow, or PyTorch.
    - Clone the YOLO repository and install requirements.
    
    ```sh
    git clone https://github.com/ultralytics/yolov5.git
    cd yolov5
    pip install -r requirements.txt
    ```

2. **Processing Detection Results:**
    - Extract data such as bounding box coordinates, confidence scores, and class labels.
    - Store detection data in a database table.

## API Development with FastAPI

1. **Setting Up FastAPI:**
    - Install FastAPI and Uvicorn.
    - Define project structure and configure the database using SQLAlchemy.

```bash
    pip install fastapi uvicorn
```

2. **Creating API Endpoints:**
    - Define SQLAlchemy models, Pydantic schemas, and CRUD operations.
    - Implement API endpoints in `main.py`.

## Learning Outcomes

- Telegram scraping using BeautifulSoup, Scrapy, and Selenium
- Object detection using YOLO
- Data cleaning and transformation using ETL processes
- Database schema design for data warehouses
- Implementing and configuring relational DBMS (e.g., PostgreSQL)
- Data integration and enrichment techniques
- End-to-end data pipeline development
- Testing and validation of data systems
- Deployment and maintenance of data warehouses

## Competency Mapping

- **Professionalism:** Articulating business values
- **Collaboration and Communication:** Reporting to stakeholders
- **Software Development Frameworks:** Using GitHub for CI/CD, writing modular codes, and packaging
- **Python Programming:** Advanced use of Python modules (Pandas, Matplotlib, Numpy, Scikit-learn, Prophet)
- **SQL Programming:** MySQL DB creation, reading, and writing
- **Data & Analytics Engineering:** Data filtering, transformation, and warehouse management
- **DBT:** ELT & ETL for data transformation
- **FastAPI:** Creating Python API

## References

- **Web Scraping:**
  - [Python Web Scraping](https://realpython.com/python-web-scraping-practical-introduction/)
  - [BeautifulSoup Web Scraper](https://realpython.com/beautiful-soup-web-scraper-python/)
  - [Scrapy](https://scrapy.org/)
  - [Selenium](https://www.selenium.dev/)
  - [Telethon Documentation](https://docs.telethon.dev/en/stable/)

- **DBT:**
  - [DBT](https://www.getdbt.com/)
  - [DBT Documentation](https://docs.getdbt.com/docs/introduction)

- **YOLO:**
  - [YOLOv5 GitHub](https://github.com/ultralytics/yolov5)
  - [YOLOv5 Tutorial](https://www.exxactcorp.com/blog/Deep-Learning/YOLOv5-PyTorch-Tutorial)

- **FastAPI:**
  - [FastAPI Documentation](https://fastapi.tiangolo.com/)
  - [FastAPI Tutorial](https://realpython.com/fastapi-python-web-apis/)
  - [Pydantic and FastAPI](https://medium.com/codenx/fastapi-pydantic-d809e046007f)

## Author: Aklilu Tamene
