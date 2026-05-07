# Human Feedback

## Summary

Human feedback is data from people about desired model behavior, including demonstrations, rankings, labels, and preference judgments.

## Explanation

In [[Training Language Models to Follow Instructions with Human Feedback]], labelers write demonstrations and rank model completions. Those rankings train [[Reward Models]], which then guide [[Reinforcement Learning from Human Feedback]].

## Related Links

- [[Alignment]]
- [[Instruction Following]]
- [[Supervised Fine-Tuning]]
- [[Reward Models]]
- [[Reinforcement Learning from Human Feedback]]
- [[Evaluation]]

## Source Papers

- [[Training Language Models to Follow Instructions with Human Feedback]]
- [[Language Models are Few-Shot Learners]]
- [[On the Opportunities and Risks of Foundation Models]]

## Contradictions and Tensions

- Human feedback improves user-facing behavior, but it reflects the sampled labelers, researchers, policies, and prompts. It is not the same as a universal solution to human values.
