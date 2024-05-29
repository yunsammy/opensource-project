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

# 전역 점수 변수
total_score = 0

# 게임 함수
def game(level):
    global total_score
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

    # 텍스트 크기 변수
    text_sizes = [sf.size(word) for word in a]  # 각 텍스트의 크기
    text_widths = [size[0] for size in text_sizes]
    text_heights = [size[1] for size in text_sizes]

    # 사용된 위치 추적 리스트
    used_positions = []

    # quiz의 위치 및 속도 설정 변수
    for i in range(speed_of_quiz):
        while True:
            x = random.randint(0, 800 - text_widths[i])
            y = random.randint(-100, -50)
            overlap = False

            for (ux, uy, uw, uh) in used_positions:
                if abs(x - ux) < uw and abs(y - uy) < uh:
                    overlap = True
                    break

            if not overlap:
                quizX.append(x)
                quizY.append(y)
                used_positions.append((x, y, text_widths[i], text_heights[i]))
                quizY_change.append(level * 0.2)
                break

    # 점수 초기화
    font = pygame.font.Font('NanumGothic-Bold.ttf', 32)
    textX = 10
    textY = 10

    # 게임오버 폰트 설정
    over_font = pygame.font.Font('NanumGothic-Bold.ttf', 64)

    # 점수 표시 함수
    def show_score(x, y):
        score = font.render("Score : " + str(total_score), True, (0, 0, 0))
        screen.blit(score, (x, y))

    # 게임오버 함수
    def game_over_text():
        over_text = over_font.render("Game Over", True, (255, 0, 0))
        over_text_rect = over_text.get_rect(center=(400, 250))
        screen.blit(over_text, over_text_rect)
        final_score = over_font.render("Score: " + str(total_score), True, (0, 0, 0))
        final_score_rect = final_score.get_rect(center=(400, 320))
        screen.blit(final_score, final_score_rect)
        sound = pygame.mixer.Sound("sounds/gameover.mp3")
        sound.play()

    # 게임클리어 함수
    def game_clear_text():
        clear_text = over_font.render("Clear!", True, (0, 255, 0))
        clear_text_rect = clear_text.get_rect(center=(400, 250))
        screen.blit(clear_text, clear_text_rect)
        final_score = over_font.render("Score: " + str(total_score), True, (0, 0, 0))
        final_score_rect = final_score.get_rect(center=(400, 320))
        screen.blit(final_score, final_score_rect)
        sound = pygame.mixer.Sound("sounds/clear.mp3")
        sound.play()

    # 퀴즈 화면 생성 함수
    def quiz(x, y, text):
        screen.blit(text, (x, y))

    # 퀴즈 충돌 관련 함수
    def isCollision(j):
        return inputStr == j

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
                            total_score += 10
                            inputStr = ''
                            while True:
                                new_x = random.randint(0, 800 - text_widths[i])
                                new_y = random.randint(-150, -100)
                                overlap = False

                                for (ux, uy, uw, uh) in used_positions:
                                    if abs(new_x - ux) < uw and abs(new_y - uy) < uh:
                                        overlap = True
                                        break

                                if not overlap:
                                    quizX[i] = new_x
                                    quizY[i] = new_y
                                    used_positions.append((new_x, new_y, text_widths[i], text_heights[i]))
                                    break
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
            # 충돌 시
            collision = isCollision(tt)
            # 초기 위치로 되돌리기
            if collision:
                total_score += 10
                inputStr = ''
                while True:
                    new_x = random.randint(0, 800 - text_widths[i])
                    new_y = random.randint(-150, -100)
                    overlap = False

                    for (ux, uy, uw, uh) in used_positions:
                        if abs(new_x - ux) < uw and abs(new_y - uy) < uh:
                            overlap = True
                            break

                    if not overlap:
                        quizX[i] = new_x
                        quizY[i] = new_y
                        used_positions.append((new_x, new_y, text_widths[i], text_heights[i]))
                        break

            quizY[i] += quizY_change[i]

            quiz(quizX[i], quizY[i], text)

            # 게임 클리어 시
            if total_score >= 50:
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
