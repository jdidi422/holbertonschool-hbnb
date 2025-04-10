# HBNB Project

## Overview

This project is a simple web application designed as part of the HBNB project, following a modular structure with clear separation of concerns for various components such as API endpoints, models, services, and persistence. The goal is to create a functional backend API for a rental platform, allowing users to interact with places, reviews, amenities, and more.

## Project Structure

The project is organized into the following directories:
### Detailed Breakdown of Directories and Files
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md

#### app/
This directory contains the core components of the application.

- **__init__.py**: Initializes the app module.
  
- **api/**: Contains the API routes and handlers.
  - **v1/**: API version 1 endpoints.
    - **users.py**: Routes and logic related to user management.
    - **places.py**: Routes for managing places.
    - **auth.py**: Authentication logic and routes.
    - **reviews.py**: Routes for managing reviews.
    - **amenities.py**: Routes for managing amenities.

- **models/**: Contains the data models and base classes.
  - **user.py**: User model.
  - **place.py**: Place model.
  - **base_model.py**: Base model with common fields and methods.
  - **review.py**: Review model.
  - **amenity.py**: Amenity model.

- **services/**: Service layer that encapsulates the business logic.
  - **facade.py**: A central service module for managing various business logic.

- **persistence/**: Manages database interactions.
  - **repository.py**: Contains the logic for interacting with the database for CRUD operations.

#### Root Files

- **run.py**: Entry point to start the application.
  
- **config.py**: Configuration settings for the app, such as database settings and app configurations.

- **requirements.txt**: List of Python dependencies required to run the application.

- **README.md**: Project documentation (this file).

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/jdidi422/holbertonschool-hbnb.git