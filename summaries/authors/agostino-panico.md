# Topic: Author: Agostino Panico

## Executive Summary

The two records attributed to Agostino Panico present a technically advanced security research profile centered on low-level program analysis, reverse engineering, exploit development, and automation. Both records are DEF CON 33 talks from 2025 and describe deep technical work on difficult analysis targets: virtualized software protectors and the Linux eBPF subsystem.

Across the records, Panico’s attributed work emphasizes turning complex, manual security research tasks into systematic workflows. In one talk, the focus is automated unpacking and deobfuscation of nested VM-based software protectors using a framework called DragonSlayer, combining symbolic execution and dynamic taint tracking to recover protected code semantics [record_id:1974]. In the other, the focus shifts to vulnerability discovery and exploitation in Linux eBPF, particularly verifier state tracking bugs, JIT compiler flaws, helper validation bypasses, and the process of turning those bugs into kernel exploit primitives [record_id:1988].

Together, the records suggest recurring interests in: complex execution environments, semantic recovery, state-aware analysis, automation of expert reverse-engineering tasks, and practical exploitation or analyst-enabling outcomes. The evidence base is narrow—only two conference-talk abstracts—but both are substantive and technically specific.

## Research Landscape

The available corpus consists of two DEF CON 33 records from 2025. Both appear to be talk abstracts rather than full transcripts, papers, slide decks, or code repositories. They are therefore strong evidence for the advertised scope, claims, and intended contributions of the talks, but limited evidence for implementation details, empirical validation, or independent assessment.

The two talks sit in adjacent but distinct areas of offensive and defensive security research:

- Malware analysis and reverse engineering, represented by “Automated Unpacking & Deobfuscation of Nested VM-Based Protectors” [record_id:1974].
- Exploit development and vulnerability discovery, represented by “Finding and Exploiting Kernel Vulnerabilities in the eBPF Subsystem” [record_id:1988].

The research landscape reflected by these records is strongly technical and systems-oriented. Both topics deal with environments where naive analysis fails because execution is mediated by complex internal machinery. In the software-protection talk, the complicating machinery is virtualization-based obfuscation, including commercial protectors such as VMProtect and Themida, as well as custom solutions [record_id:1974]. In the eBPF talk, the machinery is the Linux kernel’s eBPF verifier, JIT compiler, helper-function validation paths, and runtime security architecture [record_id:1988].

The dominant source type is conference presentation metadata and abstract text. The records do not include audience Q&A, results tables, vulnerability identifiers, released tooling links, benchmark datasets, or independent reproduction notes. As a result, the corpus is best used to understand the thematic and methodological focus of Agostino Panico’s attributed DEF CON 33 work, rather than to establish confirmed tool performance or vulnerability impact.

## Major Themes And Trends

### Automation of traditionally manual expert analysis

A central theme across the records is the automation of tasks that normally require significant human expertise. In the reverse-engineering talk, DragonSlayer is described as an “automated framework” intended to lift obfuscated bytecode, identify VM handlers, recover instruction semantics, unpack multiple virtualization layers, and reconstruct analyzable protected code representations [record_id:1974]. The abstract explicitly frames the benefit as reducing analysis time “from weeks to hours” [record_id:1974].

In the eBPF talk, the automation theme appears through “state-aware fuzzing methodologies specifically designed for eBPF” [record_id:1988]. Rather than treating eBPF as a generic fuzzing target, the approach claims to incorporate knowledge of the verifier’s internal state machine in order to find bugs in verifier state tracking, JIT compilation, and helper validation [record_id:1988]. This suggests a similar philosophy: encode domain knowledge into tooling or methodology so that high-complexity targets become tractable.

### Semantics and state as the core of analysis

Both records emphasize recovering or reasoning about semantic meaning rather than merely observing surface behavior. DragonSlayer is described as recovering “original instruction semantics” from obfuscated bytecode and reconstructing analyzable representations of protected code [record_id:1974]. This places semantic lifting at the center of the approach: the goal is not only to unpack bytes, but to understand what the protected code does after layers of virtualization have obscured it.

