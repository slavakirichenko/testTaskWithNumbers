class Reverser:
    def __init__(self, my_num):
        self.input = my_num

    def reverse_number(self, my_num):
        rev_num = 0
        while (my_num > 0):
            rev_part = my_num % 10
            rev_num = (rev_num * 10) + rev_part
            my_num = my_num // 10
        return (rev_num)

    def reverse_float_number(self, my_num):
        reminder = 0  ## scale of digits after decimal
        num_count = 0  ##number of digits of my num
        rev_num = 0  ## reversed

        while my_num != int(my_num):
            my_num *= 10
            reminder += 1
        while my_num > 0:
            rev_num = (rev_num * 10) + (my_num % 10)
            my_num //= 10
            num_count += 1
        rev_num = rev_num / (10 ** (num_count - reminder))

        return rev_num
