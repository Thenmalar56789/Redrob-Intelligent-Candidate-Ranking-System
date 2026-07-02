class FeatureExtractor:

    def extract_skills(self, candidate):
        return [
            skill["name"].lower()
            for skill in candidate.get("skills", [])
        ]

    def extract_summary(self, candidate):
        return candidate["profile"].get("summary", "").lower()

    def extract_career_text(self, candidate):
        text = ""

        for job in candidate.get("career_history", []):
            text += " " + job.get("description", "").lower()

        return text

    def extract_signals(self, candidate):
        return candidate.get("redrob_signals", {})