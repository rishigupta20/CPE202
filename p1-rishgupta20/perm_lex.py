# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
def perm_gen_lex(str_in):  # Defining function
    if len(str_in) == 0:  # Base Case for Empty String
        return []
    if len(str_in) == 1:  # Base Case for 1 letter String
        return [str_in]
    result = []  # Result String where different strings will be appended
    for i in range(len(str_in)):  # For Loop iterating through length of string
        case = str_in[i]  # Creating specific case variable using for loop index
        new_str = str_in[:i] + str_in[i + 1:]  # Creating Simpler String variable using for loop index
        new_list = perm_gen_lex(new_str)  # Recursively calling function with the simpler string each iteration
        for j in new_list:  # Creating a for loop iterating through strings
            var = case + j  # Adding case string to each permutation of the simpler string
            result.append(var)  # Appending resulting permutation to the result list
    return result
