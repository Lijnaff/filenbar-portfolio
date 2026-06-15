
import subprocess, time
subprocess.Popen(['python3', '-m', 'http.server', '9090'], cwd=r"C:\Users\Naff\portfolio",
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
print("Server restarted on http://localhost:9090/")
