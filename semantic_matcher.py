from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim


class SemanticMatcher:

    def __init__(self, jd_text):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.jd_embedding = self.model.encode(
            jd_text
        )

    def semantic_score(
        self,
        candidate_text
    ):

        candidate_embedding = self.model.encode(
            candidate_text
        )

        similarity = cos_sim(
            self.jd_embedding,
            candidate_embedding
        )

        return float(similarity) * 20