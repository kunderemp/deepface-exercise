from deepface import DeepFace
import sys


def verification(img_file_path, dataset_path):
  recognition = DeepFace.find(img_path=img_file_path, db_path = dataset_path)
  print("recognition dataset: \n" + str(recognition))

print("check sysargv len")
n = len(sys.argv)
if n < 3:
	print("need two arguments: file to be compared & directory path.")
else:
	verification(sys.argv[1], sys.argv[2])
#print("Let's verify")
#verification = DeepFace.verify(img1_path = "tests/dataset/img5.jpg", img2_path="tests/dataset/img5.jpg")
#print("verification dataset: \n" + str(verification))

#print("Let's recognize:")
#recognition = DeepFace.find(img_path="tests/dataset/img5.jpg", db_path = "tests/dataset/")

#print("recognition dataset: \n " + str(recognition))
