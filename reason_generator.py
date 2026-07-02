class ReasonGenerator:

    def generate(
        self,
        tech_score,
        learning_score,
        behavior_score,
        adaptability_score,
        transition_score
    ):

        reasons = []

        if tech_score >= 15:
            reasons.append(
                "Strong JD Match"
            )

        if learning_score >= 8:
            reasons.append(
                "High Learning Potential"
            )

        if behavior_score >= 15:
            reasons.append(
                "Strong Recruiter Signals"
            )

        if adaptability_score >= 3:
            reasons.append(
                "Adaptable Profile"
            )

        if transition_score >= 3:
            reasons.append(
                "Successful Career Transition"
            )

        if len(reasons) == 0:
            reasons.append(
                "Moderate Fit"
            )

        return ", ".join(reasons)