#tarfile
import tarfile

with tarfile.open('tar_sample.tar.gz','w:gz')as zf:
    zf.add('sample_dir1'):
    