from fastapi import FastAPI, File, UploadFile, Depends
from sqlalchemy import Table, Column, String, Boolean
from db import engine, get_db, metadata
from utils import process_csv, classify_company

app = FastAPI()

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...), db=Depends(get_db)):
    # Process CSV
    df = process_csv(file)

    # Create new column "Technology Company"
    df["Technology Company"] = df["Description"].apply(classify_company)

    # Dynamically create the table schema
    columns = []
    for col_name in df.columns:
        if col_name == "Technology Company":
            columns.append(Column(col_name, String))
        else:
            columns.append(Column(col_name, String))

    # Define the table
    table = Table("companies", metadata, *columns)

    # Create the table in the database
    metadata.create_all(bind=engine)

    return {"message": "Table created successfully with columns: " + ", ".join(df.columns)}

@app.get("/")
def read_root():
    return {"message": "Welcome to the ListenBravo Backend Assignment API!"}
