import os
import json
import subprocess
from datetime import datetime

# 로그 데이터 예시
log_data = {
    "timestamp": datetime.now().isoformat(),
    "message": "예시 로그 메시지",
    "level": "INFO"
}

# 날짜별 디렉토리 및 파일 이름 설정
today = datetime.now()
folder_name = today.strftime("%Y-%m")
file_name = today.strftime("%d.json")
base_path = os.path.join("logs", folder_name)
os.makedirs(base_path, exist_ok=True)
file_path = os.path.join(base_path, file_name)

# 로그 파일에 데이터 추가
with open(file_path, 'a', encoding='utf-8') as f:
    f.write(json.dumps(log_data, ensure_ascii=False) + '\n')

# Git 명령어를 사용하여 변경 사항 커밋 및 푸시
subprocess.run(["git", "add", "."], cwd=".")
subprocess.run(["git", "commit", "-m", f"자동 로그 업데이트: {file_name}"])
subprocess.run(["git", "push"])
