# 한국어 발음을 히라가나로 변환하는 코드 (2024.6.29)
import csv
from hanhira_dict import hanhira

def convert_to_hiragana(text: str):
    hira, read = '', ''
    # 발음을 히라가나로 변환
    for char in text:
        if char in hanhira:
            hira += hanhira[char]
        else:
            print(f'{char} :: {text}')
            hira += char
        if char=='왛':
            read += '와'
        else:
            read += char
    return hira, read

def print_result(data):
    for hira, mean, read in data:
        print(f'{hira}\t{mean}\t{read}')

result = []

input_type = input('입력 타입 선택(1.터미널 입력 변환 2.파일 변환): ')
if input_type == '1':
    print('히라가나로 변환할 발음을 한국어로 써주세요. (단, 조사 は는 \'왛\'로, を는 \'워\'로 입력)')
    s = input()
    hira, read = convert_to_hiragana(s)
    print(f'{read} -> {hira}')
    
elif input_type == '2':
    with open('./jlpt_flashcard_input.txt', 'r') as f1,\
          open('./jlpt_flashcard.csv', 'w') as f2:
        data = f1.readlines()
        wr = csv.writer(f2)
        wr.writerow(['단어', '발음', '뜻'])

        for line in data:
            read, mean = line.strip().split('/')
            hira, read_new = convert_to_hiragana(read)
            wr.writerow([hira, read_new, mean])
    print(f'{len(data)} data successfully converted.')
else:
    print('선택이 잘못됨')