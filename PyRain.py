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

# 게임 함수
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
    pygame.display.set_caption("PyRain")

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
        quizY_change.append(level * 0.2)

    # 점수 초기화
    score_value = 0
    font = pygame.font.Font('NanumGothic-Bold.ttf', 32)
    textX = 10
    textY = 10

    # 게임오버 폰트 설정
    over_font = pygame.font.Font('NanumGothic-Bold.ttf', 64)

    # 점수 표시 함수
    def show_score(x, y):
        score = font.render("Score : " + str(score_value), True, (0, 0, 0))
        screen.blit(score, (x, y))

    # 게임오버 함수
    def game_over_text():
        over_text = over_font.render("Game Over", True, (255, 0, 0))
        over_text_rect = over_text.get_rect(center=(400, 250))
        screen.blit(over_text, over_text_rect)
        final_score = over_font.render("Score: " + str(score_value), True, (0, 0, 0))
        final_score_rect = final_score.get_rect(center=(400, 320))
        screen.blit(final_score, final_score_rect)

    # 게임클리어 함수
    def game_clear_text():
        clear_text = over_font.render("Clear!", True, (0, 255, 0))
        clear_text_rect = clear_text.get_rect(center=(400, 250))
        screen.blit(clear_text, clear_text_rect)
        final_score = over_font.render("Score: " + str(score_value), True, (0, 0, 0))
        final_score_rect = final_score.get_rect(center=(400, 320))
        screen.blit(final_score, final_score_rect)
        
    # 퀴즈 화면 생성 함수
    def quiz(x, y):
        screen.blit(text, (x, y))

    # 퀴즈 충돌 관련 함수
    def isCollision(j):
        if inputStr == j:
            return True
        else:
            return False

    inputStr = ''
    # 게임 루프 설정 변수
    global z
    z = False
    x = False
    running = True

    input_active = True  # 게임 시작 시 입력란을 활성화 상태로 설정

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
            if _event.type == pygame.KEYDOWN and input_active:
                if _event.unicode.isalpha():  # 문자열인지 아닌지
                    inputStr += _event.unicode
                elif _event.key == pygame.K_BACKSPACE:
                    inputStr = inputStr[:-1]
                elif _event.key == pygame.K_RETURN:
                    # 엔터 키를 눌렀을 때만 충돌을 체크합니다.
                    for i in range(speed_of_quiz):
                        if isCollision(a[i]):
                            score_value += 10
                            inputStr = ''
                            quizX[i] = random.randint(0, 736)
                            quizY[i] = random.randint(-150, -100)
                    inputStr = ""  # 입력 초기화
            
            # 마우스 클릭 이벤트 처리
            if _event.type == pygame.MOUSEBUTTONDOWN:
                if targetRect.collidepoint(_event.pos):
                    input_active = True  # 입력란 클릭 시 활성화
                else:
                    input_active = False  # 입력란 이외의 부분 클릭 시 비활성화

        for i in range(speed_of_quiz):
            text = sf.render(a[i], True, (0, 0, 0))
            tt = a[i]
            # 게임오버 시
            if quizY[i] > 550:
                for j in range(speed_of_quiz):
                    quizY[j] = 2000
                game_over_text()
                x = True
                z = True
                break

            quizY[i] += quizY_change[i]

            quiz(quizX[i], quizY[i])

            # 게임 클리어 시
            if score_value == 50:
                x = True
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
