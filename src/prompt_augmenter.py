from sentence_transformers import SentenceTransformer, util
import numpy as np
import webscraper
  
def get_context(query, filename, top_k=5):
  model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')
#   scrapedFromOnline = webscraper.scrapeInformation(query)
#   scrapedEmbeddings = model.encode(scrapedFromOnline)
  file_input = open(filename, 'r')
  embeddings = np.load(filename + "_embeddings.npy") # np.concatenate([np.load(filename + "_embeddings.npy"), scrapedEmbeddings], axis=1)
  #allContext = file_input + "\n" + scrapedFromOnline
  information = []

  for l in file_input:
    information.append(l)
  
  query_embedding = model.encode(query)
  cos_scores = util.cos_sim(query_embedding, embeddings)[0]

  top_results = np.argpartition(-cos_scores, range(top_k))[0:top_k]
  top_result_indices = top_results.tolist()
  context = [information[idx] for idx in top_result_indices] 
  return ' '.join(context)

  # similarities = np.dot(embeddings, query_embedding) 
  # top_n = 5  # Number of context pieces to retrieve

  # top_context_indices = np.argsort(similarities)[-top_n:]  # Indices of top matches

  # most_relevant_contexts = [information[idx] for idx in top_context_indices]

  # return ' '.join(most_relevant_contexts)
