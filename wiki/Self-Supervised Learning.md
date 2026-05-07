# Self-Supervised Learning

## Summary

Self-supervised learning creates training signals from raw data itself, such as predicting masked words or the next token.

## Explanation

[[BERT]] uses [[Masked Language Modeling]] and [[Next Sentence Prediction]] to learn from unlabeled text. [[GPT-3]] uses next-token prediction at much larger scale. [[On the Opportunities and Risks of Foundation Models]] treats self-supervision as a key ingredient that makes broad pre-training economically and technically feasible.

## Related Links

- [[Pre-training]]
- [[Masked Language Modeling]]
- [[Next Sentence Prediction]]
- [[Autoregressive Language Modeling]]
- [[Foundation Models]]

## Source Papers

- [[BERT]]
- [[Language Models are Few-Shot Learners]]
- [[On the Opportunities and Risks of Foundation Models]]

## Contradictions and Tensions

- Self-supervised objectives produce broad capabilities, but [[Training Language Models to Follow Instructions with Human Feedback]] argues they do not by themselves align outputs with user intent.
