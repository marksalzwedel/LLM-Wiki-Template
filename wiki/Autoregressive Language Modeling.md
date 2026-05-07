# Autoregressive Language Modeling

## Summary

Autoregressive language modeling trains a model to predict the next token from previous tokens.

## Explanation

[[GPT-3]] is an autoregressive model: it generates text left to right and can be sampled naturally. This makes it well suited to [[Prompting]], completions, and [[In-Context Learning]]. [[InstructGPT]] keeps this model family but changes the post-training process with [[Human Feedback]].

## Related Links

- [[GPT-3]]
- [[Prompting]]
- [[In-Context Learning]]
- [[Few-Shot Learning]]
- [[Bidirectional Representations]]
- [[Self-Supervised Learning]]

## Source Papers

- [[Language Models are Few-Shot Learners]]
- [[Training Language Models to Follow Instructions with Human Feedback]]
- [[BERT]]

## Contradictions and Tensions

- [[BERT]] argues left-to-right pre-training limits language understanding representations. [[GPT-3]] demonstrates that autoregressive models can still become broadly capable when scaled and prompted.
