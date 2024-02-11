from sentence_transformers import SentenceTransformer
import numpy as np

filename = input("Filename: ")
file_input = open(filename,'r', encoding="utf8")
sentences = []

for l in file_input:
  sentences.append(l)

model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2', device='cuda')
embeddings = model.encode(sentences, show_progress_bar=True)

np.save(filename + '_embeddings', embeddings)
print("Saved as " + filename + "_embeddings")