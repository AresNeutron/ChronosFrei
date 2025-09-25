from datetime import datetime
import dateparser
# Para esta etapa, solo necesitamos dateparser, pero ya instalamos dateutil si hace falta.

# Configuración crucial para el parser en español
DATEPARSER_SETTINGS = {
    'DATE_ORDER': 'DMY',       # Formato estándar Día/Mes/Año
    'PREFER_DATES_FROM': 'future', # Ayuda a que "lunes" se refiera al próximo lunes
    'STRICT_PARSING': False    # Permite flexibilidad en el texto de entrada
}

def parse_absolute_entity(text_entity: str) -> datetime | None:
    if not text_entity:
        return None

    dt_object = dateparser.parse(
        text_entity,
        languages=['es'], # esta línea falla
        settings=DATEPARSER_SETTINGS
    )
    
    return dt_object


# Fecha Absoluta
date_text_1 = "5 de enero"
print(f"'{date_text_1}' -> {parse_absolute_entity(date_text_1)}")

# Día de la semana (manejado como absoluta)
date_text_2 = "lunes"
print(f"'{date_text_2}' -> {parse_absolute_entity(date_text_2)}")

# Hora Absoluta (Formato 12hrs)
time_text_3 = "7 PM"
print(f"'{time_text_3}' -> {parse_absolute_entity(time_text_3)}")

# Hora Absoluta (Formato 24hrs y minutos)
time_text_4 = "25 de septiembre 14:30"
print(f"'{time_text_4}' -> {parse_absolute_entity(time_text_4)}")

# Fecha + Hora (dateparser puede manejarlas juntas también)
mixed_text_5 = "20 de noviembre a las 10:30"
print(f"'{mixed_text_5}' -> {parse_absolute_entity(mixed_text_5)}")
