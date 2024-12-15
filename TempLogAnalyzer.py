import re
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict

# Leer el archivo de log
log_file = 'dht_log.txt'
with open(log_file, 'r') as file:
    logs = file.readlines()

# Expresión regular para extraer fecha y temperatura
log_pattern = re.compile(r"(\\d{4}-\\d{2}-\\d{2}) \\d{2}:\\d{2}:\\d{2} - Temperature: (\\d+)\\u00b0C")

# Diccionario para almacenar temperaturas por mes
temp_data = defaultdict(list)

# Procesar cada línea del log
for log in logs:
    match = log_pattern.search(log)
    if match:
        date_str, temp = match.groups()
        date = datetime.strptime(date_str, '%Y-%m-%d')
        month_str = date.strftime('%Y-%m')  # Formato Año-Mes
        temp_data[month_str].append(int(temp))

# Calcular la temperatura promedio por mes
monthly_avg_temps = {}
for month, temps in temp_data.items():
    if temps:
        monthly_avg_temps[month] = sum(temps) / len(temps)

# Crear una lista ordenada de meses
sorted_months = sorted(monthly_avg_temps.keys())
average_temps = [monthly_avg_temps[month] for month in sorted_months]

# Graficar los datos
plt.figure(figsize=(10, 6))
plt.plot(sorted_months, average_temps, marker='o', label='Temperatura Promedio')
plt.title('Temperatura Promedio Mensual')
plt.xlabel('Mes')
plt.ylabel('Temperatura (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
