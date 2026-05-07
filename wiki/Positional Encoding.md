# Positional Encoding

## Summary

Positional encoding injects token order into a Transformer, because self-attention alone is insensitive to sequence position.

## Explanation

[[Attention Is All You Need]] uses positional encodings so the model can distinguish the same words appearing in different orders. This is essential because [[Self-Attention]] compares all token positions directly rather than processing them one step at a time like a recurrent model.

## Related Links

- [[Transformer Architecture]]
- [[Self-Attention]]
- [[Attention Is All You Need]]

## Source Papers

- [[Attention Is All You Need]]
- [[BERT]]
- [[Language Models are Few-Shot Learners]]

## Contradictions and Tensions

- There is no direct contradiction in this paper set. Later models vary details of positional representation, but the shared need for order information remains.
