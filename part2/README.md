# HBnB API

This is a project for a simplified version of an AirBnB-like application with an API built using Flask and Flask-RESTX. 

## Project Structure

- **app/**: Contains the core application code
    - **api/**: Contains API routes organized by version
    - **models/**: Contains business logic classes (e.g., User, Place, Review)
    - **services/**: Contains the Facade pattern to communicate between layers
    - **persistence/**: Contains the in-memory repository
- **run.py**: Entry point for running the Flask application
- **config.py**: Configuration for the application
- **requirements.txt**: Lists the required dependencies for the project

## Setup

1. Clone the repository
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt

