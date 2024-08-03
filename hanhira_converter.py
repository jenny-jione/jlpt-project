# 한국어 발음을 히라가나로 변환하는 코드 (2024.6.29)
"""
input : 시아와세
output: しあわせ

파일일 경우
hanhira_text_input.txt
코노 혼왛 오모시로이데스./이 책은 재미있습니다.

hanhira_text_output.txt
この ほんは おもしろいです。
이 책은 재미있습니다.
"""

from hanhira_dict import hanhira

addie = []  # 딕셔너리에 없는 값을 체크하기 위한 리스트

def convert_to_hiragana(text: str):
    global addie
    hira, read = '', ''
    # 발음을 히라가나로 변환
    for char in text:
        if char in hanhira:
            hira += hanhira[char]
        else:
            # 딕셔너리에 없지만 3000엔 같은 경우에는 나타내지 않게 하기 위한 조건문
            if not char.isdigit():
                addie.append(char)
                print(f'{char} :: {text}')
            hira += char
        if char=='왛':
            read += '와'
        elif char=='워':
            read += '오'
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
    with open('./hanhira_text_input.txt', 'r') as f1,\
    open('./hanhira_text_output.txt', 'w') as f2:
        data = f1.readlines()
        for line in data:
            read, mean = line.strip().split('/')
            hira, read_new = convert_to_hiragana(read)
            f2.write(f'{hira}\n')
            f2.write(f'{mean}\n\n')
        print(f'{len(data)} data successfully converted.')

    if len(addie)>0:
        print()
        print(''.join(list(set(addie))))
        print(len(set(addie)))
else:
    print('선택이 잘못됨')