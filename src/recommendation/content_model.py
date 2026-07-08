from sklearn.metrics.pairwise import cosine_similarity


class ContentModel:

    def __init__(self, embeddings):

        self.embeddings = embeddings

    def similarity(
        self,
        query_embedding,
        candidate_embeddings
    ):

        scores = cosine_similarity(
            query_embedding,
            candidate_embeddings
        )[0]

        return scores