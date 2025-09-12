from backend_db import CalendarDB

if __name__ == "__main__":
    db = CalendarDB()
    
    print("--- Operación CREATE ---")
    event_id = db.add_event("Cita con el doctor", "2025-09-15 10:00:00", "2025-09-15 11:00:00", "Chequeo anual")
    print(f"Evento 'Cita con el doctor' agregado con ID: {event_id}")

    print("\n--- Operación READ (todos los eventos) ---")
    events = db.get_events()
    for event in events:
        print(event)

    print("\n--- Operación UPDATE ---")
    is_updated = db.update_event(event_id, title="Cita con el cardiólogo")
    if is_updated:
        print(f"Evento con ID {event_id} actualizado.")
    
    print("\n--- Operación READ (evento actualizado) ---")
    event = db.get_events(start_date="2025-09-15", end_date="2025-09-15")
    for e in event:
        print(e)
    
    print("\n--- Operación DELETE ---")
    is_deleted = db.delete_event(event_id)
    if is_deleted:
        print(f"Evento con ID {event_id} eliminado.")

    db.close()