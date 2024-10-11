import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# PostgreSQL connection details
DATABASE = 'data_WareHouse'
USER = 'postgres'
PASSWORD = 'ocho'
HOST = 'localhost'
PORT = '5432'

# Create SQLAlchemy engine
engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')

# List of table names
table_names = [
    'cheMed',
    'Doctorset',
    'EACHI',
    'lobelia4cosmetics',
    'yetenaweg',
]

# Function to clean data
def clean_data(df):
    df.drop_duplicates(inplace=True)
    df.fillna(method='ffill', inplace=True)
    # Additional standardization and validation steps go here
    return df

# Clean each table and store the cleaned data back to PostgreSQL
for table in table_names:
    try:
        df = pd.read_sql(f'SELECT * FROM {table}', engine)
        df_clean = clean_data(df)
        df_clean.to_sql(f'clean_{table}', engine, if_exists='replace', index=False)
        logger.info(f'Successfully cleaned data in table {table}')
    except Exception as e:
        logger.error(f'Error cleaning data in table {table}: {e}')