from leadscout_sdk.utils.db_connection import get_db_connection

def create_company_profile(company_name: str, industry: str, homepage: str) -> dict:
    """
    기업 프로필을 생성하는 함수
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO scout_agent_companyprofile (company_name, industry, homepage)
    VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (company_name, industry, homepage))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Company profile created successfully."}


def get_all_company_profiles() -> list:
    """
    모든 기업 프로필을 조회하는 함수
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "SELECT id, company_name, industry, homepage FROM scout_agent_companyprofile"
    cursor.execute(sql)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    profiles = []
    for row in rows:
        profiles.append({
            "id": row[0],
            "company_name": row[1],
            "industry": row[2],
            "homepage": row[3]
        })

    return profiles
