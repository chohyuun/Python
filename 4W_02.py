def count_word(text, word):
    save_text = open('test.txt', 'w', encoding="UTF-8")
    save_text.write(text)
    save_text.close()

    # 파일 읽을때 인코딩 방식 변경(Python3 부터 변경됨)
    use_text = open('test.txt', 'r', encoding="UTF-8")

    count = 0
    word_len = len(word)  # 찾고자 하는 문자의 길이

    # for 문을 통해 한 줄씩 점사
    for line in use_text:
        # word가 문장안에 들어있을 경우
        if word in line:
            # 문자 하나하나씩 검사
            for num in range(0, len(line)):
                # 만약 문자 길이가 같고 같은 문자를 나타낸다면 count 증가
                if line[num:num + word_len] == word:
                    count += 1

    print("문장안에 '{}'(이)라는 단어의 개수: {}".format(word, count))


test = """파이썬은 초보자부터 전문가까지 사용자층을 보유하고 있다. 
동적 타이핑(dynamic typing) 범용 프로그래밍 언어로, 펄 및 루비와 자주 비교된다. 
다양한 플랫폼에서 쓸 수 있고, 라이브러리(모듈)가 풍부하여, 대학을 비롯한 여러 교육 기관, 연구 기관 및 산업계에서 이용이 증가하고 있다. 
또 파이썬은 순수한 프로그램 언어로서의 기능 외에도 다른 언어로 쓰인 모듈들을 연결하는 풀언어(glue language)로써 자주 이용된다. 
실제 파이썬은 많은 상용 응용 프로그램에서 스크립트 언어로 채용되고 있다. 도움말 문서도 정리가 잘 되어 있으며, 유니코드 문자열을 지원해서 다양한 언어의 문자 처리에도 능하다."""

word = "언어"
count_word(test, word)