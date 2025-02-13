# AI-Powered Chatbot for Supplier and Product Information
This project is an AI-powered chatbot built with Django, allowing users to query a product and supplier database using natural language processing (NLP). The chatbot fetches relevant data from a PostgreSQL database and summarizes the results using an open-source Large Language Model (LLM). The frontend uses HTML and Bootstrap, while the backend is powered by Python and Django.

## Features
- Natural language querying of products and suppliers.
- Retrieves data from a PostgreSQL database and provides summarized responses using an open-source LLM (e.g., Hugging Face's GPT-2, GPT-3, or LLaMA 2).
- Responsive web interface built with HTML and Bootstrap.
- Provides structured and concise responses to user queries.
- Gracefully handles missing or incorrect queries.

## Usage
### Basic setup and dependency management:
1. Install `pipenv` if you don't have it installed:
    ```bash
    pip install pipenv
    ```

2. Activate the virtual environment:
    ```bash
    pipenv shell
    ```

3. Install the required libraries:
    ```bash
    pipenv install
    ```

4. Set up the PostgreSQL database:
    - Ensure you have PostgreSQL installed and running.
    - Create a database and import the schema from the provided `db.sql` file to set up the necessary tables and data.
    ```bash
    psql -U postgres -f db.sql
    ```

### To run the application:
1. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

2. Access the application at `http://127.0.0.1:8000/` in your browser.

## File Structure:
- **manage.py**: The Django project management command-line utility.
- **AI_Chatbot**:
    - **settings.py**: Contains settings and configuration for the Django project, including database setup.
    - **urls.py**: The URL configuration for the project, mapping URLs to views.
    - **wsgi.py**: Helps serve the Django application in production.
    - **asgi.py**: Used to serve the application in an ASGI-compatible server.
- **Home**: Contains views and urls for mapping all homepage related functionalities.
- **Chatbot**: Contains views and urls for mapping all chatbot-related functionalities.
- **templates**: Contains HTML files for the whole project in a structured file directory (e.g., chatbot interface).
- **db.sql**: The PostgreSQL database schema and sample data script.
- **Pipfile**: Defines the dependencies used in the project.
- **Pipfile.lock**: Locks the dependencies to specific versions for consistency across environments.
