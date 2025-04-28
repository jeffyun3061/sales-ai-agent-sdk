from leadscout_sdk.scout_agent.company_profile import create_company_profile

if __name__ == "__main__":
    result = create_company_profile(
        company_name="테스트 회사",
        industry="IT 서비스",
        homepage="http://test-company.com"
    )
    print(result)
