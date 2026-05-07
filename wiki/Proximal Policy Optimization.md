# Proximal Policy Optimization

## Summary

Proximal Policy Optimization, or PPO, is the reinforcement-learning algorithm used to optimize InstructGPT against a learned reward model.

## Explanation

[[Training Language Models to Follow Instructions with Human Feedback]] uses PPO to update a supervised fine-tuned GPT-3 policy while keeping updates constrained enough to avoid destabilizing the model. In this vault, PPO is the optimizer connecting [[Reward Models]] to [[Reinforcement Learning from Human Feedback]].

## Related Links

- [[Reinforcement Learning from Human Feedback]]
- [[Reward Models]]
- [[Supervised Fine-Tuning]]
- [[InstructGPT]]
- [[Alignment]]

## Source Papers

- [[Training Language Models to Follow Instructions with Human Feedback]]

## Contradictions and Tensions

- PPO is a mechanism, not a guarantee. If the reward model misses important values or failure modes, PPO can optimize the wrong proxy.
