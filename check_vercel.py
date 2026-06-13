
import subprocess, os, json, time

base = r"C:\Users\Naff\portfolio"

# Check if vercel CLI is available
result = subprocess.run(["where", "vercel"], capture_output=True, text=True)
print(f"vercel: {result.stdout.strip()}")

# Check npm global
result = subprocess.run(["npm", "list", "-g", "vercel"], capture_output=True, text=True)
print(f"npm vercel: {result.stdout.strip()}")

# Try npx
result = subprocess.run(["npx", "vercel", "--version"], capture_output=True, text=True, timeout=15)
print(f"npx vercel: {result.stdout.strip()}")
