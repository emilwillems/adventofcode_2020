
seats = [s.rstrip() for s in open("day5/puzzle_input").readlines()]

def get_seat_id(code: str):
    row = code[:7]
    seat = code[7:]

    int_row = int(row.replace('F', '0').replace('B', '1'), 2)
    int_seat = int(seat.replace('L', '0').replace('R', '1'), 2)

    return (int_row * 8) + int_seat

seat_ids = sorted([get_seat_id(s) for s in seats])
print("part 1:", max(seat_ids))

for idx, sid in enumerate(seat_ids):
    if seat_ids[idx+1] - sid == 2:
        print("part 2:", sid+1)
        break