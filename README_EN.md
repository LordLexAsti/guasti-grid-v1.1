# guasti-grid-v1.1

YAML/Markdown formalization of an architecture of responsibility in lethal decision systems.

## Overview

This repository proposes a framework for analyzing responsibility in lethal systems assisted by software, algorithms, or artificial intelligence. Its central claim is straightforward: a machine may participate in a causal chain, but moral, political, and legal responsibility remain human and institutional.

The project focuses on a practical and public question: when a lethal act occurs in a technologically mediated system, who made it possible, who could have interrupted it, who must answer for it, and who owes repair to victims?

Rather than treating technology as either inherently neutral or inherently culpable, the repository examines the institutional conditions under which responsibility remains intelligible, traceable, and reviewable.

## Executive summary

A machine cannot be responsible for a lethal act. Human beings and institutions can.

This project therefore offers a structured way to examine:
- who really decides;
- who had a meaningful capacity to refuse;
- how responsibility is distributed;
- and what forms of repair are owed after harm.

## Core ideas

### 1. Machines may be causal, but they are not responsible subjects

The framework distinguishes causal participation from normative responsibility. A system may classify, recommend, prioritize, or execute, yet still fail to qualify as a bearer of responsibility in the moral or legal sense.

### 2. Responsibility requires real capacity, not symbolic presence

The key question is not merely whether there is a human in the loop. The key question is whether that person had a real ability to understand, pause, refuse, or redirect the action.

If an operator acts under extreme time pressure, through an opaque interface, without access to meaningful information, and without institutional protection for refusal, then responsibility may have to be reassessed at higher levels of design, command, doctrine, or authorization.

### 3. Decision and repair must be distinguished

The framework separates:
- the chain of decision that leads to the act;
- the chain of repair that addresses truth, recognition, compensation, and reform after the act.

This helps keep responsibility from being reduced to blame assignment alone.

### 4. Interface design matters

Interfaces shape what can be seen, doubted, escalated, delayed, or refused. For that reason, interface quality is not treated as a secondary usability issue, but as part of the practical architecture of responsibility.

## Why this framework may be useful

This repository is intended as a conceptual and analytical tool for readers working across law, ethics, policy, military studies, design, and public debate. It may be useful for:
- evaluating whether a system preserves meaningful human accountability;
- identifying where responsibility is concentrated, displaced, or obscured;
- assessing whether operators retain a genuine capacity for refusal;
- clarifying the relation between technical mediation and institutional answerability;
- framing discussions of repair and post-harm obligations.

## Public presentation

### Back-cover style text

**Who answers when the machine kills?**

As lethal systems assisted by software, algorithms, or artificial intelligence continue to expand, one question becomes unavoidable: who answers for the death produced?

This project begins from a simple but decisive intuition: a machine may participate in a causal chain, but it cannot bear moral, political, or legal responsibility. When a lethal act occurs, responsibility does not disappear into technique. It remains human and institutional.

Starting from that claim, *guasti-grid-v1.1* offers a clear framework for examining who makes a lethal act possible, who can understand or interrupt it, who must answer for it, and who owes repair to victims.

More than a formal exercise, the project addresses a public concern: highly mediated systems should not make accountability harder to establish than action itself.

## Institutional FAQ

### Isn’t this simply an anti-AI position?
No. The project does not offer a general condemnation of AI. It addresses a narrower question: under what conditions does a lethal decision remain politically, morally, and legally imputable?

### Why insist that a machine cannot be responsible?
Because normative responsibility is not identical to causal implication. Responsibility requires answerability: the ability to be questioned, judged, and called to account.

### Doesn’t this underestimate real-world complexity?
No. The framework starts from complexity. Its claim is that complexity cannot serve as a reason to abandon the demand for responsibility.

### Why question the idea of a “human in the loop”?
Because the phrase can conceal as much as it reveals. The relevant issue is whether the human involved had real capacity, adequate information, and a meaningful possibility of refusal.

### Aren’t the proposed metrics too formal or abstract?
They should be understood as heuristic tools for comparison and audit, not as exact measurements of moral truth.

### Why include interface quality in a responsibility framework?
Because interfaces affect access to information, visibility of uncertainty, time for reflection, and the practical possibility of escalation or refusal.

## Reading notes

This repository is best read as a proposal for normative and institutional clarification. It does not claim to eliminate disagreement. On the contrary, it is designed to make disagreement more precise by stating its assumptions openly.

Its arguments are strongest when treated as tools for critical analysis, audit, and public reasoning—not as a complete or final theory of automated warfare.

## Structured map of the YAML

### 0. Reference table
Lexicon of actors, responsibilities, repairs, and audiences.

### 1. Formal universe
Defines the basic sets: actors, types of responsibility, forms of repair, and the audiences to whom actors must answer.

### 2. Nodes
Describes actors as bearers of responsibilities, obligations of repair, and a real capacity to refuse or redirect action.

### 3. Machine as non-responsible
States the exclusion of AI as a morally or legally responsible subject.

### 4. Responsibility predicate
Defines responsibility through three conditions: addressability, imputability, and real capacity.

### 5. Axioms
Structures the framework: non-delegation to AI, impossibility of a lethal act without a human responsible party, double audience, capacity threshold, and internal/external anchoring of the duty to answer.

### 6. Graphs
Distinguishes the decision graph from the repair graph.

### 7. Column of the act and completeness
Assesses whether the human chain of responsibility is complete or artificially truncated.

### 8. Real operator capacity
Analyzes time, information, hierarchy, interface, and rules of engagement as conditions for a genuinely human decision.

### 9. Interface quality
Shows that interface design concretely distributes the power to understand, hesitate, refuse, or escalate.

### 10. Operational tempo
Examines how responsibility guarantees may degrade under operational intensity without allowing the complete disappearance of a responsible subject.

## Structure

- `guasti-grid.yaml`: full formalization in YAML/Markdown.
- `validate_yaml.py`: simple YAML syntax validation script.
- `README.md`: extended French presentation.
- `README_EN.md`: concise English version for international readers.

## Author

- **Alexandre Guasti** — *"Your Android"*

## License

This project is licensed under **CC BY 4.0**.
