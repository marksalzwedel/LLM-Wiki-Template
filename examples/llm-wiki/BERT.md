# BERT

## Summary

BERT, short for Bidirectional Encoder Representations from Transformers, is a [[Transformer Architecture]] model trained with [[Masked Language Modeling]] and [[Next Sentence Prediction]] so it can build [[Bidirectional Representations]] from unlabeled text.

Source file: [raw/1810.04805v2.pdf](../raw/1810.04805v2.pdf)

## Explanation

The paper argues that deep bidirectional pre-training produces strong reusable language representations. Instead of designing a custom architecture for every task, BERT adds a small task head and uses [[Fine-Tuning]] to adapt the same pre-trained encoder to classification, question answering, and sentence-pair tasks.

## Related Links

- [[Bidirectional Representations]]
- [[Masked Language Modeling]]
- [[Next Sentence Prediction]]
- [[Fine-Tuning]]
- [[Self-Supervised Learning]]
- [[Transformer Architecture]]
- [[Pre-training]]

## Contradictions and Tensions

- [[BERT]] argues that bidirectionality matters for language understanding, while [[Language Models are Few-Shot Learners]] shows that [[Autoregressive Language Modeling]] plus scale and prompts can solve many tasks without bidirectional conditioning.
- BERT treats [[Fine-Tuning]] as the standard downstream adaptation path. [[GPT-3]] instead evaluates tasks through [[Prompting]] and [[In-Context Learning]] without gradient updates.
- [[On the Opportunities and Risks of Foundation Models]] treats BERT as part of a broader foundation-model shift, adding risk and governance questions that are mostly outside BERT's benchmark-focused framing.
