# ChatGPT Export Prompt for Conlang Work

**Use this prompt with ChatGPT to extract and format your conlang details for Claude analysis.**

---

## The Prompt

```
I have a constructed language I've been developing. I need to export the current state 
in a format that another AI (Claude) can analyze and build on. 

Please extract and format the following information about my language. Use this exact 
structure and fill every cell/section completely—mark uncertain items with "?" and 
defective/inapplicable items with "—", but do not leave cells blank.

---

FRONT MATTER
============

Language Name: [what is it called?]
GitHub Repo: [if you have one; otherwise "none yet"]
Current Phase: [what have you finished? 1=phonology only, 2=phonology+roots, 
               3=morphology draft, 4=morphology complete, 5=syntax, 6=lexicon, 7=testing]
Last Updated: [date]
Known Gaps: [list 2-3 biggest open questions or contradictions]

---

PHONOLOGY
=========

Consonant Inventory:
[List all consonants in IPA, organized by place/manner. Example: 
p t k | b d g | m n ŋ | f s x | v z | l r]

Vowel Inventory:
[List all vowels in IPA, organized by height/backness. Example:
i u | e o | a]

Syllable Structure:
[Describe allowed syllable templates. Examples: CV, CVC, CVCC, (C)VC, etc.]

Onset Clusters:
[What two-consonant or multi-consonant onsets are allowed? "none", "limited to X", 
or list examples like "pt, st, sn"]

Coda Constraints:
[Which consonants can appear at syllable/word end? "all", "only sonorants", 
"only stops", etc.]

Stress/Tone/Prosody:
[Is there lexical stress? Tone? Neither? Example: "Stress on penult" or 
"No lexical stress" or "4 tones: high, mid, low, rising"]

Allophony:
[Are there systematic sound changes in certain contexts? Example: 
"/x/ → [h] before high vowels" or "none noted"]

---

MORPHOLOGY
==========

Alignment Type:
[nominative-accusative / ergative-absolutive / active-stative / tripartite / 
 split-ergative / other]

Morphological Type:
[isolating / agglutinative / fusional / polysynthetic / mixed]

CASE SYSTEM (if you have one):

[Create a complete table with NO BLANK CELLS. Use "—" for defective/inapplicable 
and "?" for unknown. Example:]

| Case | Suffix | Core Meaning | Notes |
|------|--------|--------------|-------|
| ABS | Ø | patient / intransitive subject | core argument |
| ERG | -ku | agent | core argument |
| GEN | -se | possessor | never directionalizes |
| LOC | -te | at / in | directionalizes: Ø/-te, i-...-te, a-...-te |
| ... | ... | ... | ... |

[If directional cases exist, add this table:]

| Base Case | Neutral Form | i- Form (toward) | a- Form (away) |
|-----------|--------------|-----------------|----------------|
| LOC | -te | i-...-te (allative) | a-...-te (ablative) |
| ... | ... | ... | ... |

AGREEMENT SYSTEM (if present):

Person categories: [1st, 2nd, 3rd? Inclusive/exclusive? "none"]
Number categories: [singular, plural? Dual? "none"]
Gender/Noun classes: [list them, or "none"]
Agreement triggers: [does verb agree with subject? object? both? does adjective 
                     agree with noun? examples]

VERB TEMPLATE:

[Show the morpheme order in verbs. Example: ROOT-TENSE-ASPECT-MOOD-AGREEMENT]

Position 1 (ROOT): [examples: "kap, vel, tim"]
Position 2 (TENSE): ["-past, -pres, -fut" or "none"]
Position 3 (ASPECT): ["-perf, -impf" or "none"]
Position 4 (MOOD): ["-ind, -subj, -cond" or "none"]
Position 5 (POLARITY/DIRECTION): ["i-, a-, Ø" or "none"]
Position 6 (AGREEMENT): ["-1sg, -3pl" or "none"]
[Add more positions if needed]

VERB PARADIGM (complete—every cell filled):

[Show conjugation across person/number for at least one tense. Example:]

| Person/Number | Present | Past | Future |
|---|---|---|---|
| 1SG | -ø | -ak | -ib |
| 2SG | -is | -as | -id |
| 3SG | -i | -a | -i |
| 1PL | -om | -om | -im |
| 3PL | -on | -an | -in |

---

SYNTAX
======

Basic Word Order:
[SVO / SOV / VSO / VOS / OVS / OSV]

Modifier Order:
[Adjective-Noun or Noun-Adjective?]

Genitive Position:
[Pre-nominal (genitive-noun) or post-nominal (noun-genitive)?]

Adposition Type:
[Pre-position (prep-noun) or post-position (noun-postp)?]

Negation Strategy:
[particle, morpheme, word order, tone, or other?]

Interrogative Strategy:
[word order change, particle, tone, or other?]

Relative Clause Position:
[Pre-nominal, post-nominal, or internally headed?]

---

LEXICON
=======

Root Template:
[CVC, CVCV, CV, CVCC, or other?]

Total Roots So Far:
[number, or "none yet"]

Root List (if available):
[Format as: [root] /IPA/ — gloss — (POS)]

Examples:
[root] /kap/ — to hold — (VERB)
[root] /tim/ — person — (NOUN)

Sound Symbolism (if any):
[Do certain sounds correlate with meanings? Example: 
"High vowels (i, u) in small/light words; low vowels (a) in big/heavy words"]

---

EXAMPLES
========

[Provide 3-5 sentences in the language with interlinear glosses using Leipzig 
conventions. CRITICAL: Every morpheme needs a gloss, and the line below should 
be an English translation. Example format:]

1. Kap-tim-Ø i-vel-a-1SG.
   hold-person-ABS toward-give-PAST-1SG
   'I gave the person to hold.' OR 'I gave (it) to the person.'

2. [Another example with gloss + translation]

---

OPEN QUESTIONS / DECISIONS PENDING
===================================

[List 2-5 things you're unsure about or haven't decided yet:]

- [Question 1]
- [Question 2]
- [Question 3]

---

NOTES & CONTEXT
===============

[Anything else relevant? Design goals, aesthetic, typological direction, or 
constraints you're working within? Example: "I want it to feel compact and 
consonant-heavy" or "Active-stative alignment is crucial to the design"]

---

Now, please output this structure filled in with everything you know about 
my language. For any section I didn't fill in or you're unsure about, mark it 
with "?" or leave it as a prompt for me (e.g., "I don't have information about 
your verb paradigm—what tenses do you mark?"). 

Do NOT leave table cells blank. Every cell must have a value, "?", or "—".

Include example sentences if we've developed any; if not, just say "no examples 
yet."

Format the output so I can copy-paste it directly into a markdown file or send 
to Claude.
```

