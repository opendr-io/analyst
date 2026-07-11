# Topic: Author: Christopher Domas

## Executive Summary

The two records attributed to Christopher Domas both describe a 2025 hardware-security research presentation about deliberately synthesizing catastrophic hardware-failure conditions from software in order to cross CPU privilege boundaries. The Black Hat USA 2025 briefing, “Ghosts in the Machine Check - Conjuring Hardware Failures to Breach CPU Privilege Boundaries,” and the DEF CON 33 talk, “Conjuring Hardware Failures for Cross-ring Privilege Escalation,” appear to cover substantially the same research program, with closely matching abstracts and shared phrasing [record_id:92] [record_id:2010].

Across the records, Domas’s central contribution is framed as a new machine-check research vector: taking mechanisms normally associated with rare, unrecoverable hardware faults—such as cosmic ray bit flips, memory degradation, aging I/O devices, or CPU fires—and deliberately inducing comparable fatal events through software-only attacks [record_id:92] [record_id:2010]. Rather than allowing the platform’s normal fail-safe behavior to shut the system down after a Machine Check Exception, the talks describe circumventing those fail-safes, forcing the machine to continue running in a damaged state, and timing injected failure signals during privileged CPU operations to disrupt secure transitions [record_id:92] [record_id:2010].

The records are thin in number but strong in thematic consistency. They present a coherent focus on hardware fault handling, Machine Check Exceptions, secure-transition disruption, cascading failures, recovery from supposedly unrecoverable states, and hardware privilege escalation. The available evidence does not include slides, code, detailed vulnerability identifiers, affected architectures, mitigations, or a transcript. It is therefore best treated as high-level conference-abstract evidence of the research direction rather than a full technical account.

## Research Landscape

The dataset contains two conference records from 2025, both attributed to Christopher Domas and both associated with exploit development and vulnerability discovery. One is a Black Hat USA briefing and the other is a DEF CON 33 video record [record_id:92] [record_id:2010]. The records are not broad biographical coverage of Domas’s career; they are narrowly focused on a single apparent research topic presented at two major security venues.

The Black Hat record situates the work under “Platform Security,” “Hardware / Embedded,” and “Briefings,” with the title “Ghosts in the Machine Check - Conjuring Hardware Failures to Breach CPU Privilege Boundaries” [record_id:92]. The DEF CON record uses the related title “Conjuring Hardware Failures for Cross-ring Privilege Escalation” and is marked as a 45:02 video [record_id:2010]. The two abstracts are nearly identical, suggesting either the same talk adapted for different audiences or companion presentations of the same underlying research.

The research area reflected here sits at the intersection of hardware security, CPU exception handling, privilege-boundary enforcement, platform fail-safe design, and exploit development. The talks focus on Machine Check Exceptions: a class of CPU/platform response used when unrecoverable hardware errors are detected. In ordinary operation, the records say, the platform response is to shut down before the problem worsens [record_id:92] [record_id:2010]. Domas’s work explores what happens when that assumption is broken: when failure conditions are created deliberately from software and the system is coerced into continuing execution after events that would normally be fatal [record_id:92] [record_id:2010].

Because both records are abstracts rather than detailed proceedings, the research landscape is visible mainly through framing. The work appears less concerned with conventional memory corruption or software bug exploitation and more concerned with exploiting the boundary between hardware fault-management logic and CPU privilege architecture. The emphasis on “software-only attacks” is particularly notable because the presented failure mode sounds, at first, like a physical fault-injection domain; the talks instead claim that comparable hardware-failure events can be synthesized without external equipment [record_id:92] [record_id:2010].

## Major Themes And Trends

### Deliberate software synthesis of hardware-failure events

The dominant theme is the transformation of rare or naturally occurring hardware failures into deliberate, attacker-controlled events. Both records begin with examples of catastrophic hardware failures: “an aging I/O device,” “cosmic ray bit flips,” “memory degradation,” and “CPU fires” [record_id:92] [record_id:2010]. These examples establish that Machine Check Exceptions normally belong to the realm of unexpected physical degradation, environmental effects, or unrecoverable hardware malfunction.

