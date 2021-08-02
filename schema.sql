CREATE TABLE users (
	id SERIAL PRIMARY KEY,
  username TEXT UNIQUE,
	password_hash TEXT
);

CREATE TYPE room_status AS ENUM ('public', 'private');

CREATE TABLE rooms (
  id SERIAL PRIMARY KEY,
  name TEXT,
  description TEXT,
  status ROOM_STATUS,
  created_at TIMESTAMP,
  user_id INTEGER REFERENCES users
);

CREATE TABLE room_admins (
  user_id INTEGER REFERENCES users,
  room_id INTEGER REFERENCES rooms
);

CREATE TABLE threads (
  id SERIAL PRIMARY KEY,
  name TEXT,
  room_id INTEGER REFERENCES rooms,
  created_at TIMESTAMP
);

CREATE TABLE messages (
  id SERIAL PRIMARY KEY,
  content TEXT,
  thread_id INTEGER REFERENCES threads,
  created_at TIMESTAMP
);