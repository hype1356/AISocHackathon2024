from sentence_transformers import SentenceTransformer
import numpy as np

filename = input("Filename: ")
file_input = open(filename,'r')
sentences = []

for l in file_input:
  sentences.append(l)

model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')
embeddings = model.encode(sentences)

np.save(filename + '_embeddings', embeddings)
print("Saved as " + filename + "_embeddings")