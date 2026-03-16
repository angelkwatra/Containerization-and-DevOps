-- Optional: Create tables or insert initial data if needed
-- The application will also create tables via SQLAlchemy
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE
);

-- Insert sample data
INSERT INTO tasks (title, description, completed) VALUES 
('Setup Project', 'Create directory structure and backend files', TRUE),
('Dockerize', 'Write Dockerfiles and compose file', FALSE),
('Networking', 'Configure Macvlan/Ipvlan', FALSE);
