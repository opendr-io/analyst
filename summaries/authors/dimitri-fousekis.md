# Topic: Author: Dimitri Fousekis

## Executive Summary

The available corpus for “Author: Dimitri Fousekis” contains one attributed record: a BSidesLV 2025 talk titled **“Password Expiry is Dead: Real-World Metrics on What Rotation Actually Achieves”** [record_id:2500]. The record presents a security and governance-focused critique of traditional password expiration policies, especially routine 90-day password resets. Its central argument is that forced password rotation often fails to improve security and may actively degrade it by encouraging users to create predictable password mutations that reduce entropy and remain susceptible to cracking [record_id:2500].

The talk’s distinctive contribution, based on the abstract, is its emphasis on **real-world enterprise credential datasets**, **cracked password timelines**, and **behavior analysis** as evidence for evaluating whether password rotation achieves its intended security goals [record_id:2500]. Rather than treating password expiration as a compliance default, the talk proposes alternatives aligned with attacker behavior and measurable credential risk, including **time-to-crack scoring**, **event-driven rotations**, and **credential risk thresholds** [record_id:2500].

Because there is only one record, the evidence base is narrow. The summary can identify one clear research direction associated with Dimitri Fousekis in this dataset: data-driven reassessment of password governance practices, particularly the rejection of blanket periodic password expiry in favor of risk-based credential management.

## Research Landscape

The dataset includes a single conference talk record from **BSidesLV 2025**, sourced from the BSidesLV archive [record_id:2500]. The talk is tagged as part of **PasswordsCon**, with logistical metadata indicating “Tuscany,” “Wednesday,” and an 11:00–11:20 time slot [record_id:2500]. Its topic membership is classified secondarily under governance, risk, and compliance, while its primary topic metadata points to identity, OAuth, and access delegation. However, the raw record text itself focuses specifically on **password expiration**, **enterprise credential behavior**, and **risk-based alternatives to forced rotation** [record_id:2500].

The research area represented here sits at the intersection of:

- Password policy governance;
- Enterprise identity and access management;
- Credential-cracking realism;
- User behavior under security policy constraints;
- Security metrics for password risk;
- Compliance-driven versus attacker-model-driven controls [record_id:2500].

The record is not a full paper, transcript, or slide deck; it is an abstract-style description of a talk. As such, it provides enough detail to identify the argument, the claimed evidence types, and the proposed alternatives, but not enough to independently evaluate the dataset methodology, statistical results, cracking rules, sample size, enterprise contexts, or implementation details [record_id:2500].

## Major Themes And Trends

### Rejection of Traditional Password Expiry as a Default Control

The dominant theme in the record is a challenge to the longstanding assumption that regular password resets improve security. The abstract opens by framing password rotation as a decades-old organizational practice justified by the belief that “regular resets increase security,” then directly questions whether that assumption holds in practice [record_id:2500].

The talk’s title, **“Password Expiry is Dead,”** signals a strong position: routine password expiration is treated not merely as outdated, but as potentially counterproductive [record_id:2500]. The record specifically mentions organizations still enforcing **90-day resets**, implying that periodic rotation remains common despite growing skepticism in modern security guidance [record_id:2500].

### User Behavior Undermines Forced Rotation

A second major theme is that forced password changes produce predictable user behavior. According to the abstract, analysis of enterprise credential datasets before and after forced rotations reveals that “most users simply mutate old passwords” [record_id:2500]. This is presented as a key reason periodic rotation can fail: users respond to the burden of reset requirements by making minimal, pattern-based changes rather than choosing fundamentally stronger credentials.

The talk argues that these mutations create passwords that are “predictable” and “easier to crack, not harder” [record_id:2500]. This shifts the discussion away from theoretical password freshness and toward actual adversarial utility: if attackers can infer common mutation patterns, periodic rotation may produce a false sense of improvement while preserving or worsening crackability.

### Entropy and Crackability as Better Measures Than Rotation Frequency

The abstract claims that password expiration policies “decrease entropy over time” [record_id:2500]. This is an important conceptual reframing. Rather than measuring success by whether users changed passwords on schedule, the talk appears to evaluate policy outcomes by whether resulting passwords become more or less resistant to cracking.

The mention of **cracked password timelines** suggests a longitudinal or time-based analysis: passwords may be examined according to when they are cracked, how rotation affects their resistance, and whether forced updates meaningfully delay compromise [record_id:2500]. The abstract does not provide the numerical results, but it clearly positions crackability and entropy as more relevant metrics than compliance with a password age requirement.

### Compliance Defaults Versus Actual Attacker Models

The talk also contrasts traditional policy assumptions with “actual attacker models” [record_id:2500]. This is a governance theme: password expiry is often embedded in compliance regimes, audit expectations, or inherited enterprise security baselines. Fousekis’s abstract argues that such controls should be judged by whether they reduce compromise risk, not whether they satisfy a conventional checklist [record_id:2500].

The phrase “ammunition — and the data — to rethink that approach entirely” indicates the talk is designed partly for practitioners who need evidence to challenge existing organizational policy [record_id:2500]. The framing suggests a practical audience: security teams, identity administrators, governance/risk/compliance stakeholders, and leaders deciding whether to retire routine expiry requirements.

### Movement Toward Risk-Based Credential Management

The final theme is substitution rather than mere critique. The abstract does not only argue against 90-day resets; it introduces alternatives: **time-to-crack scoring**, **event-driven rotations**, and **credential risk thresholds** [record_id:2500]. These alternatives indicate a shift from calendar-based control to risk-based control.

