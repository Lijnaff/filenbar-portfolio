
import subprocess, os, time

base = r"C:\Users\Naff\portfolio"
os.chdir(base)

# Remove debug files
for f in ["check_state.py", "copy_new.py", "push_gallery.py", "restore.py", "restore_photo4.py", "serve.py", "check_pages.py", "final_push.py"]:
    fp = os.path.join(base, f)
    if os.path.exists(fp):
        subprocess.run(["git", "rm", "--cached", f], capture_output=True)
        os.remove(fp)
        print(f"Removed: {f}")

# Add gallery_4.jpg
subprocess.run(["git", "add", "gallery_4.jpg"], capture_output=True)
print("Added: gallery_4.jpg")

# Commit
subprocess.run(["git", "commit", "-m", "Add gallery_4.jpg and clean up debug files"], capture_output=True)

# Push
token = "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vcp_8NzfMmJeCiwA9x0nwwsxRrbD1W5lneELOPBpHDMTdn6pfslJk92U8ghw"
auth_url = f"https://{token}@github.com/Lijnaff/filenbar-portfolio.git"
subprocess.run(["git", "remote", "set-url", "origin", auth_url], capture_output=True)
result = subprocess.run(["git", "push", "origin", "master"], capture_output=True, text=True, timeout=300)
print(f"Push: {result.stdout}\n{result.stderr}")

# Verify
result = subprocess.run(["git", "ls-files"], capture_output=True, text=True)
print(f"\nFinal repo files:")
for line in result.stdout.strip().split('\n'):
    print(f"  {line}")
