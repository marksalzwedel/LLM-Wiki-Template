# Pre-training

## Summary

Pre-training is the stage where a model learns general representations or capabilities from large data before being adapted or evaluated on downstream tasks.

## Explanation

[[BERT]] uses pre-training to learn bidirectional representations from unlabeled text, then applies [[Fine-Tuning]]. [[GPT-3]] uses large-scale autoregressive pre-training and then performs tasks through [[Prompting]] without gradient updates. [[Foundation Models]] generalize this pattern beyond NLP and emphasize that pre-training creates broad reuse.

## Related Links

- [[Self-Supervised Learning]]
- [[Masked Language Modeling]]
- [[Autoregressive Language Modeling]]
- [[Fine-Tuning]]
- [[Foundation Models]]
- [[Scaling Language Models]]

## Source Papers

- [[BERT]]
- [[Language Models are Few-Shot Learners]]
- [[On the Opportunities and Risks of Foundation Models]]
- [[Training Language Models to Follow Instructions with Human Feedback]]

## Contradictions and Tensions

- The papers agree that pre-training matters. They disagree on what should happen after pre-training: [[BERT]] fine-tunes, [[GPT-3]] prompts, and [[InstructGPT]] adds human-feedback alignment.
