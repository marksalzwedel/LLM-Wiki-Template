# Multi-Head Attention

## Summary

Multi-head attention runs several attention projections in parallel so the model can attend to different relation types or positions at the same time.

## Explanation

[[Attention Is All You Need]] uses multiple heads to let the model jointly attend to information from different representation subspaces. This becomes a standard component of later [[Transformer Architecture]] systems, including [[BERT]], [[GPT-3]], and [[InstructGPT]].

## Related Links

- [[Attention]]
- [[Self-Attention]]
- [[Scaled Dot-Product Attention]]
- [[Transformer Architecture]]

## Source Papers

- [[Attention Is All You Need]]
- [[BERT]]
- [[Language Models are Few-Shot Learners]]
- [[Training Language Models to Follow Instructions with Human Feedback]]

## Contradictions and Tensions

- The papers do not contradict one another on the value of multi-head attention. The same mechanism supports different objectives: masked language modeling, next-token prediction, and instruction-following fine-tuning.
