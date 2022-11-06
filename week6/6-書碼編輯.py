from collections import defaultdict
book_name_order = list()
book_name_count = defaultdict(int)
book_number = 0
ans = defaultdict(list)
while True:
    book = input()
    if book == "0":
        break
    # book_name_order
    if book not in book_name_order:
        book_name_order.append(book)
    order = str(book_name_order.index(book) + 1)
    # book_name_count
    book_name_count[book] += 1
    count = str(book_name_count[book])
    # book_number
    book_number += 1
    number = str(book_number)
    
    book_num = order.zfill(3) + count.zfill(3) + number.zfill(4)
    ans[book].append(book_num)
for key, value in ans.items():
    print(key + " " + " ".join(value))

    