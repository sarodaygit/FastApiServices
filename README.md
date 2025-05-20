
```
FastApiServices
├─ .gitignore
├─ .vscode
│  └─ launch.json
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
│  │  │  └─ __init__.py
│  │  ├─ Handlers
│  │  │  ├─ DuneFastApiServicesException.py
│  │  │  ├─ ErrorCodes.py
│  │  │  ├─ Middlewares.py
│  │  │  ├─ OpenTelemetryServices.py
│  │  │  └─ __init__.py
│  │  ├─ Routers
│  │  │  ├─ LegacyPiTicketsMotorRouter.py
│  │  │  ├─ RegressionConfigMotorRouter.py
│  │  │  ├─ RegressionConfigRouter.py
│  │  │  ├─ TestPlannerRouter.py
│  │  │  └─ __init__.py
│  │  ├─ Stores
│  │  │  ├─ Mongo
│  │  │  │  ├─ Models
│  │  │  │  │  ├─ LegacyPiTickets.py
│  │  │  │  │  ├─ LegacyPiTicketsMotor.py
│  │  │  │  │  ├─ RegressionConfig.py
│  │  │  │  │  ├─ RegressionConfigMotor.py
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
│  ├─ __init__.py
│  └─ requirements.txt
├─ Tests
│  ├─ __init__.py
│  └─ test_TestPlanner.py
└─ launch.sh

```