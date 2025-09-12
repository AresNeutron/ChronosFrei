from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend_db import CalendarDB
from models.models import Event, EventUpdate, AIChatRequest

# Pydantic model para validar los datos de los eventos

app = FastAPI()
db = CalendarDB()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/events/")
def create_event(event: Event):
    """
    Crea un nuevo evento en el calendario.
    """
    event_id = db.add_event(
        event.title,
        event.start_datetime,
        event.end_datetime,
        event.description,
        event.location,
        event.is_recurring,
        event.recurrence_rule
    )
    return {"message": "Event created successfully", "id": event_id}

@app.get("/events/")
def get_all_events():
    """
    Recupera todos los eventos del calendario.
    """
    events = db.get_events()
    return {"events": events}

@app.put("/events/{event_id}")
def update_event(event_id: int, event: EventUpdate):
    """
    Actualiza la información de un evento existente.
    """
    is_updated = db.update_event(
        event_id,
        event.title,
        event.start_datetime,
        event.end_datetime,
        event.description,
        event.location
    )
    if not is_updated:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": f"Event {event_id} updated successfully"}

@app.delete("/events/{event_id}")
def delete_event(event_id: int):
    """
    Elimina un evento por su ID.
    """
    is_deleted = db.delete_event(event_id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": f"Event {event_id} deleted successfully"}


@app.post("/ai/chat")
def handle_ai_chat(request: AIChatRequest):
    """
    Recibe un mensaje de texto de la UI y lo procesa.
    Aquí es donde vivirá la magia del NLP.
    """
    print(f"Received message from UI: '{request.message}'")
    # Este es un mensaje de prueba. En el futuro, aquí se procesará el texto.
    return {"message": f"Message received successfully. The AI will process: '{request.message}'"}