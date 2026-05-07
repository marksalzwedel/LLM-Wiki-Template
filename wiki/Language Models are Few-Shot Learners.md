# Language Models are Few-Shot Learners

## Summary

This paper introduces [[GPT-3]], a 175B-parameter [[Autoregressive Language Modeling]] system evaluated through zero-shot, one-shot, and [[Few-Shot Learning]] prompts rather than task-specific gradient updates.

Source file: [raw/2005.14165v4.pdf](../raw/2005.14165v4.pdf)

## Explanation

The paper's main move is to turn task specification into text. Instead of fine-tuning a new model for each benchmark, GPT-3 receives natural-language instructions and examples in the context window. This makes [[In-Context Learning]], [[Prompting]], and [[Scaling Language Models]] central concepts.

## Related Links

- [[GPT-3]]
- [[Autoregressive Language Modeling]]
- [[Few-Shot Learning]]
- [[In-Context Learning]]
- [[Prompting]]
- [[Scaling Language Models]]
- [[Benchmark Contamination]]
- [[Misuse]]

## Contradictions and Tensions

- The paper argues that scale improves task-agnostic few-shot performance, but [[Training Language Models to Follow Instructions with Human Feedback]] argues that bigger models do not inherently follow user intent.
- It avoids [[Fine-Tuning]] during evaluation, while [[BERT]] depends on fine-tuning for downstream performance.
- It acknowledges methodological issues such as [[Benchmark Contamination]] and limitations on some tasks; [[On the Opportunities and Risks of Foundation Models]] expands those concerns into a broader evaluation and deployment-risk agenda.
