import os
import subprocess
import shutil

# 경로 설정
SOURCE_DIR = r"C:\Users\윤태훈\OneDrive\Desktop\ai_origin\log_Section"
GIT_REPO_DIR = r"C:\Users\윤태훈\daily-test"
TARGET_SUBFOLDER = os.path.join(GIT_REPO_DIR, "logs", "2025-02")

# 1. 복사: 최신 파일들 Git 레포로 옮기기
os.makedirs(TARGET_SUBFOLDER, exist_ok=True)

for file in os.listdir(SOURCE_DIR):
    if file.endswith(".json"):
        src = os.path.join(SOURCE_DIR, file)
        dst = os.path.join(TARGET_SUBFOLDER, file)
        shutil.copyfile(src, dst)

# 2. Git add → commit → push
subprocess.run(["git", "add", "."], cwd=GIT_REPO_DIR)
subprocess.run(["git", "commit", "-m", "자동 로그 푸시"], cwd=GIT_REPO_DIR)
subprocess.run(["git", "push"], cwd=GIT_REPO_DIR)
