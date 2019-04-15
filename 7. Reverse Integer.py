def reverse(data):
    k = len(data) - 1
    data_str = str(data)
    new_data = ''
    if (2 ** 31) - 1 < int(data) < (-2) ** 31:
        return 0
    elif data_str[0] == '-':
        new_data = '-'
        while k > 0 and data_str[k] == '0':
            k -= 1
        while k > 0:
            new_data = new_data + data_str[k]
            k -= 1
        print(new_data)
    elif data_str[0] != '-':
        while k > 0 and data_str[k] == '0':
            k -= 1
        while k >= 0:
            new_data = new_data + data_str[k]
            k -= 1
        print(new_data)


number = input("Please, write a number: ")
reverse(number)
