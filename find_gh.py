
import subprocess, os

# Find gh.exe in Windows AppData
base = r"C:\Users\Naff\AppData\Local"
gh_path = None
for root, dirs, files in os.walk(base):
    if "gh.exe" in files:
        gh_path = os.path.join(root, "gh.exe")
        break
    # Don't go too deep
    if root.count(os.sep) > 5:
        dirs.clear()

if gh_path:
    print(f"Found: {gh_path}")
    result = subprocess.run([gh_path, "auth", "status"], capture_output=True, text=True, timeout=15)
    print(f"stdout: {result.stdout}")
    print(f"stderr: {result.stderr}")
else:
    print("gh.exe not found via walk, trying common paths...")
    candidates = [
        r"C:\Users\Naff\AppData\Local\GitHub CLI\bin\gh.exe",
        r"C:\Users\Naff\AppData\Local\Programs\GitHub CLI\bin\gh.exe",
        r"C:\Program Files\GitHub CLI\bin\gh.exe",
        r"C:\Users\Naff\AppData\Roaming\GitHub CLI\bin\gh.exe",
    ]
    for c in candidates:
        if os.path.exists(c):
            print(f"Found: {c}")
            result = subprocess.run([c, "--version"], capture_output=True, text=True, timeout=10)
            print(f"  version: {result.stdout}")
            break
        else:
            print(f"  not found: {c}")
