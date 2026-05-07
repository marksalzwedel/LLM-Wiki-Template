# Scaled Dot-Product Attention

## Summary

Scaled dot-product attention computes attention weights from query-key dot products, scales them by the key dimension, applies softmax, and uses the result to combine values.

## Explanation

The scaling factor in [[Attention Is All You Need]] prevents large dot products from pushing softmax into regions with tiny gradients. This small numerical adjustment helps make dot-product attention practical and efficient at Transformer dimensions.

## Related Links

- [[Attention]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Transformer Architecture]]

## Source Papers

- [[Attention Is All You Need]]

## Contradictions and Tensions

- The later papers rely on this attention family but do not dispute the scaled dot-product formulation. Their disagreements are about training objectives, adaptation, and deployment rather than this operation.
