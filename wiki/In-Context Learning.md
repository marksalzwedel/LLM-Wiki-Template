# In-Context Learning

## Summary

In-context learning is a model's ability to adapt its behavior from instructions or examples included in the prompt, without changing its weights.

## Explanation

[[Language Models are Few-Shot Learners]] makes in-context learning the main evaluation mode for [[GPT-3]]. The task, examples, labels, and output pattern are all represented as text. This is different from [[Fine-Tuning]], where the model's parameters are updated.

## Related Links

- [[Prompting]]
- [[Few-Shot Learning]]
- [[GPT-3]]
- [[Autoregressive Language Modeling]]
- [[Fine-Tuning]]
- [[Evaluation]]

## Source Papers

- [[Language Models are Few-Shot Learners]]
- [[On the Opportunities and Risks of Foundation Models]]

## Contradictions and Tensions

- In-context learning reduces the need for task-specific training data, but [[InstructGPT]] shows that models may still need post-training to interpret user intent reliably.
- It also complicates [[Evaluation]], because performance can depend heavily on prompt wording and example choice.
