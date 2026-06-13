
import urllib.request, json, time

token = "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vcp_8NzfMmJeCiwA9x0nwwsxRrbD1W5lneELOPBpHDMTdn6pfslJk92U8ghw"

# Enable GitHub Pages
repo = "Lijnaff/filenbar-portfolio"
data = json.dumps({
    "source": {"branch": "master", "path": "/"}
}).encode()
req = urllib.request.Request(
    f"https://api.github.com/repos/{repo}/pages",
    data=data,
    method="POST",
    headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json"
    }
)
try:
    resp = urllib.request.urlopen(req)
    info = json.loads(resp.read())
    print(f"GitHub Pages enabled!")
    print(f"URL: {info.get('html_url')}")
except urllib.error.HTTPError as e:
    error_body = e.read().decode()
    print(f"Error {e.code}: {error_body}")
    if e.code == 422:
        print("Pages may already be enabled")
