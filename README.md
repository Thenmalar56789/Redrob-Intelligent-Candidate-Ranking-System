# Redrob Intelligent Candidate Ranking System

## Overview

This project ranks candidates for a given job description using a hybrid retrieval and ranking pipeline.

## Architecture

Stage 1:
- Rule-based candidate scoring
- JD skill matching
- Behavioral signals
- Recruiter engagement signals
- Availability scoring
- Learning potential scoring
- Career transition detection

Stage 2:
- Semantic reranking using Sentence Transformers
- Model: all-MiniLM-L6-v2

Stage 3:
- Top 100 candidate selection

## Dataset

- 100,000 candidate profiles
- Redrob behavioral signals
- Candidate profile schema

## Output

submission.csv

Columns:
- candidate_id
- rank
- score
- reasoning

## Runtime

CPU-only execution.

## Model

all-MiniLM-L6-v2