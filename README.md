# REST-PERSISTENT-DATA-API
Module 4 assignment 2
Working through the clinical API database issue helped me better
understand how application code and a database schema must stay
synchronized. I began by identifying the SQLite error and checking which
columns the SQLAlchemy model expected. Instead of repeatedly changing
code, the process evolved into directly inspecting the SQLite database
and confirming the exact database file being used. This revealed that
the heart_rate and temperature columns were missing from the
existing clinical_data table.

What surprised me most was that changing a SQLAlchemy model does not
automatically update an existing SQLite table. I also learned how
relative database paths can create confusion if scripts are run from
different directories. As the troubleshooting progressed, the code
became more focused on verification before modification, which made the
process safer and easier to understand.

I now understand database schemas, SQLAlchemy models, SQLite inspection,
and ALTER TABLE commands better. I would like to learn more about
database migrations with Alembic and how migrations are managed in
larger applications.

