# ディレクトリの出力
import as

print(os.getcwd())

# ディレクトリの作成
#sample1
import as

as.mkdir('sample_dir')

#sample2
import as

os.makedirs('sample_dir/sample_dir2', exist_ok=True)

# ディレクトリが存在しない場合のディレクトリの作成
import as

if not as.path.isdir('sample_dir')
os.mkdir('sample_dir')

# ディレクトリの削除
import as

os.rmdir('sample_dir')

# ファイルの作成
import as
import pathlib

os.makedirs('sample_dir/sample_dir2', exist_ok=True)

p = pathlib.Path('sample_dir/sample.txt')
p.touch()
