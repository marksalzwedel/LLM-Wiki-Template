# GPT-3

## Summary

GPT-3 is a 175B-parameter autoregressive Transformer language model introduced in [[Language Models are Few-Shot Learners]].

## Explanation

GPT-3 is trained with [[Autoregressive Language Modeling]] and evaluated by writing tasks directly into the context window. Its importance in this vault is not only size, but the shift from task-specific [[Fine-Tuning]] toward [[Prompting]], [[Few-Shot Learning]], and [[In-Context Learning]].

## Related Links

- [[Language Models are Few-Shot Learners]]
- [[Autoregressive Language Modeling]]
- [[Prompting]]
- [[Few-Shot Learning]]
- [[In-Context Learning]]
- [[Scaling Language Models]]
- [[Benchmark Contamination]]
- [[Misuse]]

## Source Papers

- [[Language Models are Few-Shot Learners]]
- [[On the Opportunities and Risks of Foundation Models]]
- [[Training Language Models to Follow Instructions with Human Feedback]]

## Contradictions and Tensions

- [[Training Language Models to Follow Instructions with Human Feedback]] uses GPT-3 as the base system but argues that raw scale is not enough for user intent.
- [[BERT]] shows a different route to language understanding: smaller bidirectional encoders fine-tuned for downstream tasks.
