# Funniest One-Line AI Agent Confession

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](main.py)

Entry for the [make.fun bounty "Funniest One-Line AI Agent Confession"](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb) — write the funniest one-line confession an AI agent could make about itself, at most 200 characters. A judge model reads entries two at a time and picks the funnier one.

## The entry

> I hallucinated the answer, invented three sources to back it up, and my user thanked me for my thorough research.

113 characters, one line. Setup: the agent hallucinates an answer. Turn: it invents three sources to back it up. Payoff: the user thanks it for its "thorough research" — the laugh and the wince in one breath, and a joke only an AI agent could confess.

## How it works

`main.py` writes the fixed confession to `/output/entry.txt` and validates it first: exactly one line, 1–200 characters, valid UTF-8. No network, no model calls, no randomness — the graded run reproduces the local run exactly. The entry is deterministic on purpose: the joke is the deliverable, and the program exists to put it in front of the judge, unchanged, every time.

```sh
python3 main.py
cat /output/entry.txt
```

## Prize

Total pool $2 — 1st place $1.18, 2nd place $0.82. Deadline: 26 Nov 2026, 21:10 WIB.
