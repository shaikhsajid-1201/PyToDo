Sure, here is a sample GitHub README file for a Python MySQL Todo list application running on localhost and connected using a Docker container.

```markdown
# Python MySQL Todo List App

This repository contains a simple Todo List application built with Python and MySQL. The application runs on your localhost and connects to a MySQL database using Docker containers.

## Prerequisites

- Docker
- Python 3.10
- MySQL Server running on your localhost
```

## Setup

### Step 1: Clone the Repository

```sh
git clone https://github.com/yourusername/PyToDo.git
cd PyToDo
```

### Step 2: Build and Run the Docker Container

Build the Docker image and run the container:

```sh
docker build -t imagename .
```

### Step 3: Initialize the Database

Run the database initialization script:

```sh
docker -it --rm --name containername iamgename
```

## Project Structure

```
PyToDo/
│
├── utility/
│   ├── __init__.py
│   ├── mysqlconn.py
├── script.sql
├── main.py
├── .Dockerignore
├── Dockerfile
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.
