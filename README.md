# Lead Scout Project

## 프로젝트 개요

Lead Scout는 기업 정보를 분석하고 잠재 고객을 발굴하는 AI 기반 리드 스카우팅 시스템입니다. PDF 문서, 웹사이트, 뉴스 기사 등의 다양한 소스에서 기업 정보를 수집하고 분석하여 잠재 고객을 식별합니다.

## 주요 기능

- PDF 문서 분석 및 정보 추출
- 기업 프로필 관리
- 잠재 고객 발굴 및 분석
- 기업명 활용 데이터 검색 및 HTML 보고서 제공

## 기술 스택

- Python 3.11
- Django 4.2
- Django REST Framework
- OpenAI GPT-4
- MySQL

## 설치 및 설정

### 1. 환경 설정

```bash
# 가상 환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
.\venv\Scripts\activate  # Windows

# 의존성 설치
pip install -r requirements.txt
```

### 2. 환경 변수 설정

`.env` 파일을 생성하고 다음 변수들을 설정합니다:

```env
SECRET_KEY=your-secret-key
OPENAI_API_KEY=your-openai-api-key
```

### 3. 데이터베이스 설정

```bash
python manage.py migrate
```

### 4. 서버 실행

```bash
python manage.py runserver
```

## API 문서

### 1. 회사 검색 및 보고서 응답

#### 보고서 작성 요청

```http
POST /api/lead/details/
Content-Type: application/json

{
    "search_company_name": "토스",
    "company_id": 12
}
```

응답:

```html
<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>비바리퍼블리카 기업 정보</title>
    <style>
        body {
            font-family: 'Noto Sans KR', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            display: flex;
            align-items: center;
            margin-bottom: 30px;
        }

        .logo {
            max-width: 100px;
            max-height: 100px;
            margin-right: 20px;
        }

        .company-title {
            flex-grow: 1;
        }

        .company-title h1 {
            margin-bottom: 5px;
        }

        .lead-score {
            background-color: #2c3e50;
            color: white;
            padding: 15px;
            border-radius: 5px;
            text-align: center;
        }

        .lead-score h2 {
            margin: 0;
            font-size: 24px;
        }

        .lead-score p {
            margin: 5px 0 0;
            font-size: 36px;
            font-weight: bold;
        }

        .section {
            margin-bottom: 30px;
            border: 1px solid #e1e1e1;
            border-radius: 5px;
            padding: 20px;
        }

        .section h2 {
            margin-top: 0;
            padding-bottom: 10px;
            border-bottom: 1px solid #e1e1e1;
        }

        .info-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }

        .info-item {
            margin-bottom: 15px;
        }

        .info-item h3 {
            margin-bottom: 5px;
            color: #555;
            font-size: 16px;
        }

        .info-item p {
            margin: 0;
            font-size: 18px;
        }

        .news-item {
            margin-bottom: 10px;
            padding-bottom: 10px;
            border-bottom: 1px dashed #e1e1e1;
        }

        .news-item:last-child {
            border-bottom: none;
        }

        .risk {
            background-color: #ffecec;
            padding: 15px;
            border-radius: 5px;
            border-left: 5px solid #ff8a8a;
        }
    </style>
</head>

<body>
<div class="header">

    <div class="company-title">
        <h1>비바리퍼블리카 리포트</h1>
        <p>핀테크, 금융, 송금, 결제, 투자, 보험</p>
    </div>
    <div class="lead-score">
        <h2>리드 점수</h2>
        <p>8</p>
    </div>
</div>

<div class="section">
    <h2>1. 기본 정보</h2>
    <div class="info-grid">
        <div class="info-item">
            <h3>회사명</h3>
            <p>비바리퍼블리카</p>
        </div>
        <div class="info-item">
            <h3>주요 산업 키워드</h3>
            <p>핀테크, 금융, 송금, 결제, 투자, 보험</p>
        </div>
        <div class="info-item">
            <h3>홈페이지</h3>
            <p><a href="https://toss.im/" target="_blank">https://toss.im/</a></p>
        </div>
        <div class="info-item">
            <h3>회사 주소/위치</h3>
            <p>정보 없음</p>
        </div>
        <div class="info-item">
            <h3>대표자/주요 인물</h3>
            <p>이승건 대표이사</p>
        </div>
        <div class="info-item">
            <h3>설립일</h3>
            <p>2013년 4월 23일</p>
        </div>
    </div>
</div>

<div class="section">
    <h2>2. 사업 개요</h2>
    <div class="info-item">
        <h3>기업 요약</h3>
        <p>토스는 비바리퍼블리카가 운영하는 모바일 금융 서비스로, 간편 송금, 결제, 대출 중개, 광고 등 다양한 금융 서비스를 제공하며, 2024년 3분기 기준 월간 활성 이용자 수(MAU)는
            1,910만 명에 달합니다.</p>
    </div>
    <div class="info-item">
        <h3>타겟 고객군</h3>
        <p>일반 소비자, 중소기업, 대기업, 금융기관</p>
    </div>
</div>

<div class="section">
    <h2>3. 핵심 영업 참고 정보</h2>
    <div class="info-grid">
        <div class="info-item">
            <h3>재무 정보</h3>
            <p>2024년 3분기 연결 영업수익 5,021억 원, 연결 영업이익 109억 원, 연결 당기순이익 39억 원, 2024년 3분기 누적 영업수익 1조 4,163억 원</p>
        </div>
        <div class="info-item">
            <h3>최신 동향</h3>
            <p>2024년 3분기 기준 분기 최대 실적을 달성하며, 광고, 간편결제, 대출 중개 등 컨슈머 서비스 전반의 고른 성장을 보이고 있습니다.</p>
        </div>
        <div class="info-item">
            <h3>경쟁사</h3>
            <p>카카오페이, 핀다</p>
        </div>
        <div class="info-item">
            <h3>강점 및 차별점</h3>
            <p>사용자 중심의 간편한 인터페이스, 혁신적인 기술 도입, 강력한 마케팅 전략, 종합 금융 플랫폼으로의 확장성</p>
        </div>
    </div>
    <div class="info-item risk">
        <h3>리스크 요인</h3>
        <p>경쟁 심화, 신뢰 구축, 서비스 다양화, 규제 대응</p>
    </div>
</div>

<div class="section">
    <h2>4. 뉴스 링크</h2>


    <div class="news-item">
        <a href="https://www.hankookilbo.com/News/Read/A2023122015480004853" target="_blank">토스, 월 광고 매출 100억 돌파</a>
        <p>2023-12-21 | 한국일보</p>
    </div>

    <div class="news-item">
        <a href="https://news.tf.co.kr/read/economy/2073280.htm" target="_blank">토스, IPO 본격 시동…대표 주관사로 한투·미래에셋
            선정</a>
        <p>2024-02-02 | 더팩트</p>
    </div>

    <div class="news-item">
        <a href="https://www.hankookilbo.com/News/Read/A2024102410300005526" target="_blank">토스인사이트 새 대표에 손병두 전 거래소
            이사장</a>
        <p>2024-10-24 | 한국일보</p>
    </div>


</div>
</body>

</html>
```

