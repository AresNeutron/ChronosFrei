import json
import random

# Categories from estus.csv
categories = [
    "TD_FECHA_FIJA",
    "TD_MINUTO",
    "TD_HORA",
    "TD_DIA",
    "TD_SEMANA",
    "TD_MES",
    "TD_DIA_1",
    "TD_DIA_2",
    "TD_SEM_2",
    "TD_HORA_MANANA",
    "TD_HORA_TARDE",
    "TD_HORA_NOCHE",
    "TD_HORA_MEDIODIA",
    "TD_HORA_ALMUERZO",
    "TD_HORA_CENA",
    "TD_HORA_MADRUGADA",
    "TD_HORA_ATARDECER",
    "TD_FIN_SEM",
    "TD_DIA_SEM",
    "TD_DIA_MES",
    "TD_FIN_MES",
    "TD_TRIMESTRE"
]

# Function to generate expressions
def generate_expressions():
    data = []

    # TD_FECHA_FIJA: Fixed dates
    fecha_fija = [
        "el 12 de marzo", "el 1 de enero", "el 15 de abril", "el 25 de diciembre",
        "el 5 de mayo", "el 10 de junio", "el 4 de julio", "el 14 de febrero",
        "el 31 de octubre", "el 7 de septiembre", "el 20 de noviembre", "el 8 de agosto",
        "el 2 de febrero", "el 9 de marzo", "el 16 de abril", "el 21 de mayo",
        "el 30 de junio", "el 11 de julio", "el 13 de agosto", "el 22 de septiembre",
        "el 27 de octubre", "el 3 de noviembre", "el 17 de diciembre", "el 6 de enero",
        "el 18 de febrero", "el 19 de marzo", "el 23 de abril", "el 24 de mayo",
        "el 26 de junio", "el 28 de julio", "el 29 de agosto", "el 1 de septiembre",
        "el 4 de octubre", "el 12 de noviembre", "el 15 de diciembre", "el 7 de enero",
        "el 14 de marzo", "el 25 de abril", "el 30 de mayo", "el 2 de junio",
        "el 9 de julio", "el 16 de agosto", "el 21 de septiembre", "el 5 de octubre",
        "el 11 de noviembre", "el 13 de diciembre"
    ]
    for expr in fecha_fija:
        data.append([expr, {"cat": {"TD_FECHA_FIJA": 1.0}}])

    # TD_MINUTO: Minutes
    minuto_phrases = ["en {} minutos", "dentro de {} minutos", "en {} min", "dentro de {} min"]
    for i in range(1, 46):  # 1 to 45
        for phrase in minuto_phrases:
            if i <= 10 or random.random() < 0.5:  # Limit to variety
                data.append([phrase.format(i), {"cat": {"TD_MINUTO": 1.0}}])
    # Add colloquial
    colloquial_min = [
        "en media hora", "en un cuarto de hora", "en tres cuartos de hora",
        "en una hora menos cuarto", "en 45 minutos", "en 30 min", "dentro de media hora",
        "inmediatamente", "en este momento", "ahora mismo", "ya mismo", "enseguida",
        "hoy", "este día", "ya", "en un minuto", "en dos minutos", "en tres minutos",
        "en cuatro minutos", "en cinco minutos", "en seis minutos", "en siete minutos",
        "en ocho minutos", "en nueve minutos", "en diez minutos", "en once minutos",
        "en doce minutos", "en trece minutos", "en catorce minutos", "en quince minutos"
    ]
    for expr in colloquial_min:
        data.append([expr, {"cat": {"TD_MINUTO": 1.0}}])

    # TD_HORA: Hours
    hora_phrases = ["en {} horas", "dentro de {} horas", "en {} h", "dentro de {} h", "en una hora", "en dos horas", "en tres horas", "en cuatro horas", "en cinco horas", "en seis horas", "en siete horas", "en ocho horas", "en nueve horas", "en diez horas", "en once horas", "en doce horas"]
    for i in range(1, 13):
        for phrase in hora_phrases[:4]:  # Limit
            data.append([phrase.format(i), {"cat": {"TD_HORA": 1.0}}])
    colloquial_hora = ["en una hora", "dentro de una hora", "en dos horas", "en 3 horas", "en cuatro horas", "dentro de cinco horas", "en seis horas", "en 7 horas", "dentro de 8 horas", "en 9 horas", "en 10 horas", "en 11 horas", "en 12 horas", "en media hora", "en un rato", "en un buen rato", "en poco tiempo", "pronto", "muy pronto", "en breve", "en un rato largo", "en una horita", "en dos horitas", "en tres horitas", "en cuatro horitas", "en cinco horitas", "en seis horitas", "en siete horitas", "en ocho horitas", "en nueve horitas", "en diez horitas", "en once horitas", "en doce horitas"]
    for expr in colloquial_hora:
        data.append([expr, {"cat": {"TD_HORA": 1.0}}])

    # TD_DIA: Days
    dia_phrases = ["en {} días", "dentro de {} días", "en {} d", "dentro de {} d"]
    for i in range(1, 31):
        for phrase in dia_phrases:
            if i <= 10 or random.random() < 0.3:
                data.append([phrase.format(i), {"cat": {"TD_DIA": 1.0}}])
    colloquial_dia = ["en un día", "en dos días", "en tres días", "en cuatro días", "en cinco días", "en seis días", "en siete días", "en ocho días", "en nueve días", "en diez días", "en once días", "en doce días", "en trece días", "en catorce días", "en quince días", "en dieciséis días", "en diecisiete días", "en dieciocho días", "en diecinueve días", "en veinte días", "en veintiún días", "en veintidós días", "en veintitrés días", "en veinticuatro días", "en veinticinco días", "en veintiséis días", "en veintisiete días", "en veintiocho días", "en veintinueve días", "en treinta días", "dentro de un día", "dentro de dos días", "dentro de tres días", "dentro de cuatro días", "dentro de cinco días", "dentro de seis días", "dentro de siete días", "dentro de ocho días", "dentro de nueve días", "dentro de diez días"]
    for expr in colloquial_dia:
        data.append([expr, {"cat": {"TD_DIA": 1.0}}])

    # TD_SEMANA: Weeks
    semana_phrases = ["en {} semanas", "dentro de {} semanas", "en {} sem", "dentro de {} sem"]
    for i in range(1, 11):
        for phrase in semana_phrases:
            data.append([phrase.format(i), {"cat": {"TD_SEMANA": 1.0}}])
    colloquial_semana = ["en una semana", "en dos semanas", "en tres semanas", "en cuatro semanas", "en cinco semanas", "en seis semanas", "en siete semanas", "en ocho semanas", "en nueve semanas", "en diez semanas", "dentro de una semana", "dentro de dos semanas", "dentro de tres semanas", "dentro de cuatro semanas", "dentro de cinco semanas", "dentro de seis semanas", "dentro de siete semanas", "dentro de ocho semanas", "dentro de nueve semanas", "dentro de diez semanas", "en un par de semanas", "dentro de un par de semanas", "en unas semanas", "dentro de unas semanas", "en varias semanas", "dentro de varias semanas", "en poco tiempo", "pronto", "muy pronto", "en breve", "en un rato largo", "en una semanita", "en dos semanitas", "en tres semanitas", "en cuatro semanitas", "en cinco semanitas", "en seis semanitas", "en siete semanitas", "en ocho semanitas", "en nueve semanitas", "en diez semanitas"]
    for expr in colloquial_semana:
        data.append([expr, {"cat": {"TD_SEMANA": 1.0}}])

    # TD_MES: Months
    mes_phrases = ["en {} meses", "dentro de {} meses", "en {} m", "dentro de {} m"]
    for i in range(1, 13):
        for phrase in mes_phrases:
            data.append([phrase.format(i), {"cat": {"TD_MES": 1.0}}])
    colloquial_mes = ["en un mes", "en dos meses", "en tres meses", "en cuatro meses", "en cinco meses", "en seis meses", "en siete meses", "en ocho meses", "en nueve meses", "en diez meses", "en once meses", "en doce meses", "dentro de un mes", "dentro de dos meses", "dentro de tres meses", "dentro de cuatro meses", "dentro de cinco meses", "dentro de seis meses", "dentro de siete meses", "dentro de ocho meses", "dentro de nueve meses", "dentro de diez meses", "dentro de once meses", "dentro de doce meses", "en un mesecito", "en dos mesecitos", "en tres mesecitos", "en cuatro mesecitos", "en cinco mesecitos", "en seis mesecitos", "en siete mesecitos", "en ocho mesecitos", "en nueve mesecitos", "en diez mesecitos", "en once mesecitos", "en doce mesecitos", "en poco tiempo", "pronto", "muy pronto", "en breve", "en un rato largo"]
    for expr in colloquial_mes:
        data.append([expr, {"cat": {"TD_MES": 1.0}}])

    # TD_DIA_1: Tomorrow
    dia1 = ["mañana", "al día siguiente", "el día de mañana", "mañana por la mañana", "mañana temprano", "mañana a primera hora", "mañana al alba", "mañana al amanecer", "mañana al rayar el día", "mañana al despuntar el día", "mañana al salir el sol", "mañana al clarear", "mañana al romper el alba", "mañana al romper el día", "mañana al romper el sol", "mañana al nacer el día", "mañana al nacer el sol", "mañana al apuntar el día", "mañana al apuntar el sol", "mañana al aparecer el sol", "mañana al aparecer el día", "mañana al asomar el sol", "mañana al asomar el día", "mañana al surgir el sol", "mañana al surgir el día", "mañana al emerger el sol", "mañana al emerger el día", "mañana al brotar el sol", "mañana al brotar el día", "mañana al irrumpir el sol", "mañana al irrumpir el día", "mañana al estallar el sol", "mañana al estallar el día", "mañana al explotar el sol", "mañana al explotar el día", "mañana al fulgurar el sol", "mañana al fulgurar el día", "mañana al resplandecer el sol", "mañana al resplandecer el día", "mañana al brillar el sol", "mañana al brillar el día"]
    for expr in dia1:
        data.append([expr, {"cat": {"TD_DIA_1": 1.0}}])

    # TD_DIA_2: Day after tomorrow
    dia2 = ["pasado mañana", "dentro de dos días", "el día después de mañana", "pasado mañana por la tarde", "en dos días", "pasado mañana temprano", "pasado mañana a primera hora", "pasado mañana al alba", "pasado mañana al amanecer", "pasado mañana al rayar el día", "pasado mañana al despuntar el día", "pasado mañana al salir el sol", "pasado mañana al clarear", "pasado mañana al romper el alba", "pasado mañana al romper el día", "pasado mañana al romper el sol", "pasado mañana al nacer el día", "pasado mañana al nacer el sol", "pasado mañana al apuntar el día", "pasado mañana al apuntar el sol", "pasado mañana al aparecer el sol", "pasado mañana al aparecer el día", "pasado mañana al asomar el sol", "pasado mañana al asomar el día", "pasado mañana al surgir el sol", "pasado mañana al surgir el día", "pasado mañana al emerger el sol", "pasado mañana al emerger el día", "pasado mañana al brotar el sol", "pasado mañana al brotar el día", "pasado mañana al irrumpir el sol", "pasado mañana al irrumpir el día", "pasado mañana al estallar el sol", "pasado mañana al estallar el día", "pasado mañana al explotar el sol", "pasado mañana al explotar el día", "pasado mañana al fulgurar el sol", "pasado mañana al fulgurar el día", "pasado mañana al resplandecer el sol", "pasado mañana al resplandecer el día", "pasado mañana al brillar el sol", "pasado mañana al brillar el día"]
    for expr in dia2:
        data.append([expr, {"cat": {"TD_DIA_2": 1.0}}])

    # TD_SEM_2: Two weeks
    sem2 = ["en una quincena", "en quince días", "dentro de dos semanas", "en 15 días", "una quincena", "en dos semanas", "dentro de quince días", "en una quincena de días", "en quince días justos", "dentro de una quincena", "en un par de semanas", "dentro de un par de semanas", "en dos semanitas", "dentro de dos semanitas", "en quince días hábiles", "dentro de quince días hábiles", "en una quincena aproximada", "en quince días aproximados", "dentro de una quincena aproximada", "en quince días aproximados", "en dos semanas justas", "dentro de dos semanas justas", "en una quincena redonda", "en quince días redondos", "dentro de una quincena redonda", "en quince días redondos", "en dos semanas completas", "dentro de dos semanas completas", "en una quincena completa", "en quince días completos", "dentro de una quincena completa", "en quince días completos", "en dos semanas enteras", "dentro de dos semanas enteras", "en una quincena entera", "en quince días enteros", "dentro de una quincena entera", "en quince días enteros", "en dos semanas cabales", "dentro de dos semanas cabales", "en una quincena cabal", "en quince días cabales", "dentro de una quincena cabal", "en quince días cabales"]
    for expr in sem2:
        data.append([expr, {"cat": {"TD_SEM_2": 1.0}}])

    # TD_HORA_MANANA: Morning
    manana = ["por la mañana", "a primera hora", "temprano por la mañana", "a las 8 de la mañana", "muy temprano", "al amanecer", "al alba", "al rayar el día", "al despuntar el día", "al salir el sol", "al clarear", "al romper el alba", "al romper el día", "al romper el sol", "al nacer el día", "al nacer el sol", "al apuntar el día", "al apuntar el sol", "al aparecer el sol", "al aparecer el día", "al asomar el sol", "al asomar el día", "al surgir el sol", "al surgir el día", "al emerger el sol", "al emerger el día", "al brotar el sol", "al brotar el día", "al irrumpir el sol", "al irrumpir el día", "al estallar el sol", "al estallar el día", "al explotar el sol", "al explotar el día", "al fulgurar el sol", "al fulgurar el día", "al resplandecer el sol", "al resplandecer el día", "al brillar el sol", "al brillar el día", "a las 7 de la mañana", "a las 6 de la mañana", "a las 5 de la mañana", "a las 9 de la mañana", "a las 10 de la mañana"]
    for expr in manana:
        data.append([expr, {"cat": {"TD_HORA_MANANA": 1.0}}])

    # TD_HORA_TARDE: Afternoon
    tarde = ["por la tarde", "a las 3 de la tarde", "tarde en la tarde", "por la tarde tarde", "a las 15 horas", "a las 16 horas", "a las 17 horas", "a las 18 horas", "a las 14 horas", "a las 13 horas", "a las 12 horas", "a las 19 horas", "a las 20 horas", "a las 21 horas", "a las 22 horas", "a las 23 horas", "a las 24 horas", "a las 1 de la tarde", "a las 2 de la tarde", "a las 4 de la tarde", "a las 5 de la tarde", "a las 6 de la tarde", "a las 7 de la tarde", "a las 8 de la tarde", "a las 9 de la tarde", "a las 10 de la tarde", "a las 11 de la tarde", "a las 12 de la tarde", "a las 13 de la tarde", "a las 14 de la tarde", "a las 15 de la tarde", "a las 16 de la tarde", "a las 17 de la tarde", "a las 18 de la tarde", "a las 19 de la tarde", "a las 20 de la tarde", "a las 21 de la tarde", "a las 22 de la tarde", "a las 23 de la tarde", "a las 24 de la tarde", "a las 1 de la tarde", "a las 2 de la tarde", "a las 4 de la tarde", "a las 5 de la tarde", "a las 6 de la tarde"]
    for expr in tarde:
        data.append([expr, {"cat": {"TD_HORA_TARDE": 1.0}}])

    # TD_HORA_NOCHE: Night
    noche = ["por la noche", "a última hora", "a la hora de dormir", "tarde por la noche", "a las 9 de la noche", "a las 10 de la noche", "a las 11 de la noche", "a las 12 de la noche", "a las 1 de la noche", "a las 2 de la noche", "a las 3 de la noche", "a las 4 de la noche", "a las 5 de la noche", "a las 6 de la noche", "a las 7 de la noche", "a las 8 de la noche", "a las 9 de la noche", "a las 10 de la noche", "a las 11 de la noche", "a las 12 de la noche", "a las 1 de la noche", "a las 2 de la noche", "a las 3 de la noche", "a las 4 de la noche", "a las 5 de la noche", "a las 6 de la noche", "a las 7 de la noche", "a las 8 de la noche", "a las 9 de la noche", "a las 10 de la noche", "a las 11 de la noche", "a las 12 de la noche", "a las 1 de la noche", "a las 2 de la noche", "a las 3 de la noche", "a las 4 de la noche", "a las 5 de la noche", "a las 6 de la noche", "a las 7 de la noche", "a las 8 de la noche", "a las 9 de la noche", "a las 10 de la noche", "a las 11 de la noche", "a las 12 de la noche"]
    for expr in noche:
        data.append([expr, {"cat": {"TD_HORA_NOCHE": 1.0}}])

    # TD_HORA_MEDIODIA: Noon
    mediodia = ["al mediodía", "a mediodía", "al medio día", "a las 12 del mediodía", "a las 12 en punto", "a las doce del mediodía", "a las doce en punto", "al mediodía exacto", "a mediodía exacto", "al medio día exacto", "a las 12 del mediodía exacto", "a las 12 en punto exacto", "a las doce del mediodía exacto", "a las doce en punto exacto", "al mediodía justo", "a mediodía justo", "al medio día justo", "a las 12 del mediodía justo", "a las 12 en punto justo", "a las doce del mediodía justo", "a las doce en punto justo", "al mediodía cabal", "a mediodía cabal", "al medio día cabal", "a las 12 del mediodía cabal", "a las 12 en punto cabal", "a las doce del mediodía cabal", "a las doce en punto cabal", "al mediodía completo", "a mediodía completo", "al medio día completo", "a las 12 del mediodía completo", "a las 12 en punto completo", "a las doce del mediodía completo", "a las doce en punto completo", "al mediodía entero", "a mediodía entero", "al medio día entero", "a las 12 del mediodía entero", "a las 12 en punto entero", "a las doce del mediodía entero", "a las doce en punto entero"]
    for expr in mediodia:
        data.append([expr, {"cat": {"TD_HORA_MEDIODIA": 1.0}}])

    # TD_HORA_ALMUERZO: Lunch time
    almuerzo = ["hora del almuerzo", "a la hora de comer", "hora de almorzar", "a las 13 horas", "a las 1 de la tarde", "a las 12:30", "a las 13:00", "a las 13:30", "a las 14:00", "hora de comer", "hora de almorzar", "a la hora del almuerzo", "a la hora de almorzar", "a la hora de comer", "a las 13 horas en punto", "a las 1 de la tarde en punto", "a las 12:30 en punto", "a las 13:00 en punto", "a las 13:30 en punto", "a las 14:00 en punto", "hora del almuerzo exacta", "a la hora de comer exacta", "hora de almorzar exacta", "a las 13 horas exactas", "a las 1 de la tarde exactas", "a las 12:30 exactas", "a las 13:00 exactas", "a las 13:30 exactas", "a las 14:00 exactas", "hora de comer exacta", "hora de almorzar exacta", "a la hora del almuerzo exacta", "a la hora de almorzar exacta", "a la hora de comer exacta", "a las 13 horas en punto exacto", "a las 1 de la tarde en punto exacto", "a las 12:30 en punto exacto", "a las 13:00 en punto exacto", "a las 13:30 en punto exacto", "a las 14:00 en punto exacto"]
    for expr in almuerzo:
        data.append([expr, {"cat": {"TD_HORA_ALMUERZO": 1.0}}])

    # TD_HORA_CENA: Dinner time
    cena = ["hora de la cena", "a la hora de cenar", "hora de cenar", "a las 20 horas", "a las 8 de la noche", "a las 19:00", "a las 20:00", "a las 20:30", "a las 21:00", "hora de cenar", "hora de la cena", "a la hora de cenar", "a la hora de la cena", "a las 20 horas en punto", "a las 8 de la noche en punto", "a las 19:00 en punto", "a las 20:00 en punto", "a las 20:30 en punto", "a las 21:00 en punto", "hora de cenar exacta", "hora de la cena exacta", "a la hora de cenar exacta", "a la hora de la cena exacta", "a las 20 horas exactas", "a las 8 de la noche exactas", "a las 19:00 exactas", "a las 20:00 exactas", "a las 20:30 exactas", "a las 21:00 exactas", "hora de cenar exacta", "hora de la cena exacta", "a la hora de cenar exacta", "a la hora de la cena exacta", "a las 20 horas en punto exacto", "a las 8 de la noche en punto exacto", "a las 19:00 en punto exacto", "a las 20:00 en punto exacto", "a las 20:30 en punto exacto", "a las 21:00 en punto exacto"]
    for expr in cena:
        data.append([expr, {"cat": {"TD_HORA_CENA": 1.0}}])

    # TD_HORA_MADRUGADA: Dawn
    madrugada = ["a la madrugada", "muy temprano", "a las 5 de la madrugada", "al amanecer", "al alba", "al rayar el día", "al despuntar el día", "al salir el sol", "al clarear", "al romper el alba", "al romper el día", "al romper el sol", "al nacer el día", "al nacer el sol", "al apuntar el día", "al apuntar el sol", "al aparecer el sol", "al aparecer el día", "al asomar el sol", "al asomar el día", "al surgir el sol", "al surgir el día", "al emerger el sol", "al emerger el día", "al brotar el sol", "al brotar el día", "al irrumpir el sol", "al irrumpir el día", "al estallar el sol", "al estallar el día", "al explotar el sol", "al explotar el día", "al fulgurar el sol", "al fulgurar el día", "al resplandecer el sol", "al resplandecer el día", "al brillar el sol", "al brillar el día", "a las 4 de la madrugada", "a las 3 de la madrugada", "a las 2 de la madrugada", "a las 1 de la madrugada", "a las 6 de la madrugada", "a las 7 de la madrugada"]
    for expr in madrugada:
        data.append([expr, {"cat": {"TD_HORA_MADRUGADA": 1.0}}])

    # TD_HORA_ATARDECER: Sunset
    atardecer = ["al atardecer", "a las 7 de la tarde", "cuando se pone el sol", "a las 19 horas", "a las 18:00", "a las 19:00", "a las 19:30", "a las 20:00", "al ponerse el sol", "al caer el sol", "al declinar el sol", "al ocultarse el sol", "al desaparecer el sol", "al irse el sol", "al marcharse el sol", "al retirarse el sol", "al alejarse el sol", "al despedirse el sol", "al decir adiós el sol", "al abandonar el sol", "al dejar el sol", "al partir el sol", "al irse el sol", "al marcharse el sol", "al retirarse el sol", "al alejarse el sol", "al despedirse el sol", "al decir adiós el sol", "al abandonar el sol", "al dejar el sol", "al partir el sol", "al irse el sol", "al marcharse el sol", "al retirarse el sol", "al alejarse el sol", "al despedirse el sol", "al decir adiós el sol", "al abandonar el sol", "al dejar el sol", "al partir el sol", "al irse el sol", "al marcharse el sol", "al retirarse el sol", "al alejarse el sol", "al despedirse el sol", "al decir adiós el sol", "al abandonar el sol", "al dejar el sol", "al partir el sol"]
    for expr in atardecer:
        data.append([expr, {"cat": {"TD_HORA_ATARDECER": 1.0}}])

    # TD_FIN_SEM: Weekend
    fin_sem = ["el fin de semana", "este fin de semana", "el próximo fin de semana", "fin de semana", "este finde", "el finde", "el próximo finde", "finde", "este fin de semana largo", "el fin de semana largo", "el próximo fin de semana largo", "fin de semana largo", "este finde largo", "el finde largo", "el próximo finde largo", "finde largo", "este fin de semana corto", "el fin de semana corto", "el próximo fin de semana corto", "fin de semana corto", "este finde corto", "el finde corto", "el próximo finde corto", "finde corto", "este fin de semana completo", "el fin de semana completo", "el próximo fin de semana completo", "fin de semana completo", "este finde completo", "el finde completo", "el próximo finde completo", "finde completo", "este fin de semana entero", "el fin de semana entero", "el próximo fin de semana entero", "fin de semana entero", "este finde entero", "el finde entero", "el próximo finde entero", "finde entero", "este fin de semana cabal", "el fin de semana cabal", "el próximo fin de semana cabal", "fin de semana cabal", "este finde cabal", "el finde cabal", "el próximo finde cabal", "finde cabal"]
    for expr in fin_sem:
        data.append([expr, {"cat": {"TD_FIN_SEM": 1.0}}])

    # TD_DIA_SEM: Days of week
    dias_sem = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    dia_sem = []
    for dia in dias_sem:
        dia_sem.append(f"este {dia}")
        dia_sem.append(dia)
        dia_sem.append(f"el {dia}")
        dia_sem.append(f"este próximo {dia}")
        dia_sem.append(f"próximo {dia}")
        dia_sem.append(f"el próximo {dia}")
        dia_sem.append(f"este {dia} que viene")
        dia_sem.append(f"{dia} que viene")
        dia_sem.append(f"el {dia} que viene")
        dia_sem.append(f"este {dia} entrante")
        dia_sem.append(f"{dia} entrante")
        dia_sem.append(f"el {dia} entrante")
        dia_sem.append(f"este {dia} próximo")
        dia_sem.append(f"{dia} próximo")
        dia_sem.append(f"el {dia} próximo")
        dia_sem.append(f"este {dia} siguiente")
        dia_sem.append(f"{dia} siguiente")
        dia_sem.append(f"el {dia} siguiente")
        dia_sem.append(f"este {dia} venidero")
        dia_sem.append(f"{dia} venidero")
        dia_sem.append(f"el {dia} venidero")
        dia_sem.append(f"este {dia} futuro")
        dia_sem.append(f"{dia} futuro")
        dia_sem.append(f"el {dia} futuro")
        dia_sem.append(f"este {dia} por venir")
        dia_sem.append(f"{dia} por venir")
        dia_sem.append(f"el {dia} por venir")
        dia_sem.append(f"este {dia} inminente")
        dia_sem.append(f"{dia} inminente")
        dia_sem.append(f"el {dia} inminente")
        dia_sem.append(f"este {dia} cercano")
        dia_sem.append(f"{dia} cercano")
        dia_sem.append(f"el {dia} cercano")
        dia_sem.append(f"este {dia} próximo a venir")
        dia_sem.append(f"{dia} próximo a venir")
        dia_sem.append(f"el {dia} próximo a venir")
    for expr in dia_sem:
        data.append([expr, {"cat": {"TD_DIA_SEM": 1.0}}])

    # TD_DIA_MES: Day of month
    dia_mes = []
    for i in range(1, 32):
        dia_mes.append(f"el {i} del mes")
        dia_mes.append(f"día {i} de este mes")
        dia_mes.append(f"el día {i} del mes")
        dia_mes.append(f"día {i} de este mes actual")
        dia_mes.append(f"el {i} de este mes")
        dia_mes.append(f"día {i} del mes actual")
        dia_mes.append(f"el día {i} de este mes")
        dia_mes.append(f"día {i} de este mes corriente")
        dia_mes.append(f"el {i} de este mes corriente")
        dia_mes.append(f"día {i} del mes corriente")
        dia_mes.append(f"el día {i} de este mes corriente")
        dia_mes.append(f"día {i} de este mes presente")
        dia_mes.append(f"el {i} de este mes presente")
        dia_mes.append(f"día {i} del mes presente")
        dia_mes.append(f"el día {i} de este mes presente")
        dia_mes.append(f"día {i} de este mes en curso")
        dia_mes.append(f"el {i} de este mes en curso")
        dia_mes.append(f"día {i} del mes en curso")
        dia_mes.append(f"el día {i} de este mes en curso")
        dia_mes.append(f"día {i} de este mes actual")
        dia_mes.append(f"el {i} de este mes actual")
        dia_mes.append(f"día {i} del mes actual")
        dia_mes.append(f"el día {i} de este mes actual")
        dia_mes.append(f"día {i} de este mes corriente")
        dia_mes.append(f"el {i} de este mes corriente")
        dia_mes.append(f"día {i} del mes corriente")
        dia_mes.append(f"el día {i} de este mes corriente")
        dia_mes.append(f"día {i} de este mes presente")
        dia_mes.append(f"el {i} de este mes presente")
        dia_mes.append(f"día {i} del mes presente")
        dia_mes.append(f"el día {i} de este mes presente")
        dia_mes.append(f"día {i} de este mes en curso")
        dia_mes.append(f"el {i} de este mes en curso")
        dia_mes.append(f"día {i} del mes en curso")
        dia_mes.append(f"el día {i} de este mes en curso")
    for expr in dia_mes:
        data.append([expr, {"cat": {"TD_DIA_MES": 1.0}}])

    # TD_FIN_MES: End of month
    fin_mes = ["a fin de mes", "el último día del mes", "fin de mes", "último día del mes", "a finales de mes", "el final del mes", "finales de mes", "el final del mes actual", "a finales del mes", "el último día del mes actual", "fin del mes", "último día del mes actual", "a fin del mes", "el último día del mes corriente", "fin del mes corriente", "último día del mes corriente", "a fin del mes corriente", "el último día del mes presente", "fin del mes presente", "último día del mes presente", "a fin del mes presente", "el último día del mes en curso", "fin del mes en curso", "último día del mes en curso", "a fin del mes en curso", "el último día del mes actual", "fin del mes actual", "último día del mes actual", "a fin del mes actual", "el último día del mes corriente", "fin del mes corriente", "último día del mes corriente", "a fin del mes corriente", "el último día del mes presente", "fin del mes presente", "último día del mes presente", "a fin del mes presente", "el último día del mes en curso", "fin del mes en curso", "último día del mes en curso", "a fin del mes en curso"]
    for expr in fin_mes:
        data.append([expr, {"cat": {"TD_FIN_MES": 1.0}}])

    # TD_TRIMESTRE: Quarter
    trimestre = ["en un trimestre", "dentro de 3 meses", "en dos trimestres", "dentro de 6 meses", "un trimestre", "dentro de un trimestre", "en un trimestre de tiempo", "dentro de un trimestre de tiempo", "en dos trimestres de tiempo", "dentro de dos trimestres de tiempo", "en tres trimestres", "dentro de 9 meses", "en cuatro trimestres", "dentro de 12 meses", "en un trimestre completo", "dentro de un trimestre completo", "en dos trimestres completos", "dentro de dos trimestres completos", "en tres trimestres completos", "dentro de tres trimestres completos", "en cuatro trimestres completos", "dentro de cuatro trimestres completos", "en un trimestre entero", "dentro de un trimestre entero", "en dos trimestres enteros", "dentro de dos trimestres enteros", "en tres trimestres enteros", "dentro de tres trimestres enteros", "en cuatro trimestres enteros", "dentro de cuatro trimestres enteros", "en un trimestre cabal", "dentro de un trimestre cabal", "en dos trimestres cabales", "dentro de dos trimestres cabales", "en tres trimestres cabales", "dentro de tres trimestres cabales", "en cuatro trimestres cabales", "dentro de cuatro trimestres cabales"]
    for expr in trimestre:
        data.append([expr, {"cat": {"TD_TRIMESTRE": 1.0}}])

    # Shuffle to randomize
    random.shuffle(data)

    return data

if __name__ == "__main__":
    data = generate_expressions()
    with open("raw_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)