// Interface for the data needed to create a new event
export interface EventCreate {
    title: string;
    start_datetime: string;
    end_datetime: string;
    description?: string; // Optional field
    location?: string; // Optional field
    is_recurring?: boolean; // Optional field with a default value
    recurrence_rule?: string; // Optional field
}

// Interface for the data needed to update an existing event
// All fields are optional because you only need to send the ones you want to update
export interface EventUpdate {
    title?: string; // Optional
    start_datetime?: string; // Optional
    end_datetime?: string; // Optional
    description?: string; // Optional
    location?: string; // Optional
}

// Interface for the response from the API after creating or deleting an event
export interface APIResponse {
    message: string;
    id?: number; // Optional, as it might not be present in all responses
}

// Interface for the response from the API when fetching all events
export interface GetEventsResponse {
    events: any[]; // The events data returned from the database
}