In this model, password changes would be triggered by measurable signs of credential risk or compromise likelihood, rather than elapsed time alone. The talk’s proposed approach appears to be more adaptive, empirically grounded, and aligned with attacker behavior [record_id:2500].

## Methods, Tools, And Approaches Discussed

The record references several methodological components, though it does not provide implementation details.

First, the talk claims to use **real-world data** to challenge the value of password expiry policies [record_id:2500]. The abstract specifies analysis of **enterprise credential datasets before and after forced rotations** [record_id:2500]. This implies a comparative methodology: examine password characteristics prior to a forced reset event, examine them again afterward, and determine whether the new credentials show improved security properties or predictable mutation from previous passwords.

Second, the talk uses **cracked password timelines** [record_id:2500]. This suggests measuring how long passwords survive against cracking attempts, or mapping the sequence in which credentials are cracked. Such timelines can support arguments about whether rotation meaningfully delays attacker success. If many post-rotation passwords are quickly cracked because they follow mutation patterns, then password age alone is a weak proxy for password safety.

Third, the record mentions **behavior analysis** [record_id:2500]. The behavior under analysis appears to be how users respond to forced rotation policies. The claimed finding is that many users mutate old passwords rather than invent entirely new high-entropy credentials [record_id:2500]. This behavioral lens is central: the policy outcome depends not on the written rule, but on predictable human adaptation to that rule.

Fourth, the talk discusses entropy decline. The abstract says expiration policies can “decrease entropy over time” [record_id:2500]. This implies some measurement or estimation of password entropy across rotations, likely comparing whether user-selected changes become more patterned or less complex after repeated forced updates. The record does not specify whether entropy is measured mathematically, approximated by cracking resistance, or inferred from observed mutation structures.

The proposed alternatives are also notable:

- **Time-to-crack scoring**: an approach that evaluates credentials by estimated or observed resistance to cracking rather than age [record_id:2500].
- **Event-driven rotations**: password changes triggered by events such as suspected compromise, exposure, anomalous activity, or other risk indicators rather than a fixed calendar interval [record_id:2500].
- **Credential risk thresholds**: policy triggers based on a measured level of risk, presumably allowing organizations to intervene when a password crosses a defined danger threshold [record_id:2500].

Together, these methods suggest a framework for credential governance that is evidence-driven and risk-triggered instead of compliance-calendar-driven.

## Notable Talks, Records, And Evidence

The sole record, **“Password Expiry is Dead: Real-World Metrics on What Rotation Actually Achieves,”** is the central and only evidence source for this author topic [record_id:2500]. It is notable because it addresses a common enterprise security policy with a direct empirical critique. The talk’s importance lies in its combination of three claims:

1. Forced password rotation often leads users to mutate existing passwords [record_id:2500].
2. Those mutations create predictable, pattern-based credentials that are easier to crack [record_id:2500].
3. Organizations should replace routine expiration with more attacker-aligned mechanisms such as time-to-crack scoring, event-driven rotations, and credential risk thresholds [record_id:2500].

The record is especially relevant to research agents investigating password policy modernization, enterprise identity governance, or the decline of mandatory periodic password resets. It gives a concise practitioner-facing argument for retiring blanket 90-day resets and replacing them with measurable, risk-based approaches [record_id:2500].

The strength of the record is that it claims to be based on real-world enterprise credential datasets and pre/post rotation analysis [record_id:2500]. However, because the record is an abstract rather than the underlying data or full presentation, its claims should be treated as directional evidence rather than independently verified findings.

## Gaps, Limits, And Open Questions

The evidence base is very thin because only one record is available. The abstract makes several substantive claims, but it does not include enough methodological detail to assess them independently.

Important open questions include:

- What enterprise credential datasets were used, and how large were they? [record_id:2500]
- Were the datasets drawn from one organization, multiple organizations, or a broader industry sample? [record_id:2500]
- How were passwords collected, stored, anonymized, or ethically handled? [record_id:2500]
- What cracking methodology was used to generate the “cracked password timelines”? [record_id:2500]
- How was “entropy” measured, and how was entropy decline quantified over time? [record_id:2500]
- What proportion of users mutated old passwords after forced rotation, and what mutation patterns were most common? [record_id:2500]
- Did the talk compare organizations with and without forced rotation policies? [record_id:2500]
- How were compromise risk and reduction in compromise risk evaluated? [record_id:2500]
- What operational model is proposed for implementing time-to-crack scoring or credential risk thresholds in production identity systems? [record_id:2500]
- How should organizations reconcile risk-based alternatives with compliance frameworks that still expect periodic password expiry? [record_id:2500]

There is also no record here showing whether Fousekis has broader work on identity, OAuth, access delegation, passwordless authentication, MFA, credential stuffing, or governance beyond this talk. The current corpus supports only a narrow characterization: in this dataset, Fousekis is represented by a single BSidesLV 2025 talk advocating evidence-based reform of password rotation policies [record_id:2500].

## Coverage And Evidence Notes

This topic contains exactly one record, and it is fully accounted for in the synthesis.

- **[record_id:2500]** is a BSidesLV 2025 talk by Dimitri Fousekis titled **“Password Expiry is Dead: Real-World Metrics on What Rotation Actually Achieves.”** The record argues that traditional password expiration policies, especially routine forced resets, may decrease security by encouraging users to mutate old passwords into predictable forms. It claims support from real-world enterprise credential datasets, cracked password timelines, and behavior analysis. It proposes alternatives including time-to-crack scoring, event-driven rotations, and credential risk thresholds. This is the only evidence source for the topic, so all conclusions about Fousekis’s recurring themes or unique contributions are necessarily limited to this single presentation [record_id:2500].