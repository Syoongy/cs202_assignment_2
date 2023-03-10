import sys


def convert_to_int_arr(hex_string_list):
    ret_list = []
    for hex_string in hex_string_list:
        ret_list.append(int(hex_string, 16))
    return ret_list


# Total time complexity is O(m * n).
# We iterate over every value of a which takes O(m) time
# We then use an inner loop to iterate through all elements of b
# which takes O(n) time
def LCIS(a, b):
    a_list = convert_to_int_arr(a)
    b_list = convert_to_int_arr(b)
    a_length = len(a_list)
    b_length = len(b_list)
    # table[val] is going to store length of LCIS
    # ending with arr2[val]. We initialize it as 0,
    table = [0] * b_length
    for b_idx in range(b_length):
        table[b_idx] = 0

    # We want to iterate through all elements of a_list
    # and compare it against all elements of b_list
    for a_idx in range(a_length):
        a_val = a_list[a_idx]
        # Reset current LCIS length
        current = 0

        for b_idx in range(b_length):

            b_val = b_list[b_idx]
            # If value is the same, we increment current length by 1
            if (a_val == b_val):
                # We just increment if the current value + 1 is
                # higher than the previous stored value
                if (current + 1 > table[b_idx]):
                    table[b_idx] = current + 1

            # Now seek for previous smaller common
            # element for current element of arr1
            if (a_val > b_val):
                if (table[b_idx] > current):
                    current = table[b_idx]

    # The maximum value in table[]
    # is out result
    result = 0
    for b_idx in range(b_length):
        if (table[b_idx] > result):
            result = table[b_idx]

    return result


num_pair = int(sys.stdin.readline())
for _ in range(num_pair):
    a = sys.stdin.readline().split()
    b = sys.stdin.readline().split()
    print(LCIS(a, b))
