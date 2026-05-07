# Fine-Tuning

## Summary

Fine-tuning updates a pre-trained model's weights on task-specific or preference-specific data.

## Explanation

[[BERT]] uses fine-tuning as the standard way to adapt a pre-trained encoder to downstream tasks. [[Training Language Models to Follow Instructions with Human Feedback]] also fine-tunes, but its goal is [[Alignment]] and [[Instruction Following]] rather than only benchmark accuracy.

## Related Links

- [[Pre-training]]
- [[BERT]]
- [[Supervised Fine-Tuning]]
- [[Reinforcement Learning from Human Feedback]]
- [[Adaptation]]
- [[In-Context Learning]]

## Source Papers

- [[BERT]]
- [[Language Models are Few-Shot Learners]]
- [[On the Opportunities and Risks of Foundation Models]]
- [[Training Language Models to Follow Instructions with Human Feedback]]

## Contradictions and Tensions

- [[Language Models are Few-Shot Learners]] criticizes reliance on task-specific fine-tuning datasets and evaluates without gradient updates. [[BERT]] and [[InstructGPT]] show that fine-tuning remains powerful when the target is task accuracy or human preference alignment.
