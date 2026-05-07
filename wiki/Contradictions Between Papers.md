# Contradictions Between Papers

## Summary

Most differences across these papers are not hard contradictions so much as research tensions. Each later paper keeps part of the earlier story while showing that a different objective, architecture slice, scale regime, or deployment setting changes what matters.

## Main Tensions

- [[Bidirectional Representations]] vs [[Autoregressive Language Modeling]]: [[BERT]] argues that deep bidirectional context is crucial for language understanding tasks, while [[Language Models are Few-Shot Learners]] shows that a left-to-right [[GPT-3]] model can perform many tasks through [[Prompting]] and [[In-Context Learning]].
- [[Fine-Tuning]] vs [[In-Context Learning]]: [[BERT]] centers downstream fine-tuning, but [[Language Models are Few-Shot Learners]] deliberately avoids gradient updates at evaluation time and expresses tasks in text.
- Scale vs intent: [[Language Models are Few-Shot Learners]] emphasizes that scaling improves task-agnostic few-shot performance, while [[Training Language Models to Follow Instructions with Human Feedback]] says bigger models do not inherently follow user intent and reports smaller [[InstructGPT]] models preferred over much larger GPT-3 baselines.
- Benchmark performance vs deployment risk: [[BERT]] and [[Language Models are Few-Shot Learners]] foreground benchmark gains, while [[On the Opportunities and Risks of Foundation Models]] argues that broad deployment also requires attention to [[Homogenization]], [[Bias and Fairness]], [[Misuse]], [[Environmental Impact]], and [[Evaluation]] limits.
- Capability improvement vs misuse: [[Training Language Models to Follow Instructions with Human Feedback]] improves helpful instruction following, but it also notes that models better at following intent may be easier to misuse.
- Self-supervised objective vs alignment objective: [[Pre-training]] learns broad statistical structure from data, but [[Alignment]] work adds [[Human Feedback]], [[Reward Models]], and [[Reinforcement Learning from Human Feedback]] because next-token prediction alone does not define helpful, honest, or harmless behavior.
- "Attention is all you need" vs the full foundation-model stack: [[Attention Is All You Need]] isolates an architecture breakthrough, while [[On the Opportunities and Risks of Foundation Models]] treats architecture as only one ingredient alongside data, systems, adaptation, evaluation, and governance.

## Related Links

- [[LLM Papers Index]]
- [[Transformer Architecture]]
- [[Foundation Models]]
- [[Alignment]]
- [[Scaling Language Models]]
- [[Evaluation]]
