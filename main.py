import os

line = "Great news, I found the problem: it is plugged in, switched on, and still completely ignoring both of us."

os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)

# Verify the write landed intact.
with open("/output/entry.txt", encoding="utf-8") as f:
    assert f.read() == line

# Second opinion on the file, this time in raw bytes.
with open("/output/entry.txt", "rb") as f:
    raw = f.read()
assert len(raw) == 105 and raw == line.encode("utf-8")
