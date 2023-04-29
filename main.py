from fastapi import FastAPI, HTTPException
import uvicorn
from datetime import datetime

from parking_db_manager import create_db, add_car_to_parking_lot, finish_parking_session

app = FastAPI()

create_db()
def calculate_charge(entry_time, exit_time):
    diff = exit_time - entry_time
    hours = diff.total_seconds() / 3600
    quarters = int(round(hours * 4))
    charge = quarters * 2.5
    return charge


@app.post("/entry/{plate}/{parking_lot}")
async def entry(plate: str, parking_lot: str):
    print("plate {} for parking lot {}".format(plate, parking_lot))
    entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ticket_id = add_car_to_parking_lot(plate, parking_lot, entry_time)
    if ticket_id > 0:
        response_json = {"ticket_id": ticket_id}
        response_status = 200
    else:
        print("Failed")
        response_json = {"status_message": "Failed to insert cat {}".format(plate)}
        response_status = 500
    return response_json, response_status


@app.post("/exit/{ticket_id}")
async def exit(ticket_id: int):
    id, plate, parking_lot, entry_time = finish_parking_session(ticket_id)
    if all([x != -1 for x in [ id, plate, parking_lot, entry_time]]):
        entry_time = datetime.strptime(entry_time, "%Y-%m-%d %H:%M:%S")
        exit_time = datetime.now()
        charge = calculate_charge(entry_time, exit_time)
        total_parked_time = str(exit_time - entry_time)
        response_json = {"license_plate": plate,
                "total_parked_time": total_parked_time,
                "parking_lot_id": parking_lot,
                "charge": f'{charge}$'}
        response_status = 200
    else:
        raise HTTPException(501, "Ticket {} not found".format(ticket_id))
    return response_json, response_status

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
