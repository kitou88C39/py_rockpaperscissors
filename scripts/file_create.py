import as
import pathlib

os.makedirs('sample_dir/sample_dir2', exist_ok=True)

chrs = ['a','b','c','d']

for ch in chrs:
    pathlib.Path(f'sample_dir/{ch * 3}.txt').touch()

pathlib.Path('sample_dir/sample.txt').touch()
p.touch()

with p.open(mode='w') as f:
    f.write('Good Morining')

with p.open(mode='w') as f:
    print(f.read())