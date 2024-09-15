-- Check if database exists before creating it
DO
$$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'flask_auth_db') THEN
        PERFORM pg_terminate_backend (pg_stat_activity.pid)
        FROM pg_stat_activity
        WHERE datname = 'flask_auth_db';
        EXECUTE 'CREATE DATABASE flask_auth_db';
    END IF;
END
$$;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(120) NOT NULL
);