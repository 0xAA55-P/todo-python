import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
    src_path = Path(__file__).parent / "src"
    subprocess.run([sys.executable, "main.py"], cwd=str(src_path), check=True)
        
