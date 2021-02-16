my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

def sum_list(list):
    total = 0
    for element in list:
        try:
            total += element
        except:
            print(f'"{element}" is not a number')
    return total

print(sum_list(my_list))