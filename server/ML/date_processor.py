import dateparser
from datetime import datetime
import json
import re

# Usaremos esta constante para la zona horaria de tu entorno de trabajo
LOCAL_TIMEZONE = 'America/Montevideo'

# --- Usaremos RE.SUB para reemplazar patrones, lo que es más robusto ---
CUSTOM_REPLACEMENTS = {
    # Relativos que fallan: forzamos a una expresión que dateparser entiende
    r'próxima semana|semana entrante|semana que viene': 'in 7 days',
    r'próximo fin de semana': 'next weekend',
    r'de aquí a una semana': 'in 7 days',
    r'mes en curso': 'this month',
    r'día 10': '10th',
    r'segunda quincena de marzo': '2nd half of March',
    
    # Horas ambiguas: forzamos a un formato de 12 horas para mayor precisión
    r'por la mañana': '8 AM',
    r'al mediodía': '12 PM',
    
    # Quincena: convertida a días. Usamos regex para coger "una quincena", "la quincena", etc.
    r'(una|la)\s+quincena': '15 days', # Ahora captura 'en una quincena' o 'en la quincena'
    r'quincena': '15 days',
}

DATEPARSER_SETTINGS = {
    'DATE_ORDER': 'DMY',
    'PREFER_DATES_FROM': 'future',
    'STRICT_PARSING': False,
    'TIMEZONE': LOCAL_TIMEZONE,
}

def preprocess_text(text: str) -> str:
    """
    Preprocess the text by replacing custom expressions using regex (re.sub).
    """
    processed_text = text
    for pattern, repl in CUSTOM_REPLACEMENTS.items():
        # CRÍTICO: Usar re.sub para aplicar el patrón de búsqueda y reemplazo
        processed_text = re.sub(pattern, repl, processed_text, flags=re.IGNORECASE)
    return processed_text

def parse_datetime(text_entity: str, current_time: datetime) -> datetime | None:
    # ... (No hay cambios en esta función más que usar 'es' y 'en' como antes)
    preprocessed = preprocess_text(text_entity)
    settings = DATEPARSER_SETTINGS.copy()
    settings['RELATIVE_BASE'] = current_time

    # Agregamos 'en' para mayor robustez en la interpretación de frases como 'next week'
    parsed_date = dateparser.parse(
        preprocessed,
        languages=['es', 'en'], # CRÍTICO: Intentar con inglés también, ya que las reglas son más robustas
        settings=settings
    )
    return parsed_date

def process_entities(entities_dict, current_time): 
    date_keys = ["start_datetime", "end_datetime"]
    processed_entities = {}
    
    for key, value in entities_dict.items():
        if key in date_keys:
            text_to_parse = ""
            
            # --- Lógica de Fusión: Asegura que siempre es un string ---
            if isinstance(value, list):
                text_to_parse = " ".join(value)
            elif isinstance(value, str):
                text_to_parse = value
            else:
                processed_entities[key] = value
                continue
            # --- Fin Lógica de Fusión ---

            parsed = parse_datetime(text_to_parse, current_time) 

            if parsed:
                processed_entities[key] = parsed.isoformat()
            else:
                # CORRECCIÓN CRÍTICA: Devolver el STRING fusionado que falló, NO el ARRAY original.
                processed_entities[key] = text_to_parse
        else:
            processed_entities[key] = value
            
    return processed_entities

def main():
    # Establecer la hora base para la prueba
    # Usaremos 2025-09-27 17:51:34 (Sábado por la tarde)
    base_time = datetime(2025, 9, 27, 17, 51, 34)
    print(f"Hora base para referencias relativas: {base_time.strftime('%Y-%m-%d %H:%M:%S')} (Sábado)")
    print("---------------------------------------")

    raw_data = [
        {'entities_dict': {'start_datetime': 'próxima semana'}},
        {'entities_dict': {'start_datetime': ['mañana', 'por la tarde']}}, # Prueba de fusión
        {'entities_dict': {'start_datetime': '25 de septiembre'}},
        {'entities_dict': {'start_datetime': 'este sábado'}},
        {'entities_dict': {'start_datetime': 'semana entrante'}},
        {'entities_dict': {'start_datetime': 'lunes'}},
        {'entities_dict': {'start_datetime': ['viernes', '3 PM']}}, # Prueba de fusión
        {'entities_dict': {'start_datetime': 'de aquí a una semana'}},
        {'entities_dict': {'start_datetime': 'mes en curso'}},
        {'entities_dict': {'start_datetime': 'segunda quincena de marzo'}},
    ]
    
    for item in raw_data:
        processed_item = item.copy()
        processed_item['entities_dict'] = process_entities(item['entities_dict'], base_time)
        
        original_value = item['entities_dict'].get('start_datetime')
        parsed_value = processed_item['entities_dict'].get('start_datetime')
        
        print(f"Original: {original_value}")
        print(f"Parsed:   {parsed_value}")
        print("---")

if __name__ == "__main__":
    main()