Domas’s research, as described in the abstracts, reverses that premise. Instead of waiting for rare failures, the attacker “deliberately create[s] these fatal events from software” [record_id:92] [record_id:2010]. This is the key conceptual move: hardware-failure handling becomes an attack surface. The records suggest that mechanisms intended to contain and halt catastrophic faults may themselves become exploitable if adversaries can trigger, time, and manipulate them.

### Circumventing fail-safes and running “damaged but alive”

A second recurring theme is the subversion of normal platform safety responses. The abstracts state that when an unrecoverable hardware error is detected, the common platform response is to generate a Machine Check Exception and shut down before the problem worsens [record_id:92] [record_id:2010]. The talks then ask what happens when researchers “circumvent all the traditional fail safes” and force the system to continue operating rather than shutting down [record_id:92] [record_id:2010].

The phrase “damaged but alive” appears in both records and captures the research’s distinctive posture [record_id:92] [record_id:2010]. Instead of treating catastrophic hardware-failure paths as terminal conditions, the research examines the security consequences of post-failure execution. The implied trend is that security assumptions may rely too heavily on fail-stop behavior: if the system can be kept running after supposedly unrecoverable faults, privileged invariants may be violated.

### Privilege-boundary disruption during secure CPU transitions

Both talks explicitly connect injected failure signals to privileged CPU operations. The abstracts say the presentation will show how “carefully injecting these signals during privileged CPU operations can disrupt secure transitions” [record_id:92] [record_id:2010]. This points to a timing-sensitive exploitation model: the mere existence of machine-check behavior is not enough; the attack requires introducing failure events at moments when the CPU is crossing or enforcing privilege boundaries.

The Black Hat title emphasizes “breach CPU privilege boundaries,” while the DEF CON title emphasizes “cross-ring privilege escalation” [record_id:92] [record_id:2010]. Together, these titles frame the security impact as movement across CPU protection rings or privilege levels. The records do not specify exactly which rings, instructions, transitions, or privilege modes are involved. However, the shared language about “privileged CPU operations,” “secure transitions,” and “hardware privilege escalation” strongly indicates a focus on the mechanisms CPUs use to separate less-privileged code from more-privileged execution contexts [record_id:92] [record_id:2010].

### Cascading failures as an exploitation path

Another theme is that the injected failures do not merely cause a single controlled fault. The records state that disruptions can “progress to cascading system failures” and that the attacker can “ride the chaos to gain hardware privilege escalation” [record_id:92] [record_id:2010]. This language suggests an exploitation model where reliability breakdown becomes a security opportunity.

The phrase “ride the chaos” is important because it distinguishes the work from deterministic one-bug exploitation as commonly described in software-security abstracts. The attack appears to involve steering or surviving a destabilized execution environment. The records also imply that the researcher has a method for recovering from the induced instability, because both abstracts mention undoing the damage and allowing the system to continue “as if nothing happened” after gaining privileged foothold [record_id:92] [record_id:2010].

### Recovery after “unrecoverable” errors

Both records emphasize not only causing fault conditions but also undoing them. The abstracts say the talk will show “how to undo the damage, recover from the unrecoverable, and let the system continue as if nothing happened” [record_id:92] [record_id:2010]. This is a significant part of the claimed contribution. A naive fault-injection attack that crashes the machine would be less useful for privilege escalation than one that can preserve execution after privilege has been gained.

This theme reinforces the idea that the work is about exploiting the gap between architectural assumptions and practical control. If a Machine Check Exception is designed around the premise that an unrecoverable error terminates normal operation, then recovering from that state under attacker control may expose states that were not intended to be security-hardened.

### A new research vector across technologies and architectures

Both records conclude by framing the topic as an emerging field of “machine check research opportunities” for both attackers and defenders “across technologies and architectures” [record_id:92] [record_id:2010]. This indicates that the talks are not presented merely as a one-off bug demonstration, but as an invitation to examine a broader class of platform behaviors.

There is a slight difference in wording between the records. The Black Hat abstract says the talk will use the “previously unknown vector against [redacted], to reveal another [redacted] hardware vulnerability” [record_id:92]. The DEF CON abstract generalizes this to “use this vector to reveal all-new hardware vulnerabilities” [record_id:2010]. The redactions in the Black Hat abstract imply venue- or disclosure-related limits around the affected target or vulnerability details, while the DEF CON version frames the outcome more broadly.

