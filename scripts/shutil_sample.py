#sample1
import shutil

shutil.copy('sample_dir1/aaa.txt', 'sample_dir1/sample_dir2/xxx.txt')

#sample2
import glob
import shutil

shutil.copy('sample_dir1/sample_dir2', 'sample_dir1/sample_dir3')
print(glob.glob('sample_dir1/sample_dir3/*'))