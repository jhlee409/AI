import os
from PIL import Image

# 폴더 경로 설정
folder_path = r'F:\OneDrive - UOU\LLM\EGD_Dx'

# 폴더 내의 모든 파일을 가져옴
file_list = os.listdir(folder_path)

# tif 파일을 찾아 확장자를 png로 변경하고 원본 파일 삭제
for file in file_list:
    if file.endswith(".tif"):
        # 파일 경로 생성
        file_path = os.path.join(folder_path, file)
        
        # 이미지 파일을 연다
        img = Image.open(file_path)
        
        # 확장자를 변경하여 파일 이름 생성
        new_file_path = os.path.splitext(file_path)[0] + ".png"
        
        # png로 저장
        img.save(new_file_path, "PNG")
    if file.endswith(".jpg"):
        # 파일 경로 생성
        file_path = os.path.join(folder_path, file)
        
        # 이미지 파일을 연다
        img = Image.open(file_path)
        
        # 확장자를 변경하여 파일 이름 생성
        new_file_path = os.path.splitext(file_path)[0] + ".png"
        
        # png로 저장
        img.save(new_file_path, "PNG")
        
file_list = os.listdir(folder_path)

# tif 파일을 찾아 삭제
for file in file_list:
    if file.endswith(".tif"):
        # 파일 경로 생성
        file_path = os.path.join(folder_path, file)
        
        # 파일 삭제
        os.remove(file_path)
    if file.endswith(".jpg"):
        # 파일 경로 생성
        file_path = os.path.join(folder_path, file)
        
        # 파일 삭제
        os.remove(file_path)

# 이미지 폴더 경로
src_dir = r'F:\OneDrive - UOU\LLM\EGD_Dx'

# 결과 폴더 경로
dst_dir = os.path.join(src_dir, 'result')

# 결과 폴더가 없으면 생성
os.makedirs(dst_dir, exist_ok=True)

for filename in os.listdir(src_dir):
    if filename.endswith('.png'):
        img_path = os.path.join(src_dir, filename)

        # 이미지 열기
        img = Image.open(img_path)

        # 이미지가 정사각형이 아닌 경우, 정사각형으로 만들기
        width, height = img.size
        min_dim = min(width, height)
        left = (width - min_dim) / 2
        top = (height - min_dim) / 2
        right = (width + min_dim) / 2
        bottom = (height + min_dim) / 2
        img = img.crop((left, top, right, bottom))

        # 이미지 크기 조절
        img = img.resize((224, 224))

        # 결과 저장
        img.save(os.path.join(dst_dir, filename))
