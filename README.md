# ReviewsAnalyzeAI_petproject
REST API built with **FastAPI**, PostgreSQL, Bearer Token authentication, and external API integration.

---

## 📁 Project Structure

```
ReviewsAnalyzeAI_petproject/
├── Database/
│   ├── database.py          # PostgreSQL connection
│   └── models.py            # SQLAlchemy models
├── Exceptions/
│   ├── handler.py           # Global error handlers
│   └── Service.py           # Service layer exceptions
├── migrations/              # Alembic migrations
│   └── versions/
│       ├── 83cd3e0673cc_init.py
│       └── fa1e813603cd_init.py
├── Repository/
│   ├── ProductRepository.py # Product repository
│   └── ReviewRepository.py  # Review repository
├── AI.py                    # External AI API integration
├── alembic.ini              # Alembic configuration
├── config.py                # App settings
├── Deps.py                  # Dependency Injection
├── main.py                  # FastAPI entry point
├── router.py                # Router
├── Service.py               # Business logic
├── .env.example             # Environment variables template
└── README.md
```

---

## 🚀 Endpoints

| Method | Path                 | Description              |
|--------|----------------------|--------------------------|
| `POST` | `/CreateProduct`     | Create a new product     |
| `POST` | `/CreateReview`      | Create a review          |
| `GET`  | `/get_reviews_by_id` | Get reviews by ID        |
| `POST` | `/get`               | Get detailed item info   |
| `GET`  | `/`                  | Health check             |

Swagger UI available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/DDJEDD/ReviewsAnalyzeAI_petproject
cd ReviewsAnalyzeAI_petproject
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Refactor `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

```env
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_db
DB_PORT=5432
DB_HOST=localhost
BEARER_TOKEN=your_bearer_token
API_URL=https://your-external-api.com
```

### 5. Apply migrations

```bash
alembic upgrade head
```

### 6. Run the server

```bash
uvicorn main:app --reload
```

Server will start at `http://127.0.0.1:8000`

---

## 🗄️ Requirements

- Python 3.10+
- PostgreSQL
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)

---

## 🔐 Authentication

The API uses **Bearer Token** authentication for Hugging Face API. Set your token in the `BEARER_TOKEN` environment variable and pass it in request headers:

```
Authorization: Bearer <your_token>
```

---

## 📝 Environment Variables

| Variable            | Description                                 |
|---------------------|---------------------------------------------|
| `POSTGRES_USER`     | PostgreSQL username                         |
| `POSTGRES_PASSWORD` | PostgreSQL password                         |
| `POSTGRES_DB`       | Database name                               |
| `DB_PORT`           | PostgreSQL port (default: 5432)             |
| `DB_HOST`           | PostgreSQL host                             |
| `BEARER_TOKEN`      | Bearer token for H.F                        |
| `API_URL`           | Hugging Face URL(recommended to not change) |
