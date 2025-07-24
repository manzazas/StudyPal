import requests

BASE = "http://localhost:8000"  # ADK api_server

# def ensure_session(app_name: str, user_id: str, session_id: str):
#     url = f"{BASE}/apps/{app_name}/users/{user_id}/sessions/{session_id}"
#     r = requests.post(url, json={"state": {}})
#     # it's fine if it already exists
#     if r.status_code not in (200, 409):
#         r.raise_for_status()
def ensure_session(app_name, user_id, session_id):
    url = f"http://localhost:8000/apps/{app_name}/users/{user_id}/sessions/{session_id}"
    r = requests.post(url)

    if r.status_code == 400 and "already exists" in r.text:
        # Session already exists — continue without crashing
        print(f"Session '{session_id}' already exists. Continuing...")
    elif not r.ok:
        raise RuntimeError(f"Session create failed ({r.status_code}): {r.text}")


def run_turn(app_name: str, user_id: str, session_id: str, prompt: str):
    body = {
        "appName": app_name,
        "userId": user_id,
        "sessionId": session_id,
        "newMessage": {
            "role": "user",
            "parts": [{"text": prompt}]
        }
    }
    r = requests.post(f"{BASE}/run", json=body)
    r.raise_for_status()
    return r.json()
