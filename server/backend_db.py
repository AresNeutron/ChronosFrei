import sqlite3

class CalendarDB:
    """
    Clase para manejar las operaciones CRUD de la base de datos de un calendario.
    """
    def __init__(self, db_name="chronosfrei.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Crea la tabla 'events' si no existe."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                start_datetime DATETIME NOT NULL,
                end_datetime DATETIME NOT NULL,
                description TEXT,
                location TEXT,
                is_recurring BOOLEAN NOT NULL DEFAULT 0,
                recurrence_rule TEXT
            )
        ''')
        self.conn.commit()

    def add_event(self, title, start_dt, end_dt, description=None, location=None, is_recurring=False, recurrence_rule=None):
        """C (CREATE): Agrega un nuevo evento a la base de datos."""
        self.cursor.execute('''
            INSERT INTO events (title, start_datetime, end_datetime, description, location, is_recurring, recurrence_rule)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, start_dt, end_dt, description, location, is_recurring, recurrence_rule))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_events(self, start_date=None, end_date=None):
        """R (READ): Recupera eventos, opcionalmente filtrando por un rango de fechas."""
        query = 'SELECT * FROM events'
        params = []
        if start_date and end_date:
            query += ' WHERE date(start_datetime) BETWEEN ? AND ?'
            params.append(start_date)
            params.append(end_date)
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
        
    def update_event(self, event_id, title=None, start_dt=None, end_dt=None, description=None, location=None):
        """U (UPDATE): Actualiza un evento existente por su ID."""
        fields = []
        params = []
        if title is not None:
            fields.append('title = ?')
            params.append(title)
        if start_dt is not None:
            fields.append('start_datetime = ?')
            params.append(start_dt)
        if end_dt is not None:
            fields.append('end_datetime = ?')
            params.append(end_dt)
        if description is not None:
            fields.append('description = ?')
            params.append(description)
        if location is not None:
            fields.append('location = ?')
            params.append(location)
            
        if not fields:
            return False # No hay campos para actualizar

        query = f'UPDATE events SET {", ".join(fields)} WHERE id = ?'
        params.append(event_id)
        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def delete_event(self, event_id):
        """D (DELETE): Elimina un evento por su ID."""
        self.cursor.execute('DELETE FROM events WHERE id = ?', (event_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def close(self):
        """Cierra la conexión a la base de datos."""
        self.conn.close()
