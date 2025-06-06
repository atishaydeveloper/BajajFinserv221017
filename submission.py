#!/usr/bin/env python3
import requests
import sys


WEBHOOK_URL = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"
TOKEN       = "eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IjA4MjdDRDIyMTAxNyIsIm5hbWUiOiJBdGlzaGF5IEphaW4iLCJlbWFpbCI6ImF0aXNoYXlqYWluMjIwNzUxQGFjcm9wb2xpcy5pbiIsInN1YiI6IndlYmhvb2stdXNlciIsImlhdCI6MTc0Njk2NDA5MSwiZXhwIjoxNzQ2OTY0OTkxfQ.6wNgfNgAyWWAQeOBWUD5aC7etPhnBoSVciYrTSFkRFk"


FINAL_SQL = """
SELECT
    p.amount AS SALARY,
    CONCAT(e.first_name, ' ', e.last_name) AS NAME,
    TIMESTAMPDIFF(YEAR, e.dob, p.payment_time) AS AGE,
    d.department_name
FROM payments p
JOIN employee e ON p.emp_id = e.emp_id
JOIN department d ON e.department = d.department_id
WHERE EXTRACT(DAY FROM p.payment_time) <> 1
ORDER BY p.amount DESC
LIMIT 1;

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