### 2. PDF 분석

#### PDF 분석 요청

```http
POST /api/analyze-pdf/
Content-Type: application/json

{
    "profile_id": 1
}
```

응답:

```json
{
  "status": "success",
  "message": "PDF analysis completed successfully",
  "analysis": {
    "industry": "소프트웨어",
    "sales": null,
    "total_funding": null,
    "homepage": null,
    "key_executive": "권태욱 대표이사",
    "address": null,
    "email": "david@goodai.kr",
    "phone_number": "010-8536-2267",
    "company_description": "더선한 주식회사는 AI 기반의 세일즈 인텔리전스 소프트웨어를 개발하여 B2B 세일즈 효율성을 극대화하는 솔루션을 제공합니다. 주요 기술로는 AI 에이전트, 자연어 처리, 데이터 레이크 구축 등이 있으며, 이를 통해 잠재고객 추천 및 거래 성사율을 높이는 데 주력하고 있습니다.",
    "products_services": "AI 기반 세일즈 인텔리전스 소프트웨어, 잠재고객 추천 알고리즘, 데이터 레이크 구축",
    "target_customers": "B2B 기업, 세일즈 팀, 마케팅 팀",
    "competitors": "줌인포, 링크드인, 마이크로소프트",
    "strengths": "AI 기반 기술, 세일즈 효율성 극대화, 잠재고객 추천",
    "business_model": "AI 기술을 활용하여 B2B 세일즈 프로세스를 자동화하고, 잠재고객 추천 및 거래 성사율을 높이는 소프트웨어 솔루션을 제공합니다."
  }
}
```

#### PDF 분석 결과 조회

```http
GET /api/analyze-pdf/{profile_id}
```

응답:

