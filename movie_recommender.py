import pandas as pd
import numpy as np
from scipy.spatial import distance

metadata_path = './MovieLens/movies_metadata.csv'
feature_vectors_path = './movie_lens_overview_with_plots_mixed_distilbert_vecs.npy'


class MovieRecommender:
    def __init__(self):
        self.metadata = pd.read_csv(metadata_path,
                                    low_memory=False)
        self.movie_docs = pd.DataFrame(self.metadata[['original_title',
                                                      'overview',
                                                      'release_date',
                                                      'imdb_id',
                                                      'poster_path']])
        self.init_feature_vectors()

    def get_recommendations(self,
                            title,
                            recommend_k,
                            distance_metric='cosine'):
        df = self.movie_docs
        vector = df[df["original_title"] == title]["overview vectors"].iloc[0]
        shape = vector.shape[0]
        print("vector shape:" + str(shape))
        list_of_vecs = df["overview vectors"].tolist()

        similarities = []
        for b in list_of_vecs:
            try:
                dist = None
                if distance_metric == "cosine":
                    # cos_sim = dot(a, b)/(norm(a)*norm(b))
                    dist = np.dot(vector, b) / (np.linalg.norm(vector) * np.linalg.norm(b))
                elif distance_metric == "euclidian":
                    dist = distance.euclidean(vector, b)
                elif distance_metric == "dice":
                    dist = distance.dice(vector, b)
                elif distance_metric == "hamming":
                    dist = distance.hamming(vector, b)
                elif distance_metric == "sokalmichener":
                    dist = distance.sokalmichener(vector, b)
                elif distance_metric == "sqeuclidean":
                    dist = distance.sqeuclidean(vector, b)
                elif distance_metric == "chebyshev":
                    dist = distance.chebyshev(vector, b)
                similarities.append(dist)
            except:
                print("exception in similarity metric")
                pass
        indices = np.array(similarities).argsort()[1:recommend_k + 1][::-1]

        return [list(df.iloc[index].values[0:5]) for index in indices]

    def init_feature_vectors(self):
        with open(feature_vectors_path, 'rb') as f:
            word_vecs = np.load(f, allow_pickle=True)
        self.insert_movie_feature_vectors(word_vecs)

    def insert_movie_feature_vectors(self,
                                     word_vecs):
        list_word_vecs = []
        for i in range(len(word_vecs)):
            list_word_vecs.append(np.array(word_vecs[i]))
        len(list_word_vecs)
        self.movie_docs["overview vectors"] = list_word_vecs
