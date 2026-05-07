# Training Language Models to Follow Instructions with Human Feedback

## Summary

This paper introduces [[InstructGPT]], a family of GPT-3-derived models trained to follow user instructions using demonstrations, preference rankings, [[Reward Models]], and [[Reinforcement Learning from Human Feedback]].

Source file: [raw/2203.02155v1.pdf](../raw/2203.02155v1.pdf)

## Explanation

The training pipeline starts with [[Supervised Fine-Tuning]] on labeler demonstrations, trains a reward model from human comparisons, and then optimizes the policy with [[Proximal Policy Optimization]]. The paper's core claim is that [[Alignment]] with user intent requires more than model scale and next-token prediction.

## Related Links

- [[Instruction Following]]
- [[Human Feedback]]
- [[Supervised Fine-Tuning]]
- [[Reward Models]]
- [[Reinforcement Learning from Human Feedback]]
- [[Proximal Policy Optimization]]
- [[Alignment]]
- [[Truthfulness and Toxicity]]
- [[Safety Ecosystem]]

## Contradictions and Tensions

- This paper directly challenges a simple reading of [[Language Models are Few-Shot Learners]]: a smaller instruction-tuned model can be preferred over a much larger base GPT-3 model.
- It improves helpfulness and reduces some harms, but notes that better instruction following can also increase [[Misuse]] risk.
- It aligns models to the preferences of selected labelers and researchers, not to a universal or settled definition of human values.
