-- Table: users
DROP TABLE IF EXISTS users CASCADE;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

-- Type: task_status
DROP TYPE IF EXISTS TASK_STATUS CASCADE;

CREATE TYPE TASK_STATUS AS ENUM ('new', 'in progress', 'completed');

-- Table: status
DROP TABLE IF EXISTS status CASCADE;
CREATE TABLE status (
    id SERIAL PRIMARY KEY,
    name TASK_STATUS UNIQUE
);


-- Table: tasks
DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    description TEXT,
    status_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (status_id) REFERENCES status (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
      ON DELETE CASCADE
);
