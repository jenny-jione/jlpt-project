import csv
from hiragana_conversion_dict import hanhira

def convert_to_hiragana(text: str):
    result = ''
    for char in text:
        if char in hanhira:
            result += hanhira[char]
        else:
            result += char
    return result

def print_result(data):
    for hira, mean, read in data:
        print(f'{hira}\t{mean}\t{read}')

result = []

input_type = input('입력 타입 선택(1.터미널 입력 변환 2.파일 변환):')
# input_type = '2'
if input_type == '1':
    s = input()
    read, mean = s.split('\t')
    hira = convert_to_hiragana(read)
    print_result([hira, read, mean])
    
elif input_type == '2':
    with open('./jlpt_flashcard_input.txt', 'r') as f1,\
          open('./jlpt_flashcard.csv', 'w') as f2:
        data = f1.readlines()
        wr = csv.writer(f2)
        wr.writerow(['단어', '발음', '뜻'])

        for line in data:
            read, mean = line.strip().split('/')
            hira = convert_to_hiragana(read)
            wr.writerow([hira, read, mean])
    print(f'{len(data)} data successfully converted.')
else:
    print('선택이 잘못됨')