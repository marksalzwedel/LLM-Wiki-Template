# Transformer Architecture

## Summary

The Transformer is a neural sequence architecture built around [[Self-Attention]], feed-forward layers, residual connections, normalization, and positional information.

## Explanation

[[Attention Is All You Need]] presents the Transformer as an alternative to recurrent and convolutional sequence models. Later papers reuse only parts of the original encoder-decoder design: [[BERT]] uses encoder-style bidirectional representations, while [[GPT-3]] and [[InstructGPT]] use autoregressive language-model variants.

## Related Links

- [[Attention]]
- [[Self-Attention]]
- [[Scaled Dot-Product Attention]]
- [[Multi-Head Attention]]
- [[Positional Encoding]]
- [[Encoder-Decoder Architecture]]
- [[Foundation Models]]

## Source Papers

- [[Attention Is All You Need]]
- [[BERT]]
- [[Language Models are Few-Shot Learners]]
- [[On the Opportunities and Risks of Foundation Models]]
- [[Training Language Models to Follow Instructions with Human Feedback]]

## Contradictions and Tensions

- No later paper in this set rejects the Transformer. The tension is scope: the original paper foregrounds architecture, while the foundation-model report treats architecture as one piece of a larger stack involving data, scale, adaptation, evaluation, and governance.
