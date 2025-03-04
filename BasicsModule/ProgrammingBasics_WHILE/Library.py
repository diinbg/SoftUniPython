book_name = input()
book_count = 0
current_book = input()

while current_book != 'No more books':
    if current_book == book_name:
        print(f'You checked {book_count} books and found it.')
        break
    elif current_book == 'No more books':
        print('The book you search is not here!')
        print(f'You checked {book_count} books.')

    book_count += 1
    current_book = input()