The eBPF talk similarly focuses on internal state, especially the verifier’s state machine. The abstract says the fuzzing methods incorporate knowledge of verifier state and target verifier state tracking bugs [record_id:1988]. In eBPF, the verifier’s understanding of register bounds, pointer types, helper-call constraints, and control-flow states often determines whether a program is accepted or rejected. The record specifically mentions converting “bounds calculation errors” into arbitrary read/write primitives, showing that exploitation depends on gaps between the verifier’s semantic model and actual runtime behavior [record_id:1988].

Together, these records show a recurring concern with mismatches between representation and execution. In protected binaries, virtualization hides real instruction semantics behind virtual handlers [record_id:1974]. In eBPF, verifier reasoning may diverge from actual kernel execution, creating exploitable conditions [record_id:1988].

### Layered complexity and nested analysis targets

Both talks address targets with multiple layers of indirection. The software-protection talk explicitly discusses “nested” virtualization techniques and “multiple virtualization layers” [record_id:1974]. These layered protectors hinder both static and dynamic analysis because the analyst must understand not just the protected program, but the virtual machine interpreter or interpreters that mediate its behavior.

The eBPF talk deals with a different kind of layering: user-supplied eBPF bytecode is checked by a verifier, potentially transformed by a JIT compiler, executed inside the kernel, and allowed to call helper functions under validation rules [record_id:1988]. Vulnerability discovery therefore requires reasoning across verifier logic, generated native code, helper-call constraints, and kernel memory effects.

The shared trend is research into environments where security properties depend on multiple translation, interpretation, or validation layers. Panico’s attributed work appears to target precisely those places where complexity accumulates and where traditional analysis methods are likely to miss subtle behavior.

### From analysis to practical outcomes

Both records describe not only theory but practical outputs. DragonSlayer is presented as tooling that helps reverse engineers “slay the virtualization dragon,” with case studies, methodology deep-dives, and a demonstration [record_id:1974]. The claimed practical outcome is faster analysis of protected binaries and automatic unpacking/deobfuscation.

The eBPF talk goes beyond finding vulnerabilities and includes “weaponizing verifier bypasses into practical kernel exploits” [record_id:1988]. The abstract names concrete exploitation steps: turning bounds calculation errors into arbitrary read/write, bypassing KASLR through targeted information leaks, and achieving privilege escalation via memory corruption [record_id:1988]. It also includes hardening recommendations for verifier state tracking, JIT compiler security, and runtime validation [record_id:1988].

This dual emphasis on offensive capability and defensive recommendations is notable. The eBPF record in particular spans vulnerability discovery, exploit construction, and subsystem hardening [record_id:1988]. The DragonSlayer record is more oriented toward analyst capability, but its application to commercial and custom protectors has clear relevance for malware analysis and software-protection research [record_id:1974].

## Methods, Tools, And Approaches Discussed

The most concrete named tool in the records is DragonSlayer, introduced in the talk on automated unpacking and deobfuscation of nested VM-based protectors [record_id:1974]. The raw record describes DragonSlayer as an automated framework combining symbolic execution with fine-grained dynamic taint tracking [record_id:1974]. Its stated workflow includes identifying virtual-machine handlers, recovering original instruction semantics, unpacking multiple virtualization layers, and reconstructing analyzable representations of protected code [record_id:1974].

The methodological pairing of symbolic execution and dynamic taint tracking is significant. Symbolic execution can reason about path constraints and program semantics, while dynamic taint tracking can identify how data flows through execution, including through obfuscated interpreter loops or handler dispatch mechanisms. The record does not provide implementation details, but the abstract implies that these techniques are coordinated to lift obfuscated bytecode systematically rather than through ad hoc manual reversing [record_id:1974].

The eBPF talk’s primary method is state-aware fuzzing tailored to the eBPF subsystem [record_id:1988]. The record contrasts this with “traditional fuzzing” by saying the techniques incorporate knowledge of the verifier’s internal state machine [record_id:1988]. The fuzzing targets include verifier state tracking bugs, JIT compiler flaws, and helper function validation bypasses [record_id:1988]. This suggests that the approach likely generates or mutates eBPF programs in ways designed to stress verifier abstractions, state transitions, bounds reasoning, and differences between verified assumptions and actual generated code.

The eBPF record also describes a systematic exploitation workflow. It mentions converting bounds calculation errors into arbitrary read/write primitives, bypassing KASLR through targeted information leaks, and achieving privilege escalation through constructed memory corruption [record_id:1988]. These are not just vulnerability classes but exploitation stages: first create a verifier/runtime discrepancy, then obtain memory access, defeat address-space randomization, and finally alter privileged kernel state.