## Methods, Tools, And Approaches Discussed

The records do not name specific tools, codebases, proof-of-concept repositories, CPU models, operating systems, or instrumentation frameworks. However, they describe several methods and approaches at the conceptual level.

The first method is software-only synthesis of hardware-failure events. Both records explicitly state that the fatal events are “synthesized through software-only attacks” or deliberately created from software [record_id:92] [record_id:2010]. This is notable because catastrophic hardware failures are often associated with physical causes, environmental effects, or specialized fault-injection equipment. The talks instead describe software as the mechanism for provoking hardware-level failure responses.

The second method is manipulation of Machine Check Exception behavior. In the records, Machine Check Exceptions are the common platform response to unrecoverable hardware errors, normally leading to shutdown [record_id:92] [record_id:2010]. The research approach appears to involve triggering such exceptions while preventing or bypassing the usual fail-stop response. This makes machine-check handling itself a security-relevant mechanism.

The third method is precise timing of failure injection during privileged CPU operations. Both abstracts emphasize “carefully injecting these signals during privileged CPU operations” to disrupt secure transitions [record_id:92] [record_id:2010]. The records do not explain how the timing is achieved, what signals are injected, or which transitions are affected. Still, they establish that the attack depends on the interaction between injected hardware-failure signals and privileged execution paths.

The fourth approach is exploitation through controlled instability. The records describe disruptions that become cascading system failures and then privilege escalation [record_id:92] [record_id:2010]. This suggests an exploitation workflow that includes: creating fatal events, preventing shutdown, inducing inconsistent or degraded platform state, crossing a privilege boundary, and recovering the machine afterward. The ability to “undo the damage” and continue as if nothing happened is presented as part of the technique, not merely an aftereffect [record_id:92] [record_id:2010].

The fifth approach is cross-architecture generalization. Both records state that the talks will discuss machine-check research opportunities “across technologies and architectures” [record_id:92] [record_id:2010]. The evidence does not show which architectures are covered, but the framing implies that Domas sees machine-check/failure-handling exploitation as a broader methodology rather than an isolated implementation flaw.

## Notable Talks, Records, And Evidence

The Black Hat USA 2025 record is important because it gives the most specific and formal conference framing for the research. Its title, “Ghosts in the Machine Check - Conjuring Hardware Failures to Breach CPU Privilege Boundaries,” foregrounds Machine Check behavior and CPU privilege-boundary violations [record_id:92]. The abstract walks through a full attack narrative: catastrophic hardware failures, Machine Check Exception shutdown behavior, deliberate software creation of fatal events, fail-safe circumvention, failure injection during privileged CPU operations, cascading system failures, hardware privilege escalation, recovery, and follow-on vulnerability discovery [record_id:92]. It also includes redacted references to a target and another hardware vulnerability, suggesting that some details were withheld or disclosure-controlled at the time of publication [record_id:92].

The DEF CON 33 record is important because it appears to be the public video presentation version of the same research, titled “Conjuring Hardware Failures for Cross-ring Privilege Escalation” [record_id:2010]. The “cross-ring” phrasing is a useful interpretive clue: it makes the privilege-escalation impact more explicit in CPU protection-ring terms [record_id:2010]. The DEF CON record also gives a runtime tag of 45:02, indicating that the source likely corresponds to a full talk video rather than only a schedule abstract [record_id:2010]. Its abstract largely mirrors the Black Hat text but replaces the Black Hat redacted vulnerability phrase with a broader statement about revealing “all-new hardware vulnerabilities” [record_id:2010].

Together, the two records offer strong evidence that Domas’s 2025 work focused on an unconventional hardware-security attack surface: software-triggered machine-check or hardware-failure events used to breach privilege boundaries [record_id:92] [record_id:2010]. Because the records are nearly duplicative, they reinforce the same core claims rather than expanding the evidence base into multiple unrelated works.

## Gaps, Limits, And Open Questions

The most important limitation is that the dataset contains only two records, and both appear to describe the same or very closely related talk. This means the