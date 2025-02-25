s: int = 0
count = 0

while s <= 2250:
    if count % 2 == 0:
        s += count
        print(f"S: {s}, count: {count}")
    count += 1
print(f"COUNT got to: {count-1}")
