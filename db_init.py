import sqlite3
conn = sqlite3.connect('db/phishsim.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS recipients (id INTEGER PRIMARY KEY, email TEXT, token TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, token TEXT, event_type TEXT, ip TEXT, user_agent TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')
conn.commit()
conn.close()
print("DB initialized.")
