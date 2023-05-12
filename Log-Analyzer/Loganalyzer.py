import re

def log_analyzer(log_file):
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?([a-zA-Z]{3,4}).*?([/\w-]*)\s(\d{3}).*?"(.*?)"')
    # Patrón de expresión regular para buscar patrones de direcciones IP, métodos HTTP, URI, códigos de estado y cadenas de agente de usuario en los registros de log
    logs = []
    with open(log_file, 'r') as f:
        for line in f:
            match = re.search(pattern, line)
            if match:
                logs.append({'ip': match.group(1), 'method': match.group(2), 'uri': match.group(3), 'status': match.group(4), 'user_agent': match.group(5)})
    # Analiza los registros de log y guarda la información relevante en una lista de diccionarios
    return logs

# Ejemplo de uso
log_file = 'access.log'
logs = log_analyzer(log_file)
for log in logs:
    print(log)
