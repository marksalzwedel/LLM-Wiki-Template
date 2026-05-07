# Supervised Fine-Tuning

## Summary

Supervised fine-tuning updates a pre-trained model on labeled examples or demonstrations.

## Explanation

In [[InstructGPT]], supervised fine-tuning uses labeler-written demonstrations of desired assistant behavior. This creates a model that is better positioned for preference optimization with [[Reward Models]] and [[Reinforcement Learning from Human Feedback]].

## Related Links

- [[Fine-Tuning]]
- [[Instruction Following]]
- [[Human Feedback]]
- [[Reward Models]]
- [[Reinforcement Learning from Human Feedback]]
- [[Alignment]]

## Source Papers

- [[Training Language Models to Follow Instructions with Human Feedback]]
- [[BERT]]

## Contradictions and Tensions

- [[BERT]] uses supervised fine-tuning mainly for task performance. [[InstructGPT]] uses it as an alignment step toward human-preferred behavior.
