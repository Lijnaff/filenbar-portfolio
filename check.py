
import urllib.request, json

repo = "Lijnaff/filenbar-portfolio"

# Check pages config
req = urllib.request.Request(
    f"https://api.github.com/repos/{repo}/pages",
    headers={"Accept": "application/vnd.github+json"}
)
try:
    resp = urllib.request.urlopen(req)
    info = json.loads(resp.read())
    print(f"Status: {info.get('status')}")
    print(f"URL: {info.get('html_url')}")
    print(f"Source: {info.get('source')}")
except urllib.error.HTTPError as e:
    print(f"Pages error: {e.code}")

# Check if the branch exists and has the files
req2 = urllib.request.Request(
    f"https://api.github.com/repos/{repo}/branches/master",
    headers={"Accept": "application/vnd.github+json"}
)
try:
    resp2 = urllib.request.urlopen(req2)
    branch = json.loads(resp2.read())
    print(f"\nBranch: {branch.get('name')}")
    print(f"Commit: {branch.get('commit',{}).get('sha','')[:12]}")
except urllib.error.HTTPError as e:
    print(f"Branch error: {e.code}")

# Check recent commits
req3 = urllib.request.Request(
    f"https://api.github.com/repos/{repo}/commits?per_page=3",
    headers={"Accept": "application/vnd.github+json"}
)
try:
    resp3 = urllib.request.urlopen(req3)
    commits = json.loads(resp3.read())
    print(f"\nRecent commits:")
    for c in commits:
        print(f"  {c['sha'][:8]} - {c['commit']['message'][:50]}")
except urllib.error.HTTPError as e:
    print(f"Commits error: {e.code}")
