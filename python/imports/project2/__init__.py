from pathlib import Path
import  sys

print(Path(__file__).parents[0])
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
print(sys.path)
