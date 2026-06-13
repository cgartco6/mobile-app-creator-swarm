import os
import sys
from datetime import datetime

print("🚀 Builder Engine Swarm - Minimal Working Version")
print("Python version:", sys.version)

def main():
    app_name = "MyTestApp"
    output_dir = f"generated_{app_name.lower()}"
    
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Creating {app_name}...")
    
    os.makedirs(output_dir, exist_ok=True)
    
    with open(f"{output_dir}/README.md", "w", encoding="utf-8") as f:
        f.write(f"# {app_name}\n\nBuilt at {datetime.now()}\n\nIt finally fucking worked.\n")
    
    with open(f"{output_dir}/index.html", "w", encoding="utf-8") as f:
        f.write("""<html><head><title>Swarm Test</title></head><body>
<h1 style="color:green">✅ Builder Engine Swarm Works</h1>
<p>Open this file in browser.</p>
</body></html>""")
    
    print(f"✅ Done. Check folder: {output_dir}")
    print("Open index.html to see it.")

if __name__ == "__main__":
    main()
