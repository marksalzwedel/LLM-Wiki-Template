# Encoder-Decoder Architecture

## Summary

An encoder-decoder architecture maps an input sequence into contextual representations and then decodes an output sequence from them.

## Explanation

[[Attention Is All You Need]] uses an encoder-decoder Transformer for machine translation. The encoder reads the source sentence; the decoder generates the target sentence while attending to encoder outputs. Later papers split this template apart: [[BERT]] is encoder-centered, while [[GPT-3]] and [[InstructGPT]] are decoder-style language models.

## Related Links

- [[Transformer Architecture]]
- [[Attention]]
- [[Self-Attention]]
- [[Bidirectional Representations]]
- [[Autoregressive Language Modeling]]

## Source Papers

- [[Attention Is All You Need]]
- [[BERT]]
- [[Language Models are Few-Shot Learners]]
- [[Training Language Models to Follow Instructions with Human Feedback]]

## Contradictions and Tensions

- The original Transformer is sequence-to-sequence. The later LLM papers show that encoder-only and decoder-only variants can become dominant for different purposes.
