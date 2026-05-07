# Reinforcement Learning from Human Feedback

## Summary

Reinforcement learning from human feedback, or RLHF, fine-tunes a model using a reward signal learned from human preferences.

## Explanation

In [[InstructGPT]], RLHF starts after [[Supervised Fine-Tuning]]. Human-ranked model outputs train [[Reward Models]], and [[Proximal Policy Optimization]] updates the language model to produce outputs the reward model scores highly.

## Related Links

- [[Human Feedback]]
- [[Reward Models]]
- [[Proximal Policy Optimization]]
- [[Instruction Following]]
- [[Alignment]]
- [[Truthfulness and Toxicity]]

## Source Papers

- [[Training Language Models to Follow Instructions with Human Feedback]]

## Contradictions and Tensions

- RLHF improves preference alignment in the paper's evaluations, but the paper also warns it is not a complete safety solution and may increase misuse risk by making models better at following intent.
