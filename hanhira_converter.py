import csv
hanhira = {
    '아': 'あ',
    '이': 'い',
    '우': 'う',
    '에': 'え',
    '오': 'お',
    '카': 'か',
    '키': 'き',
    '쿠': 'く',
    '케': 'け',
    '코': 'こ',
    '사': 'さ',
    '시': 'し',
    '스': 'す',
    '세': 'せ',
    '소': 'そ',
    '타': 'た',
    '치': 'ち',
    '츠': 'つ',
    '테': 'て',
    '토': 'と',
    '나': 'な',
    '니': 'に',
    '누': 'ぬ',
    '네': 'ね',
    '노': 'の',
    '하': 'は',
    '히': 'ひ',
    '후': 'ふ',
    '헤': 'へ',
    '호': 'ほ',
    '마': 'ま',
    '미': 'み',
    '무': 'む',
    '메': 'め',
    '모': 'も',
    '야': 'や',
    '유': 'ゆ',
    '요': 'よ',
    '라': 'ら',
    '리': 'り',
    '루': 'る',
    '레': 'れ',
    '로': 'ろ',
    '와': 'わ',
    '워': 'を',
    '응': 'ん',
    '가': 'が',
    '기': 'ぎ',
    '구': 'ぐ',
    '게': 'げ',
    '고': 'ご',
    '자': 'ざ',
    '지': 'じ',
    '즈': 'ず',
    '제': 'ぜ',
    '조': 'ぞ',
    '다': 'だ',
    '디': 'ぢ',
    '드': 'づ',
    '데': 'で',
    '도': 'ど',
    '바': 'ば',
    '비': 'び',
    '부': 'ぶ',
    '베': 'べ',
    '보': 'ぼ',
    '파': 'ぱ',
    '피': 'ぴ',
    '푸': 'ぷ',
    '페': 'ぺ',
    '포': 'ぽ',
    '캬': 'きゃ',
    '큐': 'きゅ',
    '쿄': 'きょ',
    '갸': 'ぎゃ',
    '규': 'ぎゅ',
    '교': 'ぎょ',
    '샤': 'しゃ',
    '슈': 'しゅ',
    '쇼': 'しょ',
    '쟈': 'じゃ',
    '쥬': 'じゅ',
    '죠': 'じょ',
    '챠': 'ちゃ',
    '츄': 'ちゅ',
    '쵸': 'ちょ',
    '댜': 'ぢゃ',
    '뜌': 'ぢゅ',
    '뚀': 'ぢょ',
    '냐': 'にゃ',
    '뉴': 'にゅ',
    '뇨': 'にょ',
    '햐': 'ひゃ',
    '휴': 'ひゅ',
    '효': 'ひょ',
    '뱌': 'びゃ',
    '뷰': 'びゅ',
    '뵤': 'びょ',
    '퍄': 'ぴゃ',
    '퓨': 'ぴゅ',
    '표': 'ぴょ',
    '먀': 'みゃ',
    '뮤': 'みゅ',
    '묘': 'みょ',
    '랴': 'りゃ',
    '류': 'りゅ',
    '료': 'りょ'
}

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