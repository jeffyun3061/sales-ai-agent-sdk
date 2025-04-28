import os
import pymysql
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

def get_db_connection():
    """
    MySQL 데이터베이스 연결을 생성하는 함수
    """
    conn = pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        db=os.getenv("DB_NAME"),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.Cursor
    )
    return conn
