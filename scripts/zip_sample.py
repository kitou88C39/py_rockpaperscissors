#zipfileの作成とすでに存在するzipfileのへのファイルの追加
import zipfile
import glob

with zipfile.ZipFile('sample_dir1/sample_zip.zip', 'w')as zf:
    for f in glob.glob('sample_dir1/*.txt'):
        zf.write(f)

#zipfileの解凍
import zipfile

with zipfile.ZipFile('sample_dir1/sample_zip.zip', 'w')as zf:
    zf.extractall('sample_dir1/*.txt'):
    


