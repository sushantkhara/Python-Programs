# Python program to remove characters from first string which  are present in the second string
NO_OF_CHARS = 256


# Utility function to convert from string to list
def tolist(string):
    temp = []
    for x in string:
        temp.append(x)
    return temp


# Utility function to convert from list to string
def tostring(List):
    return ''.join(List)


# Returns an array of size 256 containing count of characters
# in the passed char array
def getchar_count_array(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)] += 1
    return count


# removeDirtyChars takes two string as arguments: First string (str)  is the one from where function removes dirty
# chars. Second  string is the string which contain all dirty characters which need to be removed  from first string
def remove_chars(string, mask_string):
    count = getchar_count_array(mask_string)
    ip_ind = 0
    res_ind = 0
    temp = ' '
    str_list = tolist(string)

    while ip_ind != len(str_list):
        temp = str_list[ip_ind]
        if count[ord(temp)] == 0:
            str_list[res_ind] = str_list[ip_ind]
            res_ind += 1
        ip_ind += 1

    # After above step string is ngring.Removing extra "iittg" after string
    return tostring(str_list[0:res_ind])


# Driver function to test the above functions
mask_string = "mask"
string = "geeksforgeeks"
print(remove_chars(string, mask_string))
