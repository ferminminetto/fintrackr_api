# fintrackr

This is a simple pet project created to help tracking my finances while training deploying AWS services in EC2 and RDS, and also storing statements in S3.

## Project Overview

- Expenses parser using Banco Galicia debit account statements from xlsx and VISA Credit Card statements from pdf.
- Report generation stored in AWS S3.
- Docker for containerization. Intended deploy in AWS EC2
- Basic health check endpoint for testing

## How to Run the Project

1. Clone this repository.
2. Ensure you have Docker installed.
3. Run the app with the following command: `docker-compose up`

### Testing

To run test with coverage, use: `python manage.py test`
