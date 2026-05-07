# InstructGPT

## Summary

InstructGPT is the instruction-following model family introduced in [[Training Language Models to Follow Instructions with Human Feedback]].

## Explanation

InstructGPT starts from GPT-3-style models and adds [[Supervised Fine-Tuning]], [[Reward Models]], and [[Reinforcement Learning from Human Feedback]]. The result is a model better aligned with labeler and researcher preferences for helpful instruction-following behavior.

## Related Links

- [[GPT-3]]
- [[Instruction Following]]
- [[Alignment]]
- [[Human Feedback]]
- [[Supervised Fine-Tuning]]
- [[Reward Models]]
- [[Reinforcement Learning from Human Feedback]]
- [[Truthfulness and Toxicity]]

## Source Papers

- [[Training Language Models to Follow Instructions with Human Feedback]]

## Contradictions and Tensions

- InstructGPT is built from the GPT-3 lineage but revises a scale-only story: smaller instruction-tuned models can be preferred to larger base models on user prompts.
