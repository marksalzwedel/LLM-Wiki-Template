# Bidirectional Representations

## Summary

Bidirectional representations condition on both left and right context, letting each token representation use information from surrounding text.

## Explanation

[[BERT]] is designed around deep bidirectional pre-training. Its [[Masked Language Modeling]] objective avoids the left-to-right constraint by hiding selected tokens and asking the model to infer them from both sides.

## Related Links

- [[BERT]]
- [[Masked Language Modeling]]
- [[Self-Attention]]
- [[Autoregressive Language Modeling]]
- [[Fine-Tuning]]

## Source Papers

- [[BERT]]
- [[Language Models are Few-Shot Learners]]

## Contradictions and Tensions

- [[BERT]] presents bidirectionality as important for language understanding. [[Language Models are Few-Shot Learners]] accepts that bidirectionality can help some tasks, but chooses autoregressive models because they are straightforward to sample from and evaluate as language models.
