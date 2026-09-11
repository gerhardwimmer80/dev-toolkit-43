import os
import shutil
from typing import List, Union
from pathlib import Path

def sanitize_path(path: Union[str, Path]) -> Path:
    return Path(path).resolve()

class FileOrchestrator:
    def __init__(self, root: str = '.'):
        self.root = sanitize_path(root)

    def purge_directory(self, target: str, extensions: List[str] = None) -> int:
        target_path = self.root / target
        if not target_path.exists():
            return 0

        count = 0
        for item in target_path.iterdir():
            if extensions and item.suffix not in extensions:
                continue
            
            if item.is_file():
                item.unlink()
                count += 1
            elif item.is_dir():
                shutil.rmtree(item)
                count += 1
        return count

def safe_execute(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}

if __name__ == '__main__':
    orchestrator = FileOrchestrator()
    print(f'orchestrator active at {orchestrator.root}')