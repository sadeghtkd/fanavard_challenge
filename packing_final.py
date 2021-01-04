import random


def packing(objects, boxes_count, boxes_size):
    index = len(objects)
    if bxs_count == 0:
        return 0
    if boxes_count >= index:
        return index
    box_used = 0
    while True:
        sum_col = 0
        box_used += 1
        isolated_list = objects[index - boxes_size - 1 if index - boxes_size - 1 > 0 else 0: index][::-1]
        for index_col, col in enumerate(isolated_list):
            sum_col = col + sum_col
            if sum_col == boxes_size:
                index = index - index_col - 1
                break
            if sum_col > boxes_size:
                index = index - index_col
                break
            if index_col == len(isolated_list) - 1:
                index = index - index_col - 1
                break
        if box_used == boxes_count:
            break
    return len(objects) - index


bxs_count = random.randint(1, 20)
bxs_size = random.randint(1, 15)
objs = [random.randint(1, bxs_size) for i in range(random.randint(1, 50))]
print ('boxes:{} ,box size:{} ,objects:{}'.format(bxs_count, bxs_size, objs))
objects_fitted = packing(objs, bxs_count, bxs_size)
print ('max object fitted: {}'.format(objects_fitted))
