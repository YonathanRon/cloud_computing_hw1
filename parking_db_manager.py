import sqlite3 as sql

DB_NAME = 'parking_records.db'


def create_db():
    conn = sql.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        f'CREATE TABLE IF NOT EXISTS parking_records (id INTEGER PRIMARY KEY, plate VARCHAR(100) NOT NULL, parking_lot VARCHAR(100) NOT NULL, entry_time VARCHAR(100) NOT NULL);')


def add_car_to_parking_lot(plate, parking_lot, entry_time):
    ticket_id = -1
    try:
        conn = sql.connect(DB_NAME)
        c = conn.cursor()
        c.execute('INSERT INTO parking_records (plate, parking_lot, entry_time) VALUES (?, ?, ?);',
                  (plate, parking_lot, entry_time))
        ticket_id = c.lastrowid
        conn.commit()
        conn.close()
    except Exception as ex:
        print("Failed to create entry on the DB {} {} {}".format(plate, parking_lot, ex))
    return ticket_id

def finish_parking_session(ticket_id: int):
    conn = sql.connect('parking_records.db')
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM parking_records WHERE id = {ticket_id}')
    rows = cur.fetchall()

    if len(rows) < 1:
        return -1, -1, -1, -1

    id, plate, parking_lot, entry_time = rows[0]
    cur.execute('DELETE FROM parking_records WHERE id=?;', (ticket_id,))
    conn.commit()
    conn.close()

    return id, plate, parking_lot, entry_time
