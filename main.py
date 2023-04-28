from fastapi import FastAPI, HTTPException
import sqlite3 as sql
import uvicorn
from datetime import datetime

app = FastAPI()

conn = sql.connect('parking_records.db')
cur = conn.cursor()
cur.execute(f'CREATE TABLE IF NOT EXISTS parking_records (id INTEGER PRIMARY KEY, plate VARCHAR(100) NOT NULL, parking_lot VARCHAR(100) NOT NULL, entry_time VARCHAR(100) NOT NULL);')



def calculate_charge(entry_time, exit_time):
    diff = exit_time - entry_time
    hours = diff.total_seconds() / 3600
    quarters = int(round(hours * 4))
    charge = quarters * 2.5
    return charge


@app.post("/entry/{plate}/{parking_lot}")
async def entry(plate: str, parking_lot: str):
    entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sql.connect('parking_records.db')
    c = conn.cursor()
    c.execute('INSERT INTO parking_records (plate, parking_lot, entry_time) VALUES (?, ?, ?);',
              (plate, parking_lot, entry_time))

    ticket_id = c.lastrowid

    conn.commit()
    conn.close()
    return {"ticket_id": ticket_id}


@app.post("/exit/{ticket_id}")
async def exit(ticket_id: int):

    conn = sql.connect('parking_records.db')
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM parking_records WHERE id = {ticket_id}')
    rows = cur.fetchall()

    if len(rows) < 1:
        raise HTTPException(status_code=404, detail="Ticket not found")

    id, plate, parking_lot, entry_time = rows[0]
    entry_time = datetime.strptime(entry_time, "%Y-%m-%d %H:%M:%S")
    exit_time = datetime.now()
    charge = calculate_charge(entry_time, exit_time)
    total_parked_time = str(exit_time - entry_time)
    cur.execute('DELETE FROM parking_records WHERE id=?;', (ticket_id,))
    conn.commit()
    conn.close()

    return {"license_plate": plate,
            "total_parked_time": total_parked_time,
            "parking_lot_id": parking_lot,
            "charge": f'{charge}$'}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
