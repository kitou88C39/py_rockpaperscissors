#sample1
import zipfile
import glob

with zipfile.ZipFile('sample_dir1/sample_zip.zip', 'w')as zf:
    for f in glob.glob('sample_dir1/*.txt'):
        zf.write(f)