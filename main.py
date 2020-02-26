def palindrome(number):
    return tuple(reversed(tuple(str(number))))


def is_palindrome(number):
    return True if tuple(str(number)) == palindrome(number) else False


if __name__ == "__main__":
    print("\nWelcome to Reverse and Add!")
    while True:
        try:
            user_val = input("\nEnter a number (E to exit): ")
            if user_val.strip().lower() == "e":
                print("Exiting...\nGood bye!")
                break
            input_ = int(user_val)
            if input_ <= 0:
                print("Please try again!")
                continue
            sum_ = input_
            temp = i = 0
            if is_palindrome(input_):
                p_ = int("".join(palindrome(input_)))
                sum_ = input_ + p_
                print("{}. {} + {} = {}\n".format(1, input_, p_, sum_))
            while not is_palindrome(sum_):
                palindrome_ = int("".join(palindrome(sum_)))
                temp = sum_
                sum_ += palindrome_
                i += 1
                print("{}. {} + {} = {}".format(i, temp, palindrome_, sum_))
            print("Sum is a palindrome!")

        except ValueError as e:
            print("Detected invalid input! Please try again.".format(e))
            continue
