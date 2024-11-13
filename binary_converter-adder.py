""" "Utils" functions """

# Takes any positive int and converts it to a string containing the corresponding binary number
def convert_int_to_bin(number: int) -> str:
    # Check if the number is positive or if it is equal to 0 (because otherwose the loop won't iterate resulting in no result)
    if number < 0:
        raise ValueError("Number must be a positive integer")
    
    if number == 0:
        return "0"
    
    # Init the list of the rest of the divisions and some vars we'll use in the loop
    bin_result = []
    next_number = number
    index = 0

    # Compute the quotient and rest of each euclidian division
    while next_number > 0:
        bin_result.insert(index, next_number % 2)
        next_number = next_number // 2
        index += 1
    
    # Format the result of the operations
    bin_result.reverse()
    formatted_bin_result = str(bin_result).replace("[", "").replace("]", "").replace(",", "").replace(" ", "")

    return formatted_bin_result



    
def add_two_binary_numbers(number_one: str, number_two: str) -> str:
    # Init for the loop then
    result = []
    carry = 0

    # Set all numbers to the same length cause it's damn easier, also get their final length to use it in the loop
    biggest_binary_length = max(len(number_one), len(number_two))
    number_one = number_one.zfill(biggest_binary_length)
    number_two = number_two.zfill(biggest_binary_length)

    # Converting the strs to lists and reverse them so they are ready for the sum up (it starts from the right)
    number_one = list(number_one)
    number_two = list(number_two)
    number_one.reverse()
    number_two.reverse()

    for counter in range(biggest_binary_length):
        # Get the bits we will add
        bit_one = number_one[counter]
        bit_two = number_two[counter]

        # Add both bits and the carry
        sum_up = int(bit_one) + int(bit_two) + carry

        """
        sum_up can be either 1, 2, 3 or 0,
        if it is 1 either the carry, or one of the bits is 1 but the others are 0 so we have 0+0+1 with no carry -> 1
        if it is 2 either the carry and one of the bits or both bits are 1 with no carry so we have 1+1+0 -> 0 (and we carry one)
        if it is 3 the carry and both bits are one so we have 1+1+1 -> 1 (and we carry one)
        if it is 0 the carry and both bits are 0 so we have 0+0+0 -> 0
        And using the modulo gives us that result, see later how the carried bits are managed
        """
        result.append(sum_up%2)

        """
        if it is 1 there are no carry
        if it is 2 there is a carry
        if it is 3 there is a carry
        if it is 0 there are no carry
        and the euclidian division gives us that carry
        """
        carry = sum_up // 2

    # If there's an extra bit carried, we add it at the end
    if carry == 1:
        result.append(1)

    # Format the result
    result.reverse()
    formatted_result = str(result).replace("[", "").replace("]", "").replace(",", "").replace(" ", "")

    return formatted_result


""" Main code """
if __name__ == "__main__":
    try:
        number_one_in_decimal = int(input("Enter first number > "))
        number_two_in_decimal = int(input("Enter second number > "))
        
        number_one_in_binary = convert_int_to_bin(number_one_in_decimal)
        number_two_in_binary = convert_int_to_bin(number_two_in_decimal)
        
        print(f"{number_one_in_decimal} = {number_one_in_binary}")
        print(f"{number_two_in_decimal} = {number_two_in_binary}")
       
        print(f"{number_one_in_decimal} + {number_two_in_decimal} = {number_one_in_decimal + number_two_in_decimal}")
        print(f"{number_one_in_binary} + {number_two_in_binary} = {add_two_binary_numbers(number_one_in_binary, number_two_in_binary)}")

    except ValueError as error:
        print("Please enter number(s)")
