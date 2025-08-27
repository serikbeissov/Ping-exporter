import csv

def format_entry(ip, index, label):
    return (
        f'{" " * 22}"{ip}": {{\n'
        f'{" " * 24}"index": {index},\n'
        f'{" " * 24}"text": "{label}"\n'
        f'{" " * 22}}},'
    )

lines = []

# Читаем CSV-файл
with open("input.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    idx = 1
    for row in reader:
        if len(row) != 2:
            continue  # skip empty or malformed lines
        ip, label = row
        lines.append(format_entry(ip, idx, label))
        idx += 1

# Собираем JSON
output = "{\n" + "\n".join(lines).rstrip(",") + "\n}"

# Сохраняем в файл
with open("output.json", "w", encoding="utf-8") as f:
    f.write(output)