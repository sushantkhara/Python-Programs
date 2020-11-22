def large_cont_sum(arr):
    if len(arr) == 0:
        return 0

    max_num = current_sum = arr[0]  # max=sum=arr[0]bug:TypeError:'int' object is not callable.(Do not use the keyword!)

    for n in arr[1:]:
        current_sum = max(current_sum + n, n)
        max_num = max(current_sum, max_num)
    return max_num
    pass

