# Fitzone Pro

A responsive gym website and Oracle-backed Flask starter application. The public website is ready to preview; account registration, login, enquiries, and initial admin analytics use parameterized Oracle operations. The database connection is real and is not replaced with sample data. The admin account must be provisioned by the database owner.

## Requirements

- Python 3.10+
- Oracle Database with a schema/user that can create tables, sequences, triggers, and PL/SQL procedures
- Oracle Instant Client only if your Oracle setup requires thick mode (python-oracledb thin mode is the default)

## Setup

1. Create and activate a virtual environment, then install dependencies:

   ```powershell
   py -3 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env`. Set a unique `FLASK_SECRET_KEY`, Oracle credentials, DSN, and currency. Do not commit `.env`.
3. Connect to the Oracle application schema and run `database/schema.sql`, then `database/functions.sql` and `database/procedures.sql` using SQLcl, SQL*Plus, or SQL Developer. The trailing `/` lines are SQL*Plus script delimiters.
4. Optionally run `database/sample_data.sql` for the starter membership-plan catalog.
5. Create the first admin interactively; the script prompts securely and stores only a Werkzeug password hash:

   ```powershell
   python -m backend.create_admin
   ```
6. Start the server:

   ```powershell
   python -m backend.app
   ```
7. Open `http://127.0.0.1:5000`. Check `/health` for the HTTP process status. Database-backed pages report connection errors if Oracle is not configured.

## Current functionality

- Mobile-friendly public landing page with programs, coaches, class schedule, memberships, testimonials, and enquiry form.
- Member registration and login with Werkzeug password hashing and server-side role checks.
- Oracle schema, constraints, sequences, audit triggers, PL/SQL membership/payment operations, and analytics functions.
- Admin overview and Plotly revenue, plan, and payment charts backed by Oracle query results.
- Oracle-backed enquiry capture.
- Member dashboard with membership, payment history, and upcoming club schedule data.
- NumPy payment summaries, Pandas payment/revenue reports, Seaborn revenue chart export, and an optional Tkinter admin member-search client.

## Security and production notes

- Use HTTPS and set `COOKIE_SECURE=true`; use a long random secret key and restrict access to the `.env` file.
- Flask's built-in session cookie is HTTP-only and SameSite=Lax. State-changing API calls should additionally be protected with CSRF tokens before public production deployment; configure trusted origins and rate limiting at the production edge.
- Create the initial admin account via a one-time trusted administrative process and a strong password hash. The public registration endpoint only creates member-role accounts.
- Run behind a production WSGI server; the built-in Flask server is for local development only.
- Update the sample contact details, class times, membership prices, and currency to match your actual club before publishing.

## Current scope

The public website is designed as a responsive first phase. The connected app includes account registration/login, member read-only self-service, enquiry capture, admin metrics/member listing, and three live analytics charts. Complete administrator CRUD for member, trainer, plan, payment, and enquiry records, password reset and CSRF workflow, the full Plotly chart set, and richer Seaborn statistical reports remain to be implemented before treating this as a production-ready full gym-management suite. The sample timetable and quoted testimonial are presentation content, not database claims.
