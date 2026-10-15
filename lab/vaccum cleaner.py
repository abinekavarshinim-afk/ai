# Two-room vacuum cleaner problem
# 0 = clean, 1 = dirty

rooms = {"A": 1, "B": 1}
position = "A"

while any(rooms.values()):
    if rooms[position] == 1:
        rooms[position] = 0
        print(f"Cleaned room {position}")
    else:
        position = "B" if position == "A" else "A"
        print(f"Moved to room {position}")

print("Both rooms are clean!")
