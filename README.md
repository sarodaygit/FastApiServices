# FastApiServices

A FastAPI-based microservice for handling REST API requests, integrating with MongoDB, SQL Server, and supporting OpenTelemetry tracing.

## Features

- FastAPI web server with modular routers
- MongoDB integration (async with Motor)
- SQL Server integration (planned)
- Custom middleware for request timing
- Centralized configuration management
- Structured logging utility
- OpenTelemetry tracing with Jaeger exporter
- Docker support for easy deployment

## Project Structure

```
.
├── Deployment/           # Dockerfile and deployment scripts
├── Docs/                 # UML diagrams and documentation
├── Sources/              # Main source code
│   ├── FastApiServices/
│   │   ├── Conf/         # Configuration files
│   │   ├── Handlers/     # Middleware, error handling, telemetry
│   │   ├── Routers/      # API routers
│   │   ├── Stores/       # Database access (Mongo, SQLServer)
│   │   ├── Utils/        # Utilities (logging, config, JSON encoder)
│   │   └── main.py       # FastAPI app entry point
├── Tests/                # Unit and integration tests
├── cleancache.sh         # Script to clean Python cache files
├── launch.sh             # Script to build and run Docker container
└── README.md             # This file
```

## Getting Started

### Prerequisites

- Python 3.8+
- Docker (optional, for containerized deployment)
- MongoDB instance (local or remote)

### Installation

1. Clone the repository:
    ```sh
    git clone <repo-url>
    cd FastApiServices
    ```

2. Install dependencies:
    ```sh
    cd Sources
    pip install -r requirements.txt
    ```

3. Set environment variable for configuration (optional):
    ```sh
    export ENV=dev  # or prod
    ```

4. Run the FastAPI server:
    ```sh
    cd FastApiServices
    uvicorn main:app --host 0.0.0.0 --port 8004 --reload
    ```

### Required Environment Variables

Set the following environment variables before running the application:

- `ENV` — Application environment (e.g., `dev`, `prod`)
- `MONGO_CERT_PATH` — Path to MongoDB CA certificate file (required if SSL is enabled)

**Note:**  
If your MongoDB configuration has `UseSSL = true`, you must set `MONGO_CERT_PATH` to the path of your CA certificate file.  
If `MONGO_CERT_PATH` is not set and SSL is enabled, the application will raise an error.

Example:
```sh
export ENV=dev

export MONGO_CERT_PATH="/path/to/your/ca-certificate.crt"
### Running with Docker

```sh
./launch.sh
```

### Running Tests

```sh
cd Tests
pytest
```

## Configuration

Configuration files are located in `Sources/FastApiServices/Conf/`. The environment variable `ENV` selects which config file to use (`FastApiServices.dev.conf`, `FastApiServices.prod.conf`, etc).

## API Endpoints

- `/test` — Health check endpoint
- `/movies/count` — Get total movie count
- `/movies/latest` — Get the latest movie
- `/movies/highrated` — Get movies with IMDb rating > 9.0

## License

[MIT](LICENSE) (add your license file if needed)
```
```
FastApiServices
├─ Deployment
│  └─ Dockerfile
├─ Docs
│  ├─ Class_diagram.png
│  ├─ Class_diagrams.plantuml
│  ├─ sequence_diagrams.plantuml
│  └─ sequence_diagrams.png
├─ README.md
├─ Sources
│  ├─ .pylintrc
│  ├─ FastApiServices
│  │  ├─ Conf
│  │  │  ├─ FastApiServices.conf
│  │  │  ├─ FastApiServices.dev.conf
│  │  │  ├─ FastApiServices.prod copy.conf
│  │  │  ├─ FastApiServices.prod.conf
│  │  │  └─ __init__.py
│  │  ├─ FastApiServices.log
│  │  ├─ Handlers
│  │  │  ├─ ErrorCodes.py
│  │  │  ├─ FastApiServicesException.py
│  │  │  ├─ Middlewares.py
│  │  │  ├─ OpenTelemetryServices.py
│  │  │  └─ __init__.py
│  │  ├─ Routers
│  │  │  ├─ MovieStatsRouter.py
│  │  │  └─ __init__.py
│  │  ├─ Stores
│  │  │  ├─ Mongo
│  │  │  │  ├─ Models
│  │  │  │  │  ├─ MoviStats.py
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  └─ user.py
│  │  │  │  ├─ __init__.py
│  │  │  │  ├─ motorstore.py
│  │  │  │  └─ store.py
│  │  │  ├─ SQLServer
│  │  │  │  ├─ Models
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ __init__.py
│  │  │  │  └─ store.py
│  │  │  └─ __init__.py
│  │  ├─ Utils
│  │  │  ├─ ConfigParserUtil.py
│  │  │  ├─ JSONEncoder.py
│  │  │  ├─ LoggerUtil.py
│  │  │  └─ __init__.py
│  │  ├─ __init__.py
│  │  ├─ main.py
│  │  └─ run.sh
│  ├─ __init__.py
│  └─ requirements.txt
├─ Tests
│  ├─ __init__.py
│  └─ test_TestPlanner.py
├─ cleancache.sh
├─ launch.sh
└─ notes.txt

```