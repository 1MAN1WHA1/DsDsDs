
lst = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

def binary_search(lst, search_item):
    low = 0
    high = len(lst) - 1
    search_res = False
    middle = -1
    
    while low <= high and not search_res:
        middle = (low + high) // 2
        guess = lst[middle]
        if guess == search_item:
            search_res = True
        if guess > search_item:
            high = middle - 1
        else:
            low = middle + 1
    
    if search_res:
        return search_res, middle
    else:
        return search_res, -1

value = 1
result, index = binary_search(lst, value)

if result:
    print(f"Разделение найдено {index}")
else:
    print("Разделение не найдено")