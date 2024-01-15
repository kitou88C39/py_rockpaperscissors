#tarfile
import tarfile

with tarfile.open('tar_sample.tar.gz','w:gz')as tr:
    tr.add('sample_dir1'):
    