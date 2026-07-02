import pandas as pd


def save_results(results):

    submission_rows = []

    for rank, r in enumerate(results[:100], start=1):

        submission_rows.append({

            "candidate_id":
            r["candidate_id"],

            "rank":
            rank,

            "score":
            r["final_score"],

            "reasoning":
            r["reason"]

        })

    df = pd.DataFrame(submission_rows)

    df.to_csv(
        "output/submission.csv",
        index=False
    )

    print("\nSubmission CSV saved!")