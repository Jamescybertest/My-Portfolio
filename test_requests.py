import requests

def send_request(path="/", headers=None, data=""):
    url = f"http://localhost:8080{path}"
    try:
        response = requests.post(url, headers=headers, data=data)
        print(f"URL: {url}")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
        print("-" * 40)
    except Exception as e:
        print("Error:", e)

# 🚨 Test 1: Malicious request (should be BLOCKED)
malicious_headers = {
    "suffix": "%>//",
    "c1": "Runtime",
    "c2": "<%",
    "DNT": "1",
    "Content-Type": "application/x-www-form-urlencoded"
}
malicious_data = "This simulates a Spring4Shell exploit"
send_request(path="/tomcatwar.jsp", headers=malicious_headers, data=malicious_data)

# ✅ Test 2: Safe request (should be ALLOWED)
safe_headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "text/plain"
}
safe_data = "This is a normal request"
send_request(path="/normal", headers=safe_headers, data=safe_data)
