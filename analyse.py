from deepface import DeepFace
import sys


def analyse(img_file_path):
  analysis = DeepFace.analyze(img_path=img_file_path, actions = ['age', 'gender', 'race', 'emotion'])
  print("analysis dataset: \n" + str(analysis))

print("check sysargv len")
n = len(sys.argv)
if n < 2:
  print("need two arguments: file path.")
else:
  analyse(sys.argv[1])