def merge_sort(num_list):
    if len(num_list) <= 1:
        return num_list
    middle_point = int(len(num_list)/2)
    first_half = num_list[:middle_point]
    second_half = num_list[middle_point:]
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)
    return merge(first_half, second_half)

def merge(first_half, second_half):
    first_index = second_index = 0
    sorted_list = []
    while first_index < len(first_half) and second_index < len(second_half):
        if first_half[first_index] < second_half[second_index]:
            sorted_list.append(first_half[first_index])
            first_index += 1
        else:
            sorted_list.append(second_half[second_index])
            second_index += 1
    sorted_list.extend(first_half[first_index:])
    sorted_list.extend(second_half[second_index:])
    return sorted_list

num_list = [7,5,6,8,2,3,6,1,9,15,0]
print(merge_sort(num_list))
    