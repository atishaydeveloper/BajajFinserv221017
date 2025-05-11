#!/usr/bin/env python3
import requests
import sys

# ───── CONFIGURATION ───────────────────────────────────────────────────────────
WEBHOOK_URL = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"
TOKEN       = "eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IjA4MjdDRDIyMTAxNyIsIm5hbWUiOiJBdGlzaGF5IEphaW4iLCJlbWFpbCI6ImF0aXNoeWphaW4yMjA3NTFAYWNyb3BvbGlzLmluIiwic3ViIjoid2ViaG9vay11c2VyIiwiaWF0IjoxNzQ2OTU5OTA5LCJleHAiOjE3NDY5NjA4MDl9.Ol0GCSSYs1bCuEuA-uhJZTYZkvizdyOit7e2LJeHflA"

# ───── YOUR FINAL SQL ─────────────────────────────────────────────────────────
FINAL_SQL = """
SELECT 
    E1.EMP_ID,
    E1.FIRST_NAME,
    E1.LAST_NAME,
    D.DEPARTMENT_NAME,
    COUNT(E2.EMP_ID) AS YOUNGER_EMPLOYEES_COUNT
FROM 
    EMPLOYEE E1
JOIN 
    DEPARTMENT D ON E1.DEPARTMENT = D.DEPARTMENT_ID
LEFT JOIN 
    EMPLOYEE E2 ON E1.DEPARTMENT = E2.DEPARTMENT
               AND E2.DOB > E1.DOB
GROUP BY 
    E1.EMP_ID, E1.FIRST_NAME, E1.LAST_NAME, D.DEPARTMENT_NAME
ORDER BY 
    E1.EMP_ID DESC;

"""

def submit_solution(webhook_url: str, token: str, sql: str):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    payload = {"finalQuery": sql}
    r = requests.post(webhook_url, json=payload, headers=headers)
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    try:
        print("Submitting your SQL solution...")
        result = submit_solution(WEBHOOK_URL, TOKEN, FINAL_SQL)
        print("✅ Submission response:")
        print(result)
    except Exception as e:
        print("❌ Submission failed:", e, file=sys.stderr)
        sys.exit(1)
    print("Please check your webhook URL and token.")