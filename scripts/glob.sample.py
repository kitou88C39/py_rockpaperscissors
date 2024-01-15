#sample1
import glob

print(glob.glob('sample_dir/*'))
print(glob.glob('sample_dir/*.txt'))

#sample2
import glob

print(glob.glob('sample_dir/**/*.txt', recursive=True))