On the defensive side, the eBPF talk includes architectural recommendations. The abstract says it provides concrete recommendations for hardening the eBPF subsystem, including improvements to verifier state tracking, JIT compiler security, and runtime validation [record_id:1988]. This indicates that the talk is not solely exploit-focused; it also frames findings in terms of subsystem design and mitigation.

## Notable Talks, Records, And Evidence

“Automated Unpacking & Deobfuscation of Nested VM-Based Protectors” is notable because it presents a named framework, DragonSlayer, and a clear technical contribution in automated reverse engineering [record_id:1974]. The record situates the problem in the context of modern software protectors such as VMProtect, Themida, and custom virtualization solutions, which are said to hinder static and dynamic analysis [record_id:1974]. Its claimed contribution is a framework that combines symbolic execution and dynamic taint tracking to lift obfuscated bytecode and recover semantics [record_id:1974]. The strongest evidence in this record is the specificity of the stated methods and workflow. The weakest part is empirical substantiation: the abstract claims effectiveness against latest commercial and custom protectors and a time reduction from weeks to hours, but does not provide benchmarks or detailed results in the available text [record_id:1974].

“Finding and Exploiting Kernel Vulnerabilities in the eBPF Subsystem” is notable because it covers a full pipeline from vulnerability discovery to exploitation and hardening [record_id:1988]. The record identifies eBPF’s verifier and JIT compilation mechanisms as a significant attack surface [record_id:1988]. Its three major contribution areas are state-aware fuzzing, weaponization of verifier bypasses into practical kernel exploits, and security architecture recommendations for hardening eBPF [record_id:1988]. The talk’s abstract is especially concrete in naming bug and exploitation categories: verifier state tracking bugs, JIT compiler flaws, helper validation bypasses, bounds calculation errors, arbitrary read/write primitives, KASLR bypass, privilege escalation, and memory corruption [record_id:1988]. The evidence is strong for understanding the intended technical scope, but thin on which kernels, vulnerabilities, CVEs, exploit reliability, or mitigations were actually evaluated.

Together, the two records show Panico associated with advanced research into systems where program behavior is transformed before execution: protected binaries transformed through virtualized interpreters, and eBPF programs transformed and constrained by verification and JIT compilation [record_id:1974] [record_id:1988]. This makes the pair representative of a broader research orientation toward program semantics, automated analysis, and exploitation of mismatches between intended and actual execution.

## Gaps, Limits, And Open Questions

The evidence base has several important limits. First, there are only two records, both from the same event and year. This makes it difficult to infer long-term evolution in Agostino Panico’s work, recurring collaborations, publication history, or changes in research focus over time. The records show two substantial technical areas, but not whether these are isolated talks or part of a sustained research agenda.

Second, the records are abstracts rather than full technical artifacts. For DragonSlayer, the available text does not explain how VM handlers are identified, how instruction semantics are represented, how nested virtualization layers are separated, how symbolic execution path explosion is managed, or how dynamic taint is made precise in the presence of obfuscated dispatch and self-modifying behavior [record_id:1974]. It also does not provide evaluation data, sample sizes, error rates, limitations, or comparisons with other unpacking/deobfuscation tools [record_id:1974].

Third, the eBPF record does not identify specific kernel versions, vulnerability identifiers, fuzzing harness details, exploit constraints, affected configurations, or the exact hardening recommendations [record_id:1988]. It names important exploitation goals, including arbitrary read/write, KASLR bypass, and privilege escalation, but the abstract does not show how general or reproducible those techniques are [record_id:1988].

Fourth, the relationship between the two talks is not documented directly. They can be synthesized thematically around automated low-level analysis and state/semantic reasoning, but the records do not state that DragonSlayer techniques are reused in eBPF work, or that the eBPF fuzzing approach builds on the same toolchain as the VM deobfuscation framework.

Open research questions for downstream agents include:

- Was DragonSlayer released publicly, and if so, what are its architecture, supported protectors, and limitations?
- What datasets or protected binaries were used to validate DragonSlayer’s claimed reduction from weeks to hours [record_id:1974]?
- Which eBPF vulnerabilities or classes were discovered using the described state-aware fuzzing methodology [record_id:1988]?
- Were any