# Self-Attention

## Summary

Self-attention computes relationships among tokens inside the same sequence, allowing each token representation to incorporate information from other positions.

## Explanation

In [[Attention Is All You Need]], self-attention replaces recurrent recurrence as the main way to move information across a sequence. It improves parallelism because token interactions can be computed with matrix operations. [[BERT]] uses unrestricted bidirectional self-attention, while [[GPT-3]] uses masked causal self-attention so the model cannot see future tokens during generation.

## Related Links

- [[Attention]]
- [[Scaled Dot-Product Attention]]
- [[Multi-Head Attention]]
- [[Bidirectional Representations]]
- [[Autoregressive Language Modeling]]
- [[Transformer Architecture]]

## Source Papers

- [[Attention Is All You Need]]
- [[BERT]]
- [[Language Models are Few-Shot Learners]]

## Contradictions and Tensions

- [[BERT]] and [[GPT-3]] use the same family of mechanism but impose different visibility rules. This creates a core tension between bidirectional understanding and left-to-right generation.
