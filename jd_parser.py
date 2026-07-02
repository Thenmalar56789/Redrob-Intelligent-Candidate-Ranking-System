class JDParser:

    def extract_required_skills(self, jd_text):

        jd_text = jd_text.lower()

        skills = []

        keywords = [
            "python",
            "machine learning",
            "ml",
            "llm",
            "rag",
            "embeddings",
            "nlp",
            "transformers",
            "elasticsearch",
            "bm25",
            "vector search",
            "milvus",
            "api",
            "docker",
            "kubernetes",
            "mlops"
        ]

        for keyword in keywords:
            if keyword in jd_text:
                skills.append(keyword)

        return skills