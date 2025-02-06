# fintrackr

This is a simple pet project created as an excuse to explore and use **FastAPI**.

## Project Overview

- Expenses parser using Banco Galicia debit account statements from xlsx and VISA Credit Card statements from pdf.
- Report generation stored in AWS S3.
- Docker for containerization. Inteded deploy in AWS EC2
- Basic health check endpoint for testing

## How to Run the Project

1. Clone this repository.
2. Ensure you have Docker installed.
3. Run the app with the following command: `docker-compose up`

### Testing

To run test with coverage, use: `pytest --cov=.`

### Check the Docs

You can open the docs to see the available endpoints and a short description in `localhost:8000/docs`.