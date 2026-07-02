# Redrob Intelligent Candidate Ranking System

## Overview

Redrob Intelligent Candidate Ranking System is a hybrid AI-powered candidate ranking pipeline designed to identify the most relevant candidates for a given job description from a large candidate pool.

The system combines structured candidate scoring with semantic similarity matching to produce explainable and recruiter-friendly rankings.

---

## Problem Statement

Given a job description and a large candidate dataset, rank the top 100 most suitable candidates based on:

- Technical skill alignment
- Behavioral signals
- Recruiter engagement
- Candidate availability
- Assessment performance
- Learning potential
- Adaptability
- Career transition capability
- Semantic relevance to the job description

---

## Architecture

### Stage 1: Candidate Retrieval & Scoring

The system computes candidate scores using:

- JD Skill Matching
- Learning Potential Scoring
- Behavioral Signal Scoring
- Recruiter Demand Scoring
- Availability Scoring
- Assessment Scoring
- Adaptability Scoring
- Career Transition Detection

### Stage 2: Semantic Reranking

Top candidates are reranked using semantic similarity.

Model Used:

- all-MiniLM-L6-v2
- Sentence Transformers
- Cosine Similarity

This stage captures contextual relevance beyond simple keyword matching.

### Stage 3: Final Ranking

Candidates are sorted by final score and the Top 100 candidates are selected for submission.

---

## Dataset

- 100,000 candidate profiles
- Candidate profile information
- Behavioral signals
- Recruiter engagement metrics
- Assessment and availability indicators

---

## Features

- Hybrid Rule-Based + Semantic Ranking
- Explainable Candidate Recommendations
- Career Transition Detection
- Recruiter Signal Analysis
- Large-Scale Candidate Processing
- Top-100 Candidate Selection
- Semantic Similarity Matching

---

## Output

The system generates:

### submission.csv

Columns:

- candidate_id
- rank
- score
- reasoning

### detailed_results.csv

Contains detailed scoring breakdown for analysis and explainability.

---

## Technology Stack

- Python
- Pandas
- Sentence Transformers
- Hugging Face Transformers
- NumPy

---

## Model

all-MiniLM-L6-v2

Used for semantic similarity matching between candidate profiles and job descriptions.

---

## Runtime

CPU-only execution.

Approximately 1 minute to process and rank 100,000 candidate profiles using the two-stage ranking pipeline.

---

## Future Improvements

- Learning-to-Rank Models
- LLM-generated Explanations
- Vector Database Integration
- Real-time Ranking API
- Recruiter Feedback Loop

## Single command in README

python ranker.py