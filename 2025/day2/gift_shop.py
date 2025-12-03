def _is_invalid_id_part_1(id: str) -> bool:
    if len(id) % 2 != 0:
        return False
    return id[:len(id)//2] == id[len(id)//2:]

def _is_invalid_id_part_2(id: str) -> bool:
    for n in range(3, len(id)+1):
        if len(id) % n == 0:
            l = len(id) // n
            substr = id[:l]
            invalid = True
            for i in range(1, n):
                if substr != id[i*l:(i*l)+l]:
                    invalid = False
                    break
                pass
            if invalid:
                return True
    return False


invalid_id_sum_part_1 = 0
invalid_id_sum_part_2 = 0

with open("gift_shop.txt", "r") as f:
    id_ranges: list[list[int]] = [[int(r) for r in raw_range] for raw_range in [r.split("-") for r in f.read().split(",")]]

    for cur_range in id_ranges:
        for id in range(cur_range[0], cur_range[1]+1):
            if _is_invalid_id_part_1(str(id)):
                invalid_id_sum_part_1 += id
                invalid_id_sum_part_2 += id
            elif _is_invalid_id_part_2(str(id)):
                invalid_id_sum_part_2 += id


print(f"Part 1 Result: {invalid_id_sum_part_1}")
print(f"Part 2 Result: {invalid_id_sum_part_2}")