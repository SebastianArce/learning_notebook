
def unknown_binary_search(search_list):

    if len(search_list) == 1:
        return search_list[0]
    
    guess_index = len(search_list) // 2
    guess_target = search_list[guess_index]

    print(f'Our guess is: {guess_target}')
    reply = input("Enter reply: ")

    if reply == 'yes':
        print(guess_target)
        return guess_target
    
    elif reply == '>':
        print(guess_target)
        return unknown_binary_search(search_list[guess_index:])
    
    elif reply == '<':
        print(guess_target)
        return unknown_binary_search(search_list[:guess_index])

    
search_list = list(range(1, 2_097_151))
unknown_binary_search(search_list)
