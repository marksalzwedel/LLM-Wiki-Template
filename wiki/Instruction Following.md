# Instruction Following

## Summary

Instruction following is the ability of a model to understand and execute a user's natural-language request.

## Explanation

[[GPT-3]] can often respond to instructions in prompts, but [[Training Language Models to Follow Instructions with Human Feedback]] argues that instruction following improves substantially when models are trained on demonstrations and preference rankings.

## Related Links

- [[Prompting]]
- [[InstructGPT]]
- [[Alignment]]
- [[Human Feedback]]
- [[Supervised Fine-Tuning]]
- [[Reinforcement Learning from Human Feedback]]

## Source Papers

- [[Language Models are Few-Shot Learners]]
- [[Training Language Models to Follow Instructions with Human Feedback]]

## Contradictions and Tensions

- The core tension is that a model can be linguistically capable and still fail to follow what users actually intend. Prompting helps, but human-feedback fine-tuning changes the model's default behavior.
