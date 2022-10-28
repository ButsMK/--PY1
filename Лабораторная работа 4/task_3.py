def delete(list_, index=None):
    new_list = list_.copy()
    if index is None: # TODO реализовать функцию удаления элемента из списка по индексу
        new_list.pop(-1)
    else:
        new_list.pop(index)
    return new_list

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
