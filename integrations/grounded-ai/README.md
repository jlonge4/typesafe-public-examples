# grounded-ai

[grounded-ai](https://github.com/grounded-ai/grounded_ai) is an MIT-licensed Python library for evaluating LLM and agent outputs. Its `CascadeEvaluator` asks Jev first and sends only the questions Jev is not confident about to an LLM judge of your choice.

## Run

```bash
pip install "grounded-ai[jev]"
export TYPESAFE_API_KEY=...  ANTHROPIC_API_KEY=...
python cascade.py
```

```text
Collins stayed in orbit.   faithful (Jev, confidence 1.00)
Aldrin stayed in orbit.    hallucination (Jev, confidence 1.00)
```

Questions Jev answers below `min_confidence` go to the judge in one call and come back with its pick and reasoning (`result.judged` lists them).

## Benchmark

On 200 agent turns from GeneralFunctionCall-Test (should the turn call a tool or reply?), with Claude Sonnet 4.6 as the judge, a 0.7 threshold sent 37% of questions to the judge. Against Sonnet 4.6 alone, mean time per check went from 2.59 s to 1.28 s and cost per million checks from $7,751 to $2,997, with accuracy 0.695 vs 0.675. The labels are another model's (Kimi K2-thinking) choices, and n is 200. Script, prices, and results: [benchmarks/tool_call](https://github.com/grounded-ai/grounded_ai/tree/main/benchmarks/tool_call).

## Data

Evaluation inputs go to TypeSafe; escalated questions also go to the judge's provider. With `jev_kwargs={"use_local_model": True}`, the first stage runs on Strands Decider locally instead.

Maintained by Josh Longenecker (grounded-ai).
