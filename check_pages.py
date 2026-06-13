
import urllib.request, json

# Check if pages are enabled (no auth needed for public repos)
repo = "Lijnaff/filenbar-portfolio"
req = urllib.request.Request(
    f"https://api.github.com/repos/{repo}/pages",
    headers={"Accept": "application/vnd.github+json"}
)
try:
    resp = urllib.request.urlopen(req)
    info = json.loads(resp.read())
    print(f"Pages status: {info.get('status')}")
    print(f"Pages URL: {info.get('html_url')}")
    print(f"Source: {info.get('source')}")
except urllib.error.HTTPError as e:
    if e.code == 404:
        print("Pages not enabled yet")
    else:
        print(f"Error {e.code}")
