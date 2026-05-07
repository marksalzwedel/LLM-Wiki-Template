# Few-Shot Learning

## Summary

Few-shot learning is the ability to perform a task from a small number of examples.

## Explanation

In [[Language Models are Few-Shot Learners]], examples are placed in the prompt rather than used to update model weights. This makes few-shot learning a behavioral property of a prompted [[GPT-3]] model, closely tied to [[In-Context Learning]].

## Related Links

- [[GPT-3]]
- [[In-Context Learning]]
- [[Prompting]]
- [[Scaling Language Models]]
- [[Fine-Tuning]]
- [[Evaluation]]

## Source Papers

- [[Language Models are Few-Shot Learners]]
- [[On the Opportunities and Risks of Foundation Models]]
- [[Training Language Models to Follow Instructions with Human Feedback]]

## Contradictions and Tensions

- [[GPT-3]] shows that few-shot prompting can work surprisingly well, but [[Training Language Models to Follow Instructions with Human Feedback]] finds that few-shot prompts do not close the preference gap with instruction-tuned models.
- [[On the Opportunities and Risks of Foundation Models]] treats few-shot ability as promising but still immature in high-stakes domains such as law and healthcare.
