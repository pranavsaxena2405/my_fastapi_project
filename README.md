To run the FastAPI application described above, follow these steps:

### 1. **Set Up Your Environment**

1. **Clone the Repository**: If the project is hosted on a version control system like Git, clone it.
   ```bash
   git clone <repository-url>
   cd my_fastapi_project
   ```

2. **Install Dependencies**: You can use either `pip` or `Poetry` to install the required dependencies.

   - **Using pip**:
     ```bash
     pip install -r requirements.txt
     ```

   - **Using Poetry**:
     ```bash
     poetry install
     ```

3. **Set Up Environment Variables**: Create a `.env` file in the project root directory and configure it with your database URL and LLM API key.
   ```bash
   echo "DB_URL='postgresql://username:password@localhost/dbname'" >> .env
   echo "LLM_API_KEY='your-llm-api-key-here'" >> .env
   ```

### 2. **Run the Application Locally**

1. **Start the FastAPI Server**: You can run the server using `uvicorn`.
   - **Using pip**:
     ```bash
     uvicorn main:app --reload
     ```
   - **Using Poetry**:
     ```bash
     poetry run uvicorn main:app --reload
     ```

   - The `--reload` flag is useful during development as it automatically reloads the server when you make changes to your code.

2. **Access the API**: Once the server is running, you can access the API at `http://127.0.0.1:8000`.

3. **Test the Application**:
   - **Upload a CSV File**: You can use tools like Postman, cURL, or even the Swagger UI provided by FastAPI to test the upload functionality.
   - **Swagger UI**: Access it at `http://127.0.0.1:8000/docs`.

   For example, using `curl`:
   ```bash
   curl -X POST "http://127.0.0.1:8000/upload-csv/" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "file=@/path/to/your/file.csv"
   ```

### 3. **Running the Application with Docker**

If you'd like to run the application inside a Docker container:

1. **Build the Docker Image**:
   ```bash
   docker build -t my_fastapi_project .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -p 8000:80 my_fastapi_project
   ```

3. **Access the API**: Now, the API should be accessible at `http://127.0.0.1:8000`.

### 4. **Connecting to the Database**

Ensure your database is running and accessible at the `DB_URL` you provided. If you're using PostgreSQL, you can start it with:

```bash
docker run --name my_postgres -e POSTGRES_PASSWORD=yourpassword -d postgres
```

You might need to adjust your `DB_URL` in the `.env` file to match the connection details.

### 5. **Final Deployment**

For production, you can configure your FastAPI application to run behind a more robust web server like `gunicorn`:

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

This command starts the application with 4 worker processes. Adjust the number of workers based on your server's resources.
