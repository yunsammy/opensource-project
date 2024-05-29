import random
import pygame
import time


# quiz 생성 클래스
class QuizClass:
    
    @staticmethod
    def quizMethod():
        with open('gametext.txt', 'r') as f:
            a = f.read()
        b = a.split()
        return b


def game(level):
    a = QuizClass.quizMethod()

    # 색상설정 변수
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

    # quiz 변수
    quizX = []
    quizY = []
    quizY_change = []
    speed_of_quiz = len(a)

    sf = pygame.font.SysFont("freesansbold.ttf", 30)

    # 텍스트 크기 변수
    text_width, text_height = 50, 30  # 대략적인 텍스트 크기

    # 사용된 위치 추적 리스트
    used_positions = []

    # quiz의 위치 및 속도 설정 변수
    for i in range(speed_of_quiz):
        while True:
            x = random.randint(0, 800 - text_width)
            y = random.randint(-100, -50)
            overlap = False
            
            for (ux, uy) in used_positions:
                if abs(x - ux) < text_width and abs(y - uy) < text_height:
                    overlap = True
                    break
            
            if not overlap:
                quizX.append(x)
                quizY.append(y)
                used_positions.append((x, y))
                quizY_change.append(level * 0.2)
                break

    # 점수 초기화
    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    textX = 10
    textY = 10

    # Game Over 폰트설정
    over_font = pygame.font.Font('freesansbold.ttf', 64)

    # 점수표시 함수
    def show_score(x, y):
        score = font.render("Score : " + str(score_value), True, black)
        screen.blit(score, (x, y))

    # 게임오버 함수
    def game_over_text():
        over_text = over_font.render("GAME OVER", True, black)
        screen.blit(over_text, (200, 250))
        sound = pygame.mixer.Sound( "sounds/gameover.mp3" )
        sound.play()

    # 게임클리어 함수
    def game_clear_text():
        over_text = over_font.render(f"{level} stage clear!", True, black)
        screen.blit(over_text, (200, 250))
        sound = pygame.mixer.Sound( "sounds/clear.mp3" )
        sound.play()

    # quiz 화면 생성 함수
    def quiz(x, y, text):
        screen.blit(text, (x, y))

    # quiz 충돌관련 함수
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
    while running:

        # 배경화면 채우기
        screen.fill(black)
        # 이미지파일 불러오기
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
            text = sf.render(a[i], True, black)
            tt = a[i]
            # Game Over시
            if quizY[i] > 550:
                for j in range(speed_of_quiz):
                    quizY[j] = 2000
                game_over_text()
                x = True
                z = True
                break

            quizY[i] += quizY_change[i]

            # 충돌 시
            collision = isCollision(tt)
            # 초기 위치로 되돌리기
            if collision:
                score_value += 10
                inputStr = ''
                while True:
                    new_x = random.randint(0, 800 - text_width)
                    new_y = random.randint(-150, -100)
                    overlap = False

                    for (ux, uy) in used_positions:
                        if abs(new_x - ux) < text_width and abs(new_y - uy) < text_height:
                            overlap = True
                            break

                    if not overlap:
                        quizX[i] = new_x
                        quizY[i] = new_y
                        used_positions.append((new_x, new_y))
                        break

            quiz(quizX[i], quizY[i], text)

            # Game Clear시
            if score_value == 50:
                x = True
                game_clear_text()
                break

        # 타이핑 구간 생성 및 설정
        targetRect = pygame.draw.rect(screen, gray, [300, 550, 200, 20])
        block = font1.render(inputStr, True, (255, 255, 161))
        rect = block.get_rect()
        rect.topleft = targetRect.topleft  # 왼쪽정렬

        screen.blit(block, rect)
        show_score(textX, textY)
        pygame.display.update()

        if x:
            break
    time.sleep(2)

