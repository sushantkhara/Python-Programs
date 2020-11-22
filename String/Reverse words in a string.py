# Function to reverse words of string


def reverse_words(input):
    # split words of string separated by space
    input_words = input.split(" ")

    # reverse list of words
    # suppose we have list of elements list = [1,2,3,4],
    # list[0]=1, list[1]=2 and index -1 represents
    # the last element list[-1]=4 ( equivalent to list[3]=4 )
    # So, inputWords[-1::-1] here we have three arguments
    # first is -1 that means start from last element
    # second argument is empty that means move to end of list
    # third arguments is difference of steps
    input_words = input_words[-1::-1]

    # now join words with space
    output = ' '.join(input_words)

    return output


if __name__ == "__main__":
    input = 'my name is khan'
    print(reverse_words(input))
