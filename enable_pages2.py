
import subprocess, json

# Try using gh api (since gh CLI is installed but not in PATH)
# First find gh binary
import os, glob

gh_path = None
for pattern in [
    r"C:\Users\Naff\AppData\Local\Programs\GitHub CLI\bin\gh.exe",
    r"C:\Users\Naff\AppData\Local\GitHub CLI\bin\gh.exe",
    r"C:\Program Files\GitHub CLI\bin\gh.exe",
]:
    matches = glob.glob(pattern)
    if matches:
        gh_path = matches[0]
        break

if gh_path:
    print(f"Found gh at: {gh_path}")
    # Try to enable pages
    result = subprocess.run(
        [gh_path, "api", f"repos/Lijnaff/filenbar-portfolio/pages", 
         "-X", "POST", "-f", "source[branch]=master", "-f", "source[path]=/"],
        capture_output=True, text=True, timeout=30
    )
    print(f"stdout: {result.stdout}")
    print(f"stderr: {result.stderr}")
else:
    print("gh CLI not found")
