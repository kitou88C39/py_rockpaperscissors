#tarfile
# sample1
import tarfile

with tarfile.open('tar_sample.tar.gz','w:gz')as tr:
    tr.add('sample_dir1')

# sample2
import tarfile

with tarfile.open('tar_sample.tar.gz','r:gz')as tr:
    tr.extractall('tar_sample'):