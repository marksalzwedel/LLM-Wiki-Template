# Evaluation

## Summary

Evaluation is the process of measuring model behavior, including benchmark accuracy, human preference, robustness, safety, and deployment fitness.

## Explanation

[[BERT]] emphasizes benchmark scores across NLP tasks. [[Language Models are Few-Shot Learners]] evaluates broad zero-shot, one-shot, and few-shot behavior while studying [[Benchmark Contamination]]. [[Training Language Models to Follow Instructions with Human Feedback]] uses human preference evaluations, truthfulness, toxicity, and public NLP regressions. [[On the Opportunities and Risks of Foundation Models]] argues that evaluation must expand across societal and domain-specific risks.

## Related Links

- [[Benchmark Contamination]]
- [[Few-Shot Learning]]
- [[Alignment]]
- [[Truthfulness and Toxicity]]
- [[Bias and Fairness]]
- [[Safety Ecosystem]]

## Source Papers

- [[BERT]]
- [[Language Models are Few-Shot Learners]]
- [[On the Opportunities and Risks of Foundation Models]]
- [[Training Language Models to Follow Instructions with Human Feedback]]

## Contradictions and Tensions

- Benchmark improvement can overstate real capability when data contamination, prompt sensitivity, distribution shift, or harmful behavior are not measured.
- Human preference evaluation captures user-facing quality better than static benchmarks, but it depends on who the labelers are and what instructions they receive.
