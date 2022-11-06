chinese_english = dict()
english_chinese = dict()

while True:
    command, *info = input().split()
    if command == "I":
        chinese, english = info
        if chinese in chinese_english:
            print("[fail]")
        else:
            chinese_english.update({chinese: english})
            english_chinese.update({english: chinese})
            print("[succeed]")
    elif command == "C":
        chinese = info[0]
        print(chinese_english.get(chinese, "[fail]"))
    elif command == "E":
        english = info[0]
        print(english_chinese.get(english, "[fail]"))
    elif command == "Q":
        break