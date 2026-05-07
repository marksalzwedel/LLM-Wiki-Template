# Masked Language Modeling

## Summary

Masked language modeling trains a model to predict hidden tokens from their surrounding context.

## Explanation

In [[BERT]], a fraction of input tokens are selected for prediction. Some are replaced with a mask token, some with random tokens, and some are left unchanged. This forces the model to maintain contextual representations across the sequence and enables [[Bidirectional Representations]].

## Related Links

- [[BERT]]
- [[Bidirectional Representations]]
- [[Self-Supervised Learning]]
- [[Pre-training]]
- [[Fine-Tuning]]

## Source Papers

- [[BERT]]
- [[On the Opportunities and Risks of Foundation Models]]

## Contradictions and Tensions

- [[GPT-3]] does not use masked language modeling; it uses [[Autoregressive Language Modeling]]. The papers differ on whether the goal is best framed as representation learning for fine-tuned tasks or generative task completion from a prompt.
