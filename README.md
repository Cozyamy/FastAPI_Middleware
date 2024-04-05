# FastAPI File Upload Service

This project implements a FastAPI-based file upload service. It allows users to upload files and determines their MIME type. The service includes middleware for logging incoming requests.

## Installation

To install the dependencies, run:

```bash
poetry shell
poetry install
```

## Usage

### Running the Server

To start the FastAPI server, run:

```bash
uvicorn main:app --reload
```

### Endpoints

- **POST /upload/**: Upload a file and determine its MIME type.

## Project Structure

- **main.py**: Main entry point for the FastAPI application. Includes setup of routes and middleware.
- **routes.py**: Defines API endpoints and request handlers.
- **services.py**: Contains helper functions for processing files, such as determining their MIME type.
- **config.py**: Configures logging settings.
- **test_routes.py**: Contains test cases for API endpoints.

## Running Tests

To run tests, use PyTest:

```bash
pytest
```

## Dependencies

- FastAPI: Web framework for building APIs with Python.
- Magic: Library for detecting MIME types of files.