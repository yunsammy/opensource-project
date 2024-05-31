from PIL import Image
import os

def resize_images(input_paths, output_paths, size=(800, 600)):
    """
    여러 이미지 파일을 열어 크기를 변경한 후 저장하는 함수.

    :param input_paths: 원본 이미지 파일 경로 리스트
    :param output_paths: 리사이즈된 이미지 저장 경로 리스트 (파일 이름과 확장자 포함)
    :param size: (width, height) 형태의 튜플로 리사이즈할 크기
    """
    for input_path, output_path in zip(input_paths, output_paths):
        # 이미지 열기
        with Image.open(input_path) as img:
            # 이미지 리사이즈
            resized_img = img.resize(size)
            
            # 리사이즈된 이미지 저장
            resized_img.save(output_path)
            print(f"이미지가 성공적으로 저장되었습니다: {output_path}")


# 사용 예시
input_image_paths = [
    "C:\\Users\\user\\Desktop\\한라산.jpeg",
    "C:\\Users\\user\\Desktop\\돌하르방.jpeg"
]  # 원본 이미지 파일 경로
output_image_paths = [
    "C:\\Users\\user\\Desktop\\한라산1.jpeg",
    "C:\\Users\\user\\Desktop\\돌하르방1.jpeg"
]  # 리사이즈된 이미지 저장 경로 (파일 이름과 확장자 포함)

resize_images(input_image_paths, output_image_paths)
