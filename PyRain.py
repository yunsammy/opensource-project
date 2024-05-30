import random
import pygame
import time


# 퀴즈 생성 클래스
class QuizClass:
    
    @staticmethod
    def quizMethod():
        with open('gametext.txt', 'r', encoding='utf-8') as f:
            a = f.read()
            b = a.split(' ')
        return b


def game(level):
    a = QuizClass.quizMethod()

    # 색상 설정 변수
    black = (0, 0, 0)
    white = (255, 255, 255)
    sky_blue = (153, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    gray = (153, 153, 153)

    # pygame 초기화
    pygame.init()

    # 화면 생성
    screen = pygame.display.set_mode((800, 600))

    # 배경화면
    background = pygame.image.load('bg2.png')

    # 제목 설정
    pygame.display.set_caption("맞춰보라게")

    # 퀴즈 변수
    quizX = []
    quizY = []
    quizY_change = []
    speed_of_quiz = len(a)

    sf = pygame.font.Font("NanumGothic-Bold.ttf", 30)

    # 퀴즈의 위치 및 속도 설정 변수
    for i in range(speed_of_quiz):
        quizX.append(random.randint(50*i, 50*i+50))
        quizY.append(random.randint(-100, -50))
        quizY_change.append(level*0.2)

    # 점수 초기화
    score_value = 0
    font = pygame.font.Font('NanumGothic-Bold.ttf', 32)
    textX = 10
    textY = 10

    # 게임오버 폰트 설정
    over_font = pygame.font.Font('"NanumGothic-Bold.ttf"', 64)

    # 점수 표시 함수
    def show_score(x, y):
        score = font.render("Score : " + str(score_value), True, (0, 0, 0))
        screen.blit(score, (x, y))

    # 게임오버 함수
    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (0, 0, 0))
        screen.blit(over_text, (200, 250))

    # 게임클리어 함수
    def game_clear_text():
        over_text = over_font.render("{}stage clear!".format(level), True, (0, 0, 0))
        screen.blit(over_text, (200, 250))

    # 퀴즈 화면 생성 함수
    def quiz(x, y):
        screen.blit(text, (x, y))

    # 퀴즈 충돌 관련 함수
    def isCollision(j):
        if inputStr == j:
            return True
        else:
            False

    inputStr = ''
    processed_words = set()  # 처리된 단어들을 저장할 집합

    # 게임 루프 설정 변수
    global z
    z = False
    x = False
    running = True
    while running:

        # 배경화면 채우기
        screen.fill((0, 0, 0))
        # 이미지 파일 불러오기
        screen.blit(background, (0, 0))
        font1 = pygame.font.Font(None, 30)

        # 이벤트 처리
        for _event in pygame.event.get():

            if _event.type == pygame.QUIT:
                running = False
                pygame.quit()

            # 키보드 이벤트 처리
            if _event.type == pygame.KEYDOWN:
                if _event.unicode.isalpha():  # 문자열인지 아닌지
                    inputStr += _event.unicode
                elif _event.key == pygame.K_BACKSPACE:
                    inputStr = inputStr[:-1]
                elif _event.key == pygame.K_RETURN:
                    inputStr = ""  # 지우기

        for i in range(speed_of_quiz):
            text = sf.render(a[i], True, (0, 0, 0))
            tt = a[i]
            # 게임오버 시
            if quizY[i] > 550:
                for j in range(speed_of_quiz):
                    quizY[j] = 2000
                game_over_text()
                x=True
                z=True
                break

            quizY[i] += quizY_change[i]

            # 충돌 시
            collision = isCollision(tt)
            # 초기 위치로 되돌리기
            if collision and tt not in processed_words:
                score_value += 10
                inputStr = ''
                quizX[i] = random.randint(0, 736)
                quizY[i] = random.randint(-150, -100)
                processed_words.add(tt)  # 처리된 단어로 추가

            quiz(quizX[i], quizY[i])

            # 게임 클리어 시
            if score_value == 50:
                x=True
                game_clear_text()
                break

        # 타이핑 구간 생성 및 설정
        targetRect = pygame.draw.rect(screen, gray, [300, 550, 200, 20])
        block = font1.render(inputStr, True, (255, 255, 161))
        rect = block.get_rect()
        rect.topleft = targetRect.topleft  # 왼쪽 정렬

        screen.blit(block, rect)
        show_score(textX, textY)
        pygame.display.update()

        if x:
            break
    time.sleep(2)
