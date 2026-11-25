import os

line = "Great news, I found the problem: it is plugged in, switched on, and still completely ignoring both of us."

os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)
