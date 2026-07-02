import json
from semantic_matcher import SemanticMatcher
from reason_generator import ReasonGenerator
from output_writer import save_results
from feature_extractor import FeatureExtractor
from scoring import Scorer
from jd_parser import JDParser

extractor = FeatureExtractor()
scorer = Scorer()
reasoner = ReasonGenerator()


# Load JD
with open("data/jd.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()

semantic_matcher = SemanticMatcher(
    jd_text
)

parser = JDParser()
required_skills = parser.extract_required_skills(jd_text)

print("JD Skills:", required_skills)

# Load Candidates
import json

candidates = []

with open(
    "data/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for line in f:
        candidates.append(
            json.loads(line)
        )
print(
    "Total Candidates:",
    len(candidates)
)

results = []

for candidate in candidates:

    skills = extractor.extract_skills(candidate)
    signals = extractor.extract_signals(candidate)
    summary = extractor.extract_summary(
    candidate
)

    career_text = extractor.extract_career_text(
        candidate
    )

    candidate_text = (
        summary
        + " "
        + career_text
    )
    tech_score, matched_skills = scorer.jd_match_score(
    skills,
    required_skills

)
    learning_score = scorer.learning_score(candidate)
    behavior_score = scorer.behavior_score(signals)
    adaptability_score = scorer.adaptability_score(candidate)
    potential_score = scorer.potential_score(candidate)
    transition_score = scorer.transition_score(candidate)

    recruiter_score = scorer.recruiter_demand_score(signals)

    availability_score = scorer.availability_score(signals)

    assessment_score = scorer.assessment_score(signals)
    



    reason = reasoner.generate(
    tech_score,
    learning_score,
    behavior_score,
    adaptability_score,
    transition_score
)
    

    final_score = (
    tech_score
    + learning_score
    + behavior_score
    + recruiter_score
    + availability_score
    + assessment_score
    + adaptability_score
    + potential_score
    + transition_score
    
)
    
    results.append({
    "candidate_id": candidate["candidate_id"],

    "final_score": round(
        final_score,
        2
    ),

    "jd_score": tech_score,

    "learning_score": learning_score,

    "behavior_score": behavior_score,

    "recruiter_score": recruiter_score,

    "availability_score": availability_score,

    "assessment_score": assessment_score,

    "adaptability_score": adaptability_score,

    "potential_score": potential_score,

    "transition_score": transition_score,
    

    "reason": reason
})

results.sort(
    key=lambda x: x["final_score"],
    reverse=True
)
top_candidates = results[:1000]
candidate_lookup = {}

for candidate in candidates:
    candidate_lookup[
        candidate["candidate_id"]
    ] = candidate

for r in top_candidates:

    candidate = candidate_lookup[
        r["candidate_id"]
    ]

    summary = extractor.extract_summary(
        candidate
    )

    career_text = (
        extractor.extract_career_text(
            candidate
        )
    )

    candidate_text = (
        summary
        + " "
        + career_text
    )

    semantic_score = (
        semantic_matcher.semantic_score(
            candidate_text
        )
    )

    r["final_score"] += semantic_score
    
results.sort(
    key=lambda x: x["final_score"],
    reverse=True
)

print("\nTOP 100\n")

for r in results[:100]:

    print(
        r["candidate_id"],
        "->",
        r["final_score"]
    )

save_results(results)