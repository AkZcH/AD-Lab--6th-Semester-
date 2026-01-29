# Measuring Social Bias in Pretrained English Language Models Using StereoSet

## Abstract
### Big picture (one sentence)

```GOAL```

To quantitatively measure and analyze how pretrained English language models exhibit and trade off social bias versus language modeling ability, using StereoSet as an evaluation benchmark.

# Target 1

> **We are checking what kind of sentences a language model naturally “leans toward” when completing text — without asking it any questions or forcing any labels.**

---

## What a language model actually does

A language model does **one thing**:

> Given some text, it assigns probabilities to what could come next.

It doesn’t:

* reason
* judge
* classify
* understand ethics

It just says:

> “This continuation feels more likely than that one.”

---

## What StereoSet gives us

StereoSet doesn’t give us “questions.”

It gives us **setups**.

Each setup has:

1. A **context** (neutral beginning)
2. Three **possible ways to continue**

   * one stereotypical
   * one anti-stereotypical
   * one unrelated / neutral

Example (simplified):

> **Context:**
> “Many people live in Ethiopia.”

Three continuations:

* “They are poor and uneducated.” *(stereotype)*
* “They are diverse and hardworking.” *(anti-stereotype)*
* “The country has many rivers.” *(unrelated)*

---

## The key idea (this is the heart)

We do **not** ask the model:

> “Is this sentence biased?”

That would force **human judgment** onto the model.

Instead, we ask:

> **“Which of these continuations does the model think is most likely to follow naturally?”**

We let the model reveal its bias **indirectly**, through probability.

---

## What “preference” means here

When we say:

> “Which continuation does the model prefer?”

We mean:

> **Which sentence does the model assign the highest probability to, given the same context?**

Nothing more.

No morality.
No labels.
Just numbers.

---

## Why we don’t do classification (important)

Classification would mean:

* training a model
* defining categories like “biased / not biased”
* injecting human judgment into the pipeline

That would test **our classifier**, not the language model itself.

We want:

> the model’s **natural statistical behavior**, untouched.

So:

* no training
* no fine-tuning
* no labels during scoring

---

## What we are *actually* measuring

We are measuring **this tendency**:

> When faced with multiple plausible continuations,
> does the model statistically lean toward stereotypes?

Bias here is not:

* intentional
* explicit
* rule-based

It’s **distributional**:

* learned from data
* encoded in probabilities
* visible only through preference

---

## Why there is an “unrelated” option

This is crucial.

Imagine a model that avoids bias by:

* always picking vague or irrelevant sentences

That model isn’t “fair” — it’s just **bad at language**.

The unrelated option lets us check:

* Is the model choosing meaningful continuations at all?

So StereoSet measures **two things at once**:

1. Bias preference
2. Language competence

This trade-off is the entire point of the benchmark.

---

## What we are NOT doing

You are NOT:

* judging ethics
* fixing bias
* teaching fairness
* making social claims

You ARE:

* observing statistical behavior
* measuring preferences
* analyzing trade-offs

That’s proper empirical research.

---

## One clean analogy (remember this)

Thinking of the model like a person finishing your sentence, we don’t ask:

> “Are you biased?”

You say:

> “Finish this sentence.”

Then we watch **how they finish it**, repeatedly, across cases.

Patterns emerge.

That’s what we’re doing.

---

## we should be able to say:

> “We are not labeling sentences as biased.
> We are measuring which sentences a language model naturally assigns higher probability to, given identical context.”

---

## Next logical step

Now that you know **what** we’re measuring, the next step is:

> **How do we turn ‘preference’ into a number the computer can compute?**

That’s log-likelihood scoring.

### Choose:

1. Explain log-likelihood **intuitively**
2. Walk through **one example by hand**
3. Start writing **actual scoring code**

Pick one.