---

## How to Use This Prompt

1. **Copy the prompt above** (everything inside the backticks)
2. **Paste into ChatGPT** with your language name and any context you want to add
3. **ChatGPT will ask clarifying questions** if you haven't filled in sections—answer them
4. **Copy ChatGPT's output** into a markdown file (or save as `.md`)
5. **Send the output to Claude** with a message like:

   ```
   Here's my language exported from ChatGPT. Can you [specific task]?
   [paste the formatted export]
   ```

---

## What Makes This Prompt Effective

- **Explicit structure** — ChatGPT knows exactly what sections to fill
- **No blank cells rule** — Forces completeness; incomplete data is marked `?` or `—`
- **Examples required** — Forces you to test the language, not just describe it
- **Table format** — Easy for Claude to parse and work with
- **Open questions section** — Shows Claude what you're still uncertain about

---

## Variations

### Minimal Export (Early Phases)
If you're still on Phase 1–2 (just phonology/basic morphology), simplify:

```
Just focus on:
- Front matter
- Phonology
- Morphology: case system OR verb template (whichever you have)
- Open questions

Skip syntax, lexicon, examples if you haven't developed them yet.
```

### Detailed Export (Advanced Phases)
If you're on Phase 5+ (syntax/lexicon), add:

```
ADDITIONAL SECTIONS:
- Phrase structure (head-initial vs. head-final consistency)
- Clause combining (coordination, subordination, switch-reference)
- Information structure (topic/comment, focus marking)
- Lexical gaps (what semantic domains still need roots?)
```

---

## Tips

**Before sending to ChatGPT:**
- Have your language notes/Google Doc ready
- If you're unsure about something, it's fine to ask ChatGPT to infer or make a guess—just mark it `?`
- Provide any examples you've already created

**After ChatGPT outputs:**
- Scan for blank cells—if any exist, ask ChatGPT to fill them
- Check paradigm tables for consistency (do rows/columns make sense?)
- Verify examples are in your language (not made up by ChatGPT)

**Before sending to Claude:**
- Paste the full export
- Add your question/what you want to work on next
- Include GitHub URL if you have one

