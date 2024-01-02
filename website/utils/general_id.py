import itertools
import string

# 定義字符集，包括0-9和小寫字母A-Z，但排除字母 "I" 和 "O"
characters = ''.join([c for c in string.digits + string.ascii_uppercase if c not in 'IO'])

# 定義編號的長度
length = 5

# 設定計數器的起始值
start_value = 1
counter = itertools.count(start=start_value)

def generate_record_code():
    # 獲取下一個計數值
    count = next(counter)
    
    # 計算編號的位數
    code_length = len(characters)
    
    # 初始化一個空字符串來存儲編號
    code = ""
    
    # 將計數值轉換成編號字符串
    while count > 0:
        count, index = divmod(count - 1, code_length)
        code = characters[index] + code
    
    # 將編號擴展到指定的長度
    if len(code) < length:
        code = characters[0] * (length - len(code)) + code
    
    return code 

# 測試列印
# for i in range(1000):
#     next_ordered_number = generate_record_code()
#     print(next_ordered_number)

