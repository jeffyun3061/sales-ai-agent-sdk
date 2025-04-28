import os
import boto3
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

def upload_pdf_to_s3(file_path: str, s3_key: str) -> str:
    """
    로컬 PDF 파일을 S3 버킷에 업로드하는 함수
    """
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION")
    )

    bucket_name = os.getenv("AWS_S3_BUCKET")

    s3.upload_file(file_path, bucket_name, s3_key)

    s3_url = f"https://{bucket_name}.s3.{os.getenv('AWS_REGION')}.amazonaws.com/{s3_key}"
    return s3_url


def analyze_pdf(file_path: str) -> str:
    """
    PDF 파일을 분석해서 텍스트를 추출하는 함수 (간단한 버전)
    """
    from pdfminer.high_level import extract_text

    extracted_text = extract_text(file_path)
    return extracted_text
