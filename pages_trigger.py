
import subprocess, os, time

base = r"C:\Users\Naff\portfolio"
os.chdir(base)

# GitHub Pages for user/org sites uses the master branch directly
# The repo is Lijnaff/filenbar-portfolio which is a user repo
# For user repos, Pages serves from master branch root

# Let's check if there's a CNAME file or any config needed
# Actually for user Pages, the URL is Lijnaff.github.io/filenbar-portfolio
# and it serves from the master branch

# The issue might be that Pages needs to be enabled first
# Let me try pushing an empty commit to trigger the build

# First, create a simple .nojekyll file to bypass Jekyll processing
with open(os.path.join(base, ".nojekyll"), "w") as f:
    f.write("")

# Also create a _config.yml to disable Jekyll
with open(os.path.join(base, "_config.yml"), "w") as f:
    f.write("exclude:\n  - .nojekyll\n")

subprocess.run(["git", "add", "."], capture_output=True)
result = subprocess.run(["git", "status"], capture_output=True, text=True)
print(f"Status: {result.stdout}")

subprocess.run(["git", "commit", "-m", "Add .nojekyll for GitHub Pages"], capture_output=True)

# Push
token = "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vcp_8NzfMmJeCiwA9x0nwwsxRrbD1W5lneELOPBpHDMTdn6pfslJk92U8ghw"
auth_url = f"https://{token}@github.com/Lijnaff/filenbar-portfolio.git"
subprocess.run(["git", "remote", "set-url", "origin", auth_url], capture_output=True)

result = subprocess.run(["git", "push", "origin", "master"], capture_output=True, text=True, timeout=120)
print(f"Push: {result.stdout}\n{result.stderr}")