```json
{
  "status": "success",
  "analysis": {
    "industry": "소프트웨어",
    "sales": null,
    "total_funding": null,
    "homepage": null,
    "key_executive": "권태욱 대표이사",
    "address": null,
    "email": "david@goodai.kr",
    "phone_number": "010-8536-2267",
    "company_description": "더선한 주식회사는 AI 기반의 세일즈 인텔리전스 소프트웨어를 개발하여 B2B 세일즈 효율성을 극대화하는 솔루션을 제공합니다. 주요 기술로는 AI 에이전트, 자연어 처리, 데이터 레이크 구축 등이 있으며, 이를 통해 잠재고객 추천 및 거래 성사율을 높이는 데 주력하고 있습니다.",
    "products_services": "AI 기반 세일즈 인텔리전스 소프트웨어, 잠재고객 추천 알고리즘, 데이터 레이크 구축",
    "target_customers": "B2B 기업, 세일즈 팀, 마케팅 팀",
    "competitors": "줌인포, 링크드인, 마이크로소프트",
    "strengths": "AI 기반 기술, 세일즈 효율성 극대화, 잠재고객 추천",
    "business_model": "AI 기술을 활용하여 B2B 세일즈 프로세스를 자동화하고, 잠재고객 추천 및 거래 성사율을 높이는 소프트웨어 솔루션을 제공합니다.",
    "created_at": "2025-04-15T10:25:10.581634Z",
    "updated_at": "2025-04-15T10:25:10.581710Z"
  }
}
```

### 3. 잠재 고객 발굴

#### 잠재 고객 검색

```http
POST /api/find-leads/
Content-Type: application/json

{
    "company_id": 1
}
```

응답:

```json
{
  "status": "success",
  "message": "Found 5 potential leads",
  "source_used": "pdf_analysis",
  "leads": [
    {
      "company": "삼성전자",
      "industry": "전자제품 제조",
      "sales": 230000000000.0,
      "total_funding": 0.0,
      "homepage": "https://www.samsung.com/",
      "key_executive": "이재용",
      "relevance_score": 0.85,
      "reasoning": "삼성전자는 다양한 B2B 제품과 서비스를 제공하며, 대규모 세일즈 팀을 운영하고 있습니다. 더선한 주식회사의 AI 기반 세일즈 인텔리전스 소프트웨어를 활용하여 세일즈 리드 추천 및 거래 성사율을 높일 수 있습니다. 또한, 삼성전자의 글로벌 네트워크를 통해 더선한 주식회사의 솔루션을 해외 시장에 확장할 수 있는 기회도 있습니다."
    }
    // 총 5개 리드 출력
  ]
}
```

## DB

