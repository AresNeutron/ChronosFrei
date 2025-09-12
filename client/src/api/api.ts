import type { EventCreate, EventUpdate } from "../types";

const API_BASE_URL = 'http://127.0.0.1:8000';

// Función para crear un nuevo evento (C de CRUD)
export const createEvent = async (eventData: EventCreate) => {
    try {
        const response = await fetch(`${API_BASE_URL}/events/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(eventData),
        });
        if (!response.ok) {
            throw new Error('Failed to create event');
        }
        return await response.json();
    } catch (error) {
        console.error("Error creating event:", error);
        throw error;
    }
};

// Función para obtener todos los eventos (R de CRUD)
export const getEvents = async () => {
    try {
        const response = await fetch(`${API_BASE_URL}/events/`);
        if (!response.ok) {
            throw new Error('Failed to fetch events');
        }
        const data = await response.json();
        return data.events;
    } catch (error) {
        console.error("Error fetching events:", error);
        throw error;
    }
};

// Función para actualizar un evento (U de CRUD)
export const updateEvent = async (eventId: number, updatedData: EventUpdate) => {
    try {
        const response = await fetch(`${API_BASE_URL}/events/${eventId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updatedData),
        });
        if (!response.ok) {
            throw new Error('Failed to update event');
        }
        return await response.json();
    } catch (error) {
        console.error("Error updating event:", error);
        throw error;
    }
};

// Función para eliminar un evento (D de CRUD)
export const deleteEvent = async (eventId: number) => {
    try {
        const response = await fetch(`${API_BASE_URL}/events/${eventId}`, {
            method: 'DELETE',
        });
        if (!response.ok) {
            throw new Error('Failed to delete event');
        }
        return await response.json();
    } catch (error) {
        console.error("Error deleting event:", error);
        throw error;
    }
};

// Función para enviar el texto transcrito a la IA del backend
export const sendChatToAI = async (text: string) => {
    try {
        const response = await fetch(`${API_BASE_URL}/ai/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: text }), // Enviamos el texto en un objeto JSON
        });
        if (!response.ok) {
            throw new Error('Failed to send message to AI');
        }
        return await response.json();
    } catch (error) {
        console.error("Error sending message to AI:", error);
        throw error;
    }
};