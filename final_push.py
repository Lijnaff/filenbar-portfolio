
import subprocess, os

base = r"C:\Users\Naff\portfolio"
os.chdir(base)

# Remove debug files that exist
debug_files = ["check_pages2.py", "check_photos.py", "check_status.py", 
    "enable_pages3.py", "push2.py", "push_instagram.py", "test_auth.py",
    "check.py", "check_vercel.py", "enable_pages.py", "enable_pages2.py",
    "find_gh.py", "pages_trigger.py", "test_token.py"]

for f in debug_files:
    fpath = os.path.join(base, f)
    if os.path.exists(fpath):
        subprocess.run(["git", "rm", "--cached", f], capture_output=True)
        os.remove(fpath)
        print(f"Removed: {f}")
    else:
        # Try to remove from git tracking even if file is gone
        subprocess.run(["git", "rm", "--cached", f], capture_output=True)

# Commit and push
subprocess.run(["git", "add", "."], capture_output=True)
result = subprocess.run(["git", "status", "--short"], capture_output=True, text=True)
print(f"Status: {result.stdout}")

subprocess.run(["git", "commit", "-m", "Clean up debug files"], capture_output=True)

token = "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vcp_8NzfMmJeCiwA9x0nwwsxRrbD1W5lneELOPBpHDMTdn6pfslJk92U8ghw"
auth_url = f"https://{token}@github.com/Lijnaff/filenbar-portfolio.git"
subprocess.run(["git", "remote", "set-url", "origin", auth_url], capture_output=True)
result = subprocess.run(["git", "push", "origin", "master"], capture_output=True, text=True, timeout=300)
print(f"Push: {result.stdout}\n{result.stderr}")

# Final state
result = subprocess.run(["git", "ls-files"], capture_output=True, text=True)
print(f"\nFinal repo files:")
for line in result.stdout.strip().split('\n'):
    print(f"  {line}")
