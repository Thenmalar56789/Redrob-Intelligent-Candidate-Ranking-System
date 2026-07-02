class Scorer:

    def jd_match_score(
        self,
        candidate_skills,
        required_skills
    ):

        matched_skills = []

        for skill in candidate_skills:

            if skill in required_skills:
                matched_skills.append(skill)

        score = len(matched_skills) * 5

        return min(score, 30), matched_skills

    def learning_score(self, candidate):

        score = 0

        certifications = candidate.get(
            "certifications",
            []
        )

        score += len(certifications) * 5

        advanced_count = 0

        for skill in candidate.get(
            "skills",
            []
        ):

            if skill.get(
                "proficiency"
            ) in [
                "advanced",
                "expert"
            ]:
                advanced_count += 1

        score += advanced_count * 3

        return min(score, 20)

    def behavior_score(self, signals):

        score = 0

        if signals.get(
            "open_to_work_flag"
        ):
            score += 5

        score += (
            signals.get(
                "interview_completion_rate",
                0
            ) * 10
        )

        score += (
            signals.get(
                "recruiter_response_rate",
                0
            ) * 10
        )

        return round(score, 2)

    def recruiter_demand_score(
        self,
        signals
    ):

        score = 0

        score += min(
            signals.get(
                "profile_views_received_30d",
                0
            ) / 10,
            5
        )

        score += min(
            signals.get(
                "saved_by_recruiters_30d",
                0
            ),
            5
        )

        score += min(
            signals.get(
                "search_appearance_30d",
                0
            ) / 20,
            5
        )

        return round(score, 2)

    def availability_score(
        self,
        signals
    ):

        score = 0

        if signals.get(
            "open_to_work_flag"
        ):
            score += 5

        score += (
            signals.get(
                "recruiter_response_rate",
                0
            ) * 5
        )

        notice = signals.get(
            "notice_period_days",
            180
        )

        if notice <= 30:
            score += 5

        elif notice <= 60:
            score += 3

        return round(score, 2)

    def assessment_score(
        self,
        signals
    ):

        assessments = signals.get(
            "skill_assessment_scores",
            {}
        )

        if not assessments:
            return 0

        avg_score = (
            sum(
                assessments.values()
            )
            / len(
                assessments
            )
        )

        return round(
            avg_score / 100 * 15,
            2
        )

    def adaptability_score(
        self,
        candidate
    ):

        score = 0

        summary = candidate[
            "profile"
        ].get(
            "summary",
            ""
        ).lower()

        keywords = [
            "learning",
            "transition",
            "building",
            "self-directed",
            "open to",
            "interested in"
        ]

        for word in keywords:

            if word in summary:
                score += 3

        return min(score, 20)

    def potential_score(
        self,
        candidate
    ):

        score = 0

        certifications = candidate.get(
            "certifications",
            []
        )

        score += len(
            certifications
        ) * 2

        github_score = candidate.get(
            "redrob_signals",
            {}
        ).get(
            "github_activity_score",
            0
        )

        if github_score > 70:
            score += 10

        elif github_score > 40:
            score += 5

        experience = candidate[
            "profile"
        ].get(
            "years_of_experience",
            0
        )

        if experience < 8:
            score += 5

        return min(score, 20)

    def transition_score(
        self,
        candidate
    ):

        score = 0

        education = candidate.get(
            "education",
            []
        )

        summary = candidate[
            "profile"
        ].get(
            "summary",
            ""
        ).lower()

        non_cs = [
            "biotechnology",
            "mechanical",
            "civil",
            "chemical",
            "electronics",
            "biology"
        ]

        transition_words = [
            "python",
            "software",
            "developer",
            "machine learning",
            "data science",
            "backend",
            "full stack",
            "ai"
        ]

        found_non_cs = False

        for edu in education:

            field = edu.get(
                "field_of_study",
                ""
            ).lower()

            for degree in non_cs:

                if degree in field:
                    found_non_cs = True

        if found_non_cs:

            for word in transition_words:

                if word in summary:
                    score += 3

        return min(score, 15)