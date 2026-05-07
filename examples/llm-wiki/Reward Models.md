# Reward Models

## Summary

Reward models are learned models that predict which outputs humans would prefer.

## Explanation

[[Training Language Models to Follow Instructions with Human Feedback]] trains a reward model from pairwise comparisons of model outputs. The reward model becomes an optimization target for [[Proximal Policy Optimization]] during [[Reinforcement Learning from Human Feedback]].

## Related Links

- [[Human Feedback]]
- [[Reinforcement Learning from Human Feedback]]
- [[Proximal Policy Optimization]]
- [[Alignment]]
- [[Evaluation]]

## Source Papers

- [[Training Language Models to Follow Instructions with Human Feedback]]

## Contradictions and Tensions

- Reward models make human preferences optimizable, but they can also inherit labeler biases, misspecify goals, or be exploited by the policy if used beyond their reliable range.