![image](https://github.com/user-attachments/assets/83de8dfa-036b-4bfd-b910-daeb4e259c15)

## Prompt

### 1. PDF 요약 Prompt

```
            당신은 회사 분석 전문가입니다. 아래 제공된 PDF에서 추출한 텍스트를 분석하여 "{company_name}" 회사에 대한 상세 정보를 추출해주세요.

            다음 정보들을 최대한 정확하게 찾아 JSON 형식으로 반환해주세요:
            
            # 기본 회사 정보
            - industry: 회사의 산업 분야 (예: "소프트웨어", "제조업" 등)
            - sales: 연간 매출액 (숫자만, 단위 없이)
            - total_funding: 총 투자 유치 금액 (숫자만, 단위 없이)
            - homepage: 회사 홈페이지 URL
            - key_executive: 주요 경영진 (CEO 등)
            - address: 회사 주소
            - email: 연락 이메일
            - phone_number: 연락처
            
            # 상세 정보
            - company_description: 회사 설명 및 핵심 사업 분야 (500자 이내)
            - products_services: 주요 제품 및 서비스 (쉼표로 구분된 목록)
            - target_customers: 주요 타겟 고객층 (쉼표로 구분된 목록)
            - competitors: 주요 경쟁사 (쉼표로 구분된 목록)
            - strengths: 회사의 강점 (쉼표로 구분된 목록)
            - business_model: 비즈니스 모델 설명 (300자 이내)

            텍스트에서 명확하게 확인할 수 없는 정보는 null로 표시하거나 생략하세요. 
            특히 매출액이나 투자금액은 확실한 숫자만 포함하고 추측하지 마세요.

            분석할 PDF 텍스트:
            {text}

            JSON 형식으로만 응답해주세요. 다른 텍스트나 설명은 포함하지 마세요.
```

### 2. Lead 탐색 Prompt

```
        당신은 B2B 영업 리드 스카우트 전문가입니다. 
        아래 회사 정보를 기반으로 이 회사에 제품이나 서비스를 판매하기에 적합한 잠재적인 영업 타겟이 될 수 있는 회사 5개를 찾아주세요.

        소스 회사 정보:
        - 회사명: {company_data.company}
        - 산업: {company_data.industry or "정보 없음"}
        - 매출: {company_data.sales or "정보 없음"}
        - 총 펀딩: {company_data.total_funding or "정보 없음"}
        - 홈페이지: {company_data.homepage or "정보 없음"}
        - 주요 경영진: {company_data.key_executive or "정보 없음"}
        - 주소: {company_data.address or "정보 없음"}
        - 이메일: {company_data.email or "정보 없음"}
        - 연락처: {company_data.phone_number or "정보 없음"}

        {additional_info}
        웹 검색을 통해 소스 회사에 대한 추가 정보를 확인하고, 다음과 같은 기준으로 잠재적 리드 대상 회사를 찾아주세요:

        1. 산업 시너지: 소스 회사와 상호보완적인 산업 또는 동일 산업 내에서 협력 가능성이 있는 회사, 산업군은 NCS 기준으로 경쟁업체이면 배제
        2. 비즈니스 모델 적합성: 소스 회사의 제품/서비스를 활용하여 비즈니스를 개선할 수 있는 회사
        3. 성장 단계 적합성: 소스 회사의 솔루션을 필요로 할 가능성이 높은 성장 단계에 있는 회사
        4. 잠재적 파트너십 가능성: 전략적 제휴나 협업을 통해 상호 이익을 얻을 수 있는 회사
        5. 시장 접근성: 비즈니스 네트워크상 소스 회사가 접근하기 좋은 회사
        6. 장소: 국가는 대한민국, 지역은 소스 회사와 가까울수록 선호
        7. 직원수, 매출, 순이익: 많을수록 선호
        8. 당면 문제: 소스 회사가 해결하는 문제와 유사할수록 선호

        리드 대상 회사의 관련성 점수(relevance_score)는 다음 항목 기준 가중치를 적용하여 산출해주세요:
        
        | 항목 | 기준 | 가중치(%) | 설명 |
        |------|------|-----------|------|
        | 산업군 적합성 | 코어 타깃 산업군 포함 여부 | 30% | 예: IT, 제조, 환경 분야 등 |
        | 매출 규모 | 최근 매출 규모 | 20% | 일정 매출 이상일수록 가산점 |
        | 성장성 | 최근 3년 평균 성장률 | 20% | 고성장 기업에 가산점 |
        | 지역성 | 특정 지역(예: 수도권, 해외시장) 여부 | 10% | 전략 지역 포함 시 추가 점수 |
        | 뉴스/이슈 노출 | 최근 1년 내 긍정 뉴스 기사 수 | 10% | 긍정적 이슈 많은 기업 우대 |
        | 비즈니스 적합성 | 소스 회사 제품/서비스 활용 가능성 | 10% | 활용 시나리오가 명확할수록 가산점 |
        
        응답은 다음 JSON 형식으로 제공해주세요:
        {{
            "leads": [
                {{
                    "company": "회사명",
                    "industry": "산업",
                    "sales": 매출액(숫자),
                    "total_funding": 총 펀딩 금액(숫자),
                    "homepage": "웹사이트 URL", 
                    "key_executive": "주요 경영진",
                    "address": "회사 주소",
                    "email": "연락 이메일",
                    "phone_number": "연락처",
                    "relevance_score": 0.0~1.0 사이의 관련성 점수,
                    "reasoning": "이 회사가 소스 회사에게 좋은 영업 타겟인 이유를 구체적으로 설명 (산업 시너지, 비즈니스 모델 적합성 등을 기반으로)"
                }},
                ...
            ]
        }}

        중요: 
        1. 실제로 확인된 정보만 포함하세요. 
        2. 홈페이지 URL은 반드시 실제 존재하는 URL만 제공하고, 확실하지 않은 경우 빈 문자열("")로 남겨두세요.
        3. 단순히 회사명을 기반으로 URL을 추측하지 마세요.
        4. 웹 검색을 통해 확인된 정보만 포함하세요.
        5. 추천하는 회사가 실제로 소스 회사의 제품/서비스로 혜택을 얻을 수 있는지, 구체적인 협업 가능성이 있는지 명확히 설명하세요.
```

## 시스템 아키텍처

### 1. 데이터 흐름

1. 기업 프로필 생성(api x)
2. PDF/웹사이트 데이터 수집
3. AI 기반 정보 분석
4. 잠재 고객 식별
5. 결과 저장 및 반환

### 2. 주요 컴포넌트

- **CompanyProfile**: 기업 프로필 관리
- **PDFAnalysis**: PDF 문서 분석 결과 저장
- **LeadScoutAgent**: 잠재 고객 발굴 로직
- **PDFAnalysisService**: PDF 분석 서비스

## 작동 로직

### 1. PDF 분석 프로세스

1. PDF URL에서 문서 다운로드
2. 텍스트 추출
3. OpenAI를 통한 정보 분석
4. 분석 결과 DB 저장
5. 결과 반환

### 2. 잠재 고객 발굴 프로세스

1. 기업 프로필 조회
2. 관련 PDF 문서 분석
3. AI 기반 잠재 고객 식별
4. 결과 정제 및 저장
5. 응답 생성
