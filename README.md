# KavtechHRM_backend

The **Django REST API for Kavtech HRM**, an HR / recruitment portal. It provides account registration, token-based login/logout and an HR profile record for each user, and is consumed by the React front-ends [Kav_HRM_Frontend](https://github.com/SanaAkram/Kav_HRM_Frontend) and [KavHRM_frontend](https://github.com/SanaAkram/KavHRM_frontend).

## API

All routes are served from the site root.

| Method | Endpoint | Purpose |
|---|---|---|
| `POST` | `/Kavtech/register/` | Register — body `username`, `email` (unique), `password`; returns the created user (id, username, email) |
| `POST` | `/Kavtech/login/` | Log in with username + password; returns a **Knox** auth token |
| `POST` | `/Kavtech/logout/` | Invalidate the current token (`Authorization: Token <token>`) |
| `POST` | `/Kavtech/logoutall/` | Invalidate every token of the user (log out of all devices) |
| `POST` | `/Kavtech/kavprof/` | Create an HR profile — `first_name`, `last_name`, `usertype` (user id), `experience`, `location`, `birth_date` |
| — | `/admin/` | Django admin |

```bash
curl -X POST http://127.0.0.1:8000/Kavtech/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"sana","email":"sana@example.com","password":"S3cret!"}'
```

## Data model

```
CustomUser (username, email, password)  1 ───< KavProf (first_name, last_name, experience, location, birth_date)
                                               table: account_kavprof
```

## Architecture

```
React front-end ──JSON──► KavtechHRM/urls.py ──► accounts/urls.py
                                                   ├─ RegisterAPI  ─► RegisterSerializer ─► CustomUser
                                                   ├─ LoginAPI     ─► django-rest-knox token
                                                   ├─ Logout / LogoutAll (knox views)
                                                   └─ KavprofAPI   ─► KavprofSerializer ─► KavProf
                                                                              │
                                                                              ▼
                                                                    PostgreSQL "kavHRM"
```

| Path | Role |
|---|---|
| `KavtechHRM/` | Django project — settings (database, CORS, DRF), urls, wsgi/asgi |
| `accounts/` | The app: `models.py`, `serializers.py`, `views.py`, `urls.py` |
| `kavHRM` | A SQLite database file kept from development (the configured database is PostgreSQL) |
| `manage.py` | Django entry point |

## Stack

- Python 3.8+, Django, **Django REST Framework**
- **django-rest-knox** — token authentication
- **django-cors-headers** — lets the React app on another port call the API
- **PostgreSQL** via `psycopg2`

## Setup

There is no `requirements.txt`; install the dependencies the code imports:

```bash
git clone https://github.com/SanaAkram/KavtechHRM_backend.git
cd KavtechHRM_backend

python -m venv venv
# Windows:      venv\Scripts\activate
# macOS/Linux:  source venv/bin/activate

pip install django djangorestframework django-rest-knox django-cors-headers psycopg2-binary
```

### Database connection

```sql
CREATE DATABASE "kavHRM";
```

Then set `DATABASES` in `KavtechHRM/settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "kavHRM",
        "USER": "<your-postgres-user>",
        "PASSWORD": "<your-postgres-password>",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```

Never commit the real password — read it from an environment variable in your own settings.

### Run

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver          # API on http://127.0.0.1:8000/
```

Allow your front-end origin in the CORS settings (currently `CORS_ALLOW_ALL_ORIGINS = True`, fine for development only).

## Known gaps

- **Two user tables:** `/register/` writes to the app's own `CustomUser` table, while `/login/` authenticates against **Django's built-in `auth.User`** (that is what Knox's `AuthTokenSerializer` checks). Users created with `createsuperuser`/the admin can log in; users created through `/register/` cannot until registration is changed to create an `auth.User` (e.g. `User.objects.create_user(...)`).
- `CustomUser.password` is stored as sent (not hashed) — use `create_user` so passwords are hashed.
- The front-end posts profile data to `/Kavtech/profile/`, but the API exposes it at `/Kavtech/kavprof/`.
- The front-ends send `email` + `password` to `/login/`, but Knox's `AuthTokenSerializer` expects `username` + `password`.
- `RegisterAPI` does not return a token, and `KavprofAPI` does not yet require authentication.
