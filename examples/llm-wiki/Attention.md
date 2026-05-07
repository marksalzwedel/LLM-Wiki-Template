# Attention

## Summary

Attention is a mechanism that lets a model weight one part of an input or generated sequence against other parts when computing a representation.

## Explanation

In [[Attention Is All You Need]], attention moves from an auxiliary sequence-to-sequence component into the center of the model. [[Self-Attention]] lets each token attend to other tokens in the same sequence, while cross-attention lets decoder tokens attend to encoder outputs.

## Related Links

- [[Self-Attention]]
- [[Scaled Dot-Product Attention]]
- [[Multi-Head Attention]]
- [[Transformer Architecture]]
- [[Encoder-Decoder Architecture]]

## Source Papers

- [[Attention Is All You Need]]
- [[BERT]]
- [[Language Models are Few-Shot Learners]]

## Contradictions and Tensions

- The papers agree that attention-based models are powerful. The main tension is architectural specialization: [[BERT]] uses attention bidirectionally in an encoder, while [[GPT-3]] uses causal attention for next-token prediction.
