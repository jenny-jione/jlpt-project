# 히라가나를 한국어 발음으로 변환하는 코드 (2024.7.4)
from jamodict import *
from hirahan_dict import hirahan

# 주어진 히라가나를 한 음절씩 분리
def split_hiragana(word: str):
    """
    input: 'いらっしゃいませ'
    output : ['い', 'らっ', 'しゃ', 'い', 'ま', 'せ']

    요음/촉음/ん은 그 앞 글자에 이어서 붙임 (단독 존재x)
    """
    stegana = ['ゃ', 'ゅ', 'ょ', 'っ', 'ん',
               'ャ', 'ュ', 'ョ', 'ッ', 'ン',
               'ぁ', 'ぃ', 'ぅ', 'ぇ', 'ぉ', 'ゕ', 'ゖ', 'ゎ']
    result = []
    idx = 0
    syllable = ''
    while True:
        if idx >= len(word):
            result.append(syllable)
            break
        if word[idx] in stegana:
            syllable += word[idx]
        else:
            if syllable:
                result.append(syllable)
            syllable = word[idx]
        idx += 1
    return result
# split_hiragana('がまんする')


# 분리된 히라가나를 한글로 대응시키기
def hira_to_hangeul(syllable: str):
    """
    input: 'まん'
    output: ['마', 'ㄴ']
    """
    result = []
    for ch in syllable:
        result.append(hirahan[ch])
    return result
# hira_to_hangeul('おきゃくさん')


# 자모 분리
def split_jamo(hangeuls: list):
    """
    input: ['마', 'ㄴ']
    output: ['ㅁ', 'ㅏ', 'ㄴ']

    input: ['키', 'ㅑ']
    output: ['ㅋ', 'ㅑ']
    ㅑ, ㅠ, ㅛ가 있을 경우에는 앞의 모음을 제거하고 대체한다.
    """
    result = []
    for char in hangeuls:
        if '가'<=char<='힣':
            ch1 = (ord(char) - BASE_CODE) // CHOSUNG_CODE
            ch2 = (ord(char) - BASE_CODE - CHOSUNG_CODE * ch1) // JUNGSUNG_CODE
            result.append(CHOSUNG_LIST[ch1])
            result.append(JUNGSUNG_LIST[ch2])        
        else:
            if char in 'ㅑㅠㅛ':
                result[-1] = char
            else:
                result.append(char)
    return result
# split_jamo(['키', 'ㅑ'])
# split_jamo(['라', 'ㅅ'])
# split_jamo(['마', 'ㄴ'])


# 자음과 모음을 한 글자의 한글로 조합하는 함수
def combine_jamo(chars: list):
    """
    input: ['ㅇ', 'ㅏ', 'ㄴ']
    output: '안'

    한글 유니코드 값 구하는 공식
    (초성 * 588) + (중성 * 28) + 종성 + 44032
    """
    result_code = BASE_CODE + CHOSUNG_LIST.index(chars[0]) * CHOSUNG_CODE
    if len(chars)>1:
        result_code += JUNGSUNG_LIST.index(chars[1]) * JUNGSUNG_CODE
    if len(chars)>2:
        result_code += JONGSUNG_LIST.index(chars[2])
    return chr(result_code)
# chars = ['ㅇ', 'ㅏ', 'ㄴ']
# combine_jamo(chars)


# 전체 함수
def hiragana_convert(hira):
    """
    input: 'いらっしゃいませ'
    output: '이랏샤이마세'
    """
    han = ''
    # 주어진 히라가나를 한 음절씩 분리
    syllables = split_hiragana(hira)
    for syllable in syllables:
        # 히라가나가 아닌 것은 continue
        if syllable in ' -ー=':
            han += syllable
            continue
        # 분리된 히라가나를 한글로 대응시키기
        hangeuls = hira_to_hangeul(syllable)
        jamos = split_jamo(hangeuls)
        hangeul_char = combine_jamo(jamos)
        han += hangeul_char
    return han
print(hiragana_convert('いらっしゃいませ'))