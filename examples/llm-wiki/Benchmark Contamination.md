# Benchmark Contamination

## Summary

Benchmark contamination occurs when evaluation examples or close variants appear in the training data, making reported performance less trustworthy.

## Explanation

[[Language Models are Few-Shot Learners]] studies contamination because large web-scale corpora can overlap with common NLP benchmarks. The issue becomes more important as [[Foundation Models]] train on broad data and are evaluated on many public datasets.

## Related Links

- [[Evaluation]]
- [[GPT-3]]
- [[Pre-training]]
- [[Foundation Models]]
- [[Scaling Language Models]]

## Source Papers

- [[Language Models are Few-Shot Learners]]
- [[On the Opportunities and Risks of Foundation Models]]

## Contradictions and Tensions

- GPT-3's broad training data enables few-shot generality, but the same breadth creates uncertainty about whether some benchmark success reflects generalization or memorized exposure.
