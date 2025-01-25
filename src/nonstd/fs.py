from dataclasses import dataclass
import os
import shutil
from pathlib import Path
import json
from nonstd.data import List

@dataclass
class File:
    name: str
    parent: str
    full_path: str

def resolve(path: str) -> str:
    return Path(path).resolve().__str__()

def to_file(path: str):
    xs = path.split("/")
    return File(xs[-1], '/'.join(xs[:-1]), path)

def stat(path: str):
    return os.stat(Path(path))

def list_all(path: str):
	return (
		List(os.listdir(path))
		.map(lambda x: File(x, path, os.path.join(path, x)))
	)

def list_files(path: str):
	return (
		list_all(path)
		.filter(lambda x: os.path.isfile(x.full_path))
	)

def list_dirs(path: str):
	return (
		list_all(path)
		.filter(lambda x: os.path.isdir(x.full_path))
	)

def delete(path: str):
    if exists(path):
        os.remove(path)

def exists(path: str):
    p = Path(path)
    return p.exists()

def read_text(path: str):
    with open(path, 'r') as f:
        return f.read()

def write_text(path: str, data: str):
    ensure_parent(path)
    with open(path, 'w') as f:
        return f.write(data)

def append_text(path: str, data: str):
    ensure_parent(path)
    with open(path, 'a') as f:
        return f.write(data)

def read_json(path: str):
    return json.loads(read_text(path))

def get_parent(path: str):
    return Path(path).parent.__str__()

def ensure_parent(path: str):
    Path(path).parent.mkdir(parents=True, exist_ok=True)

def copy_file(src: str, dst: str):
    ensure_parent(dst)
    shutil.copyfile(src, dst)

def copy_tree(src: str, dst: str):
    ensure_parent(dst)
    shutil.copytree(src, dst, dirs_exist_ok=True)
