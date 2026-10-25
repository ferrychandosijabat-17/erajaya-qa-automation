import csv
import urllib.request
import json
import time
import sys
import os

URL = "https://demoqa.com/Account/v1/User"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(SCRIPT_DIR, "..", "data", "users.csv")

def register_user(username, password):
    payload = json.dumps({
        "userName": username,
        "password": password
    }).encode("utf-8")
    
    req = urllib.request.Request(
        URL,
        data=payload,
        headers={"Content-Type": "application/json"}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            print(f"[SUCCESS] Registered {username} (UserID: {data.get('userID')})")
            return True
    except urllib.error.HTTPError as e:
        error_msg = e.read().decode()
        if "User exists" in error_msg:
            print(f"[INFO] {username} already exists.")
            return True
        else:
            print(f"[FAIL] {username}: HTTP {e.code} - {error_msg}")
            return False
    except Exception as e:
        print(f"[ERROR] {username}: {str(e)}")
        return False

def main():
    print(f"Reading users from {CSV_PATH}...")
    success_count = 0
    total = 0
    with open(CSV_PATH, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += 1
            user = row["username"]
            pwd = row["password"]
            if register_user(user, pwd):
                success_count += 1
            time.sleep(0.5) # respectful rate limit to DemoQA server
    
    print(f"\nFinished: {success_count}/{total} users prepared.")

if __name__ == "__main__":
    main()
