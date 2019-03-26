number_list = [45,7,8,1,9,78]

def Selection_sort(number_list):
    n = len(number_list)

    for x in range(n-1):
        temp_index = x
        for y in range(x,n):
            if number_list[temp_index] > number_list[y]:
                temp_index = y

        number_list[temp_index],number_list[x] = number_list[x],number_list[temp_index]

    return number_list
print(Selection_sort(number_list))