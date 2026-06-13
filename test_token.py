
import urllib.request, json

# Exact token from user
token = "ghp_HhLDXZvZyMLgIWcCAmpJ4eU0CTjipLzjRW6vcp_8NzfMmJeCiwA9x0nwwsxRrbD1W5lneELOPBpHDMTdn6pfslJk92U8ghw"

repo = "Lijnaff/filenbar-portfolio"

# Try to get user info
req = urllib.request.Request(
    "https://api.github.com/user",
    headers={"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
)
try:
    resp = urllib.request.urlopen(req)
    user = json.loads(resp.read())
    print(f"Logged in as: {user.get('login')}")
    print(f"Token scopes: {resp.headers.get('x-oauth-scopes', 'unknown')}")
except urllib.error.HTTPError as e:
    error_body = e.read().decode()
    print(f"User error {e.code}: {error_body}")
