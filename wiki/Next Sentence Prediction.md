# Next Sentence Prediction

## Summary

Next sentence prediction is a BERT pre-training task that asks whether two text segments appeared consecutively in the original corpus.

## Explanation

[[BERT]] uses this task to help learn sentence-pair relationships for downstream tasks such as natural language inference and question answering. It sits beside [[Masked Language Modeling]] as the second pre-training objective in the original BERT setup.

## Related Links

- [[BERT]]
- [[Masked Language Modeling]]
- [[Pre-training]]
- [[Fine-Tuning]]
- [[Evaluation]]

## Source Papers

- [[BERT]]

## Contradictions and Tensions

- No other paper in this set directly tests or rejects next sentence prediction. The broader tension is that later GPT-style work prefers text-prompt task specification over BERT's task-head and sentence-pair fine-tuning setup.
