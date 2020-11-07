def merge(list1, list2):
    result = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    result += list1[i:] + list2[j:]
    
    return result

def merge_sort(my_list):

    if len(my_list) <= 1:
        return my_list
    
    mid = len(my_list) // 2
    
    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])
    return merge(left, right)
