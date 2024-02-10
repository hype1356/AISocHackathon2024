from sentence_transformers import SentenceTransformer, util
import numpy as np
  
def get_context(query, filename, top_k=3):
  model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')
  file_input = open(filename, 'r')
  embeddings = np.load(filename + "_embeddings.npy")
  information = []

  for l in file_input:
    information.append(l)
  
  query_embedding = model.encode(query)
  cos_scores = util.cos_sim(query_embedding, embeddings)[0]

  top_results = np.argpartition(-cos_scores, range(top_k))[0:top_k]
  top_result_indices = top_results.tolist()

  context = [information[idx] for idx in top_result_indices] 
  return ' '.join(context)