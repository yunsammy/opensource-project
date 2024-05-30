import requests
import xml.etree.ElementTree as ET

for page in range(1, 359):
    # API URL 설정
    url = f'http://www.jeju.go.kr/rest/JejuDialectService/getJejuDialectServiceList?page={page}'

    # API 요청 보내기
    response = requests.get(url)

    root = ET.fromstring(response.text)

    item_elems = root.findall('.//siteName')
    sound_url_elems = root.findall('.//soundUrl')

    with open('gametext.txt', 'a', encoding='utf-8') as file:
        for i, item in enumerate(item_elems):
            word = item.text

            # 입력 가능한 글자인지 확인
            isValid = True
            for c in word:
                code = ord(c)
                if code == 32 or (code >= 44032 and code <= 55203):
                    continue
                else:
                    isValid = False
                    break

            if isValid:
                file.write(word + ' ')