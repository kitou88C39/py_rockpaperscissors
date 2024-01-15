#sample1
import shutil

shutil.copy('sample_dir1/aaa.txt', 'sample_dir1/sample_dir2/xxx.txt')

#sample2(コピー)
import glob
import shutil

shutil.copy('sample_dir1/sample_dir2', 'sample_dir1/sample_dir3')
print(glob.glob('sample_dir1/sample_dir3/*'))

#sample3(移動)
import glob
import shutil

shutil.move('sample_dir1/sample_dir2', 'sample_dir1/sample_dir3')
print(glob.glob('sample_dir1/sample_dir3/*'))

#sample4(削除)
import glob
import shutil

shutil.rmtree('sample_dir1/')