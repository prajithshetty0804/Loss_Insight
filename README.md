# Loss Insights

A web-based analytics application to track, analyze, and compare weekly losses across multiple Plants and Business Groups.

## Project Overview
Loss Insights enables management teams to identify:
- Weekly loss patterns
- Trends across Plants and Business Units
- Current vs previous week performance
- Actionable insights using data analytics

## Tech Stack
- Python, Django, Django REST Framework
- PostgreSQL
- Azure Pipelines (CI)
- Git / Version Control
- Agile & Scrum

## Features
- REST APIs for loss summary
- Serializer-driven data transformation
- Unit testing structure
- Modular Django app architecture

## Repository Structure
```
loss_insights/
│
├── loss_insights/
│   └── urls.py
│
├── insights/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── azure-pipelines.yml
├── requirements.txt
└── README.md
```

## How to Run
```
pip install -r requirements.txt
python manage.py runserver
```

## API Endpoint
GET /api/v1/weekly-loss/

