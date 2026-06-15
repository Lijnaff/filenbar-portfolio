
import subprocess, os, time

base = r"C:\Users\Naff\portfolio"
os.chdir(base)

# Stop server
os.system('for /f "tokens=5" %a in (\'netstat -ano ^| findstr ":9090"\') do taskkill /F /PID %a 2>nul')
time.sleep(0.5)

# Remove debug files
for f in ["check_diff.py", "check_live.py", "check_live_imgs.py", "check_pages3.py", "check_state.py", "debug.py", "push_fix.py", "trigger_build.py", "wait_build.py"]:
    fp = os.path.join(base, f)
    if os.path.exists(fp):
        subprocess.run(["git", "rm", "--cached", f], capture_output=True)
        os.remove(fp)

# Commit everything
subprocess.run(["git", "add", "."], capture_output=True)
subprocess.run(["git", "commit", "-m", "Add gallery images 1-3 to slots and fix lightbox"], capture_output=True)

# Push
token = "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vcp_8NzfMmJeCiwA9x0nwwsxRrbD1W5lneELOPBpHDMTdn6pfslJk92U8ghw"
auth_url = f"https://{token}@github.com/Lijnaff/filenbar-portfolio.git"
subprocess.run(["git", "remote", "set-url", "origin", auth_url], capture_output=True)
result = subprocess.run(["git", "push", "origin", "master"], capture_output=True, text=True, timeout=600)
print(f"Push rc: {result.returncode}")
print(f"stdout: {result.stdout}")
print(f"stderr: {result.stderr}")

# Restart server
subprocess.Popen(['python3', '-m', 'http.server', '9090'], cwd=base,
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
print("Server restarted!")
