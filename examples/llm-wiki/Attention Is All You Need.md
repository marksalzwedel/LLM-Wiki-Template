# Attention Is All You Need

## Summary

This paper introduces the [[Transformer Architecture]], replacing recurrent and convolutional sequence models with stacked [[Self-Attention]] and feed-forward layers. Its core claim is architectural: attention mechanisms can model sequence transduction more efficiently and with better parallelism.

Source file: [raw/1706.03762v7.pdf](../raw/1706.03762v7.pdf)

## Explanation

The model uses an [[Encoder-Decoder Architecture]] for machine translation. It represents token relationships with [[Scaled Dot-Product Attention]], runs several attention heads in parallel through [[Multi-Head Attention]], and injects order information through [[Positional Encoding]]. The paper is the technical root for later systems such as [[BERT]], [[GPT-3]], [[Foundation Models]], and [[InstructGPT]].

## Related Links

- [[Transformer Architecture]]
- [[Attention]]
- [[Self-Attention]]
- [[Scaled Dot-Product Attention]]
- [[Multi-Head Attention]]
- [[Positional Encoding]]
- [[Encoder-Decoder Architecture]]

## Contradictions and Tensions

- Later papers do not reject the Transformer; they specialize it. [[BERT]] uses the encoder side, while [[GPT-3]] and [[Training Language Models to Follow Instructions with Human Feedback]] use autoregressive decoder-style language models.
- The title-level lesson can sound like architecture is the whole story. [[On the Opportunities and Risks of Foundation Models]] complicates that by emphasizing data, scale, systems, adaptation, safety, and social context.
