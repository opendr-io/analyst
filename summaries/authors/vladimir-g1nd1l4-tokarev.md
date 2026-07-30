# Topic: Author: Vladimir "G1ND1L4" Tokarev

## Meta-Summary

The three records attributed to Vladimir “G1ND1L4” Tokarev are DEF CON 34 talks focused on exploit development at security boundaries commonly assumed to be protective: local AI runtime interfaces, WebAssembly-based Python isolation, and hardware-backed shadow stacks. Collectively, they present Tokarev’s work as systems-oriented offensive security research that tests abstractions against their underlying implementation. The recurring conclusion is that a nominal boundary—managed/native language separation, WASM confinement, or control-flow enforcement—does not provide security if adjacent lifecycle, host-integration, kernel, or instruction-level mechanisms permit it to be crossed.

The records claim concrete outcomes rather than merely conceptual weaknesses: a full exploit in llama.cpp’s Android integration, a server-side exploitation primitive in llama.cpp, an information-disclosure primitive in Ollama, seven Pyodide escapes with two public CVEs, and three ways to place attacker-selected values into protected shadow-stack memory. The work also emphasizes reproducible demonstrations, disclosure, and general audit patterns. However, the available evidence consists only of talk descriptions; it does not include the presentations, exploit code, technical papers, vendor responses for every issue, or independent validation.

## Research Landscape

All three records are official DEF CON 34 talks dated 2026 and categorized primarily around exploit development and vulnerability discovery. Two are collaborations: the local AI runtime research is co-authored with Ofek Itach [record_id:2858], while the WebAssembly/Pyodide sandbox research is co-authored with Saar Pearl [record_id:2878]. The shadow-stack research is attributed to Tokarev alone [record_id:2911]. This small and event-concentrated corpus should therefore be read as a snapshot of one conference program rather than a complete career bibliography.

The research spans three layers of the modern software stack:

- Application and AI infrastructure, particularly native memory safety at Java/JNI, HTTP lifecycle, and Go/C boundaries [record_id:2858].
- WebAssembly-hosted language runtimes and the security consequences of embedding CPython/Pyodide into JavaScript hosts [record_id:2878].
- Operating-system and processor-level exploit mitigations, including Intel CET, ARM64 GCS, Linux memory-management interfaces, and shadow-stack write mechanisms [record_id:2911].

Despite the different technologies, exploit demonstrations dominate all three records. Each starts from a security assumption made by developers or defenders and then examines lower-level behavior that invalidates it. The AI talk rejects the tendency to frame AI security primarily in terms of prompt injection, insisting that local model runtimes remain ordinary native software [record_id:2858]. The Pyodide talk rejects the treatment of WebAssembly itself as a complete application sandbox [record_id:2878]. The shadow-stack talk rejects the idea that protected return-address storage necessarily makes return-address corruption unusable [record_id:2911].

The corpus also bridges vulnerability classes that are often researched separately. It connects memory corruption and lifetime errors to AI runtimes; language-runtime escape to workflow automation and software supply chains; and kernel interfaces or CPU instructions to bypasses of hardware control-flow defenses. Tokarev’s apparent niche in these records is not a single product family, but the examination of compositional failures where individually legitimate subsystems create an exploitable path when combined.

## Major Themes And Trends

### Security boundaries fail at integration points

The strongest cross-record theme is that security claims must be evaluated at the real implementation boundary, not at the level of a product’s marketing or architectural shorthand.

For local AI runtimes, the critical boundaries are Java-to-native JNI integration, concurrent HTTP request and model lifecycle handling, and transfer of lengths and buffers between Go and C. The described bugs arise because object ownership, teardown, or size assumptions become unsafe while crossing these interfaces [record_id:2858]. In the Pyodide research, the meaningful boundary is not simply “Python inside WASM”; it is CPython compiled with Emscripten and embedded in a JavaScript host. If facilities such as `ctypes` or reflection remain reachable, untrusted Python can reportedly reach Emscripten’s JavaScript bridge and enter the host runtime [record_id:2878]. In the shadow-stack work, the nominally protected memory remains affected by kernel mechanisms such as `FOLL_FORCE`, `ptrace`, `userfaultfd`, and `MADV_DONTNEED`, as well as Intel’s expressly provided `WRSSQ` instruction [record_id:2911].

These cases collectively support an “effective boundary” model: the actual security boundary is defined by all reachable interfaces and privileges, including host APIs, lifecycle operations, memory-management behavior, and cross-language conversion rules.

### Native exploitation remains central to emerging platforms

The local AI talk explicitly distinguishes its subject from prompt injection. Its thesis is that AI runtimes deployed on phones, desktops, and internal servers expose conventional native-code attack surfaces [record_id:2858]. The claimed findings include use-after-free conditions, cross-thread object reclamation, attacker-controlled native dereferences, unsafe lengths, out-of-bounds reads, and heap-data disclosure. This places AI infrastructure within established memory-safety and exploit-development practice rather than treating it as an entirely new security category.

A similar “old problems in new settings” trend appears in the Pyodide talk. WebAssembly and embedded Python may look like modern isolation mechanisms, but the practical escape path depends on familiar issues: exposed reflection, foreign-function interfaces, dangerous host bridges, and ambient runtime permissions [record_id:2878]. The talk’s references to workflow automation, spreadsheets, AI agents, desktop wrappers, and CI systems suggest that the same integration mistake recurs across diverse product categories.

### Mitigations are challenged through legitimate system features

The shadow-stack work is especially notable for using intended operating-system or architectural facilities rather than simply disabling CET. The first method uses `/proc/self/mem` and the kernel’s `FOLL_FORCE` behavior to override page protections; a variant combines `fork` and `ptrace`. The second manipulates page-fault handling through `userfaultfd` and supplies replacement shadow-stack content. The third invokes Intel’s user-mode shadow-stack write instruction, `WRSSQ` [record_id:2911].

This reflects a broader concern seen across the corpus: protective mechanisms can be undermined by surrounding functionality that remains available for compatibility, debugging, embedding, or legitimate memory management. The same pattern is visible when `ctypes` or reflection survives inside a supposedly restricted Pyodide environment [record_id:2878], and when ordinary object-lifecycle operations create use-after-free opportunities in local model runtimes [record_id:2858].

### Partial primitives are treated as meaningful research outcomes

The records distinguish among different levels of exploit maturity. In the AI runtime talk, Tokarev and Itach claim one full exploit, one validated server-side primitive, and one disclosure primitive. The Android llama.cpp issue reaches code execution in the embedding application, while the server race is described as reaching remote cross-thread reclamation and an attacker-controlled native dereference but still requiring additional work for stable remote code execution. The Ollama issue is characterized as heap disclosure rather than code execution [record_id:2858].

That calibrated language is important: the record does not collapse every bug into “RCE.” It recognizes exploit primitives and intermediate validation as useful evidence while identifying unfinished exploitation steps. By comparison, the Pyodide record claims immediate host-side code execution in typical Node.js embeddings and configuration-dependent impact in Deno, including full RCE under one default configuration [record_id:2878]. The shadow-stack record makes its strongest impact claim through demonstrations against three historical CVEs, including a root shell while CET remained enabled [record_id:2911].

### Research is paired with disclosure and corrective action

Two records report externally visible outcomes. The Pyodide research cites public advisories for n8n and Grist—CVE-2025-68668 and CVE-2026-24002—within a wider set of seven claimed escapes and additional disclosures [record_id:2878]. The shadow-stack record states that, after the `/proc/self/mem` issue was reported, Linus Torvalds merged Linux commit `599bbba5a36f` to restrict that route [record_id:2911].

At the same time, the researchers stress that a single patch does not settle the architectural problem. The shadow-stack description says a `fork` plus `ptrace` variant remains viable on patched kernels and that the `userfaultfd` method is unaffected by the `/proc/self/mem` patch [record_id:2911]. The Pyodide talk similarly frames the findings as an architectural failure rather than a one-off bug and recommends defenses beyond fragile denylists [record_id:2878].

## Methods, Tools, And Approaches Discussed

The local AI runtime research uses boundary-focused source review and exploit construction. For llama.cpp’s Android integration, the researchers describe a lifetime race in which Java frees a native `llama_context` while native code continues to use it. Their exploitation approach reclaims the freed 648-byte object and redirects a virtual-function-table call to obtain code execution in the embedding application [record_id:2858]. This is a conventional use-after-free exploitation workflow applied to a JNI-backed AI component: identify mismatched ownership, trigger premature destruction, reclaim a precisely sized allocation, and redirect an indirect call.

For llama.cpp’s server component, the approach targets concurrency between idle model teardown and active requests. The resulting dangling pointer lies in a freed 17,816-byte model allocation. The researchers claim remote, cross-thread reclamation and an attacker-controlled native dereference, then explicitly reserve stable RCE as remaining work [record_id:2858]. This highlights lifecycle and allocator analysis under concurrent server workloads rather than only malformed model parsing.

For Ollama, the researchers analyze quantization across a Go/C boundary. Malicious GGUF metadata allegedly supplies unsafe lengths, causing C to read beyond a Go-backed buffer and return heap contents to the caller [record_id:2858]. The implied auditing method is to trace untrusted metadata through cross-language length conversions and verify whether the receiving native code preserves the source language’s buffer bounds and lifetime assumptions.

The Pyodide research starts by reconstructing the host-embedding architecture. Pyodide is CPython compiled to WebAssembly with Emscripten, but it operates inside a JavaScript runtime. The researchers test whether supposedly blocked capabilities can be recovered through reachable mechanisms such as `ctypes` or reflection. They report reaching Emscripten’s `emscripten_run_script*` bridge, thereby crossing from Python/WASM into host-side JavaScript [record_id:2878].

Impact analysis then varies by host. In Node.js, the escaped code reportedly reaches a runtime without a native permission model, making host code execution immediate. In Deno, the escape still reaches the host, but its effects depend on the permissions granted to the embedding runtime; one tested default configuration allegedly provided enough authority for full RCE [record_id:2878]. This is a useful methodological distinction between proving an isolation escape and assessing the post-escape permission envelope.

The Pyodide work also generalizes testing beyond one product. It reports examining n8n and other deployments across workflow automation, spreadsheets, AI agents, desktop wrappers, build tooling, and CI environments. In CI, the researchers emphasize proximity to credentials, tokens, secrets, and release artifacts, converting a runtime escape into a software supply-chain concern [record_id:2878]. Their proposed defensive direction is architectural hardening rather than merely blocking a list of Python modules or names.

The shadow-stack research presents three technically distinct write paths:

1. **`/proc/self/mem` with `FOLL_FORCE`.** An unprivileged process opens its own memory pseudo-file and uses `pwrite()` to modify shadow-stack memory. The record says the kernel’s `FOLL_FORCE` flag overrides normal protections. This was tested on x86-64 CET and ARM64 GCS [record_id:2911].

2. **A `fork` and `ptrace` variant.** The description states this continues to work after the reported `/proc/self/mem` restriction, indicating that the mitigation addressed one access route rather than the full class [record_id:2911].

3. **`userfaultfd`-mediated replacement.** A fault handler is registered on the shadow-stack virtual memory area, a page is discarded using `MADV_DONTNEED`, and a later `RET` faults on the missing page. The handler then supplies a page filled with selected return addresses, which the kernel maps with valid shadow-stack page-table encoding [record_id:2911].

4. **Direct writes using `WRSSQ`.** Intel’s `WRSSQ` instruction permits user-mode writes to shadow-stack pages. Tokarev reports correcting a prior proof-of-concept encoding error: adding a `0x66` prefix produces `ADCX`, not `WRSSQ`. The corrected form was reportedly confirmed on Sapphire Rapids hardware [record_id:2911].

The shadow-stack techniques were evaluated against vulnerabilities in dnsmasq, libinput, and rsync. The talk claims bare-metal demonstrations and a root shell while CET remained active [record_id:2911]. This validation strategy is stronger than presenting synthetic writes alone because it connects the techniques to exploit chains based on real memory-corruption vulnerabilities, although the record does not provide the chains themselves.

## Notable Talks, Records, And Evidence

### Breaking Local AI Runtimes: Exploiting llama.cpp and Ollama

This joint talk with Ofek Itach is representative of Tokarev’s effort to bring conventional native exploitation scrutiny to AI infrastructure. Its three case studies cover distinct trust boundaries rather than variants of one parser bug: JNI object lifetime, HTTP server teardown concurrency, and Go/C buffer handling [record_id:2858].

The strongest claimed result is code execution in an Android application embedding llama.cpp, achieved through reclamation of a freed `llama_context` and vtable redirection. The server issue is less complete but potentially remotely reachable, while the Ollama issue provides an information-disclosure primitive through malicious GGUF metadata [record_id:2858]. The record’s explicit separation of a complete exploit from validated but incomplete primitives gives the evidence a relatively careful scope.

Its unique contribution within the corpus is the direct reframing of local AI security as a native software-security problem. It also offers reusable audit targets: cross-language ownership, asynchronous teardown, thread interaction, metadata-derived lengths, and buffers whose backing storage is controlled by another language runtime [record_id:2858].

### WASM Was Not the Boundary: Sandcastles, Not Sandboxes

Co-authored with Saar Pearl, this talk has the broadest product and ecosystem reach. It argues that products treating Pyodide as a ready-made sandbox may block obvious modules such as `os` or `js` while leaving lower-level capabilities reachable. Through `ctypes` or reflection, attacker-controlled Python can reportedly access the Emscripten-to-JavaScript bridge and escape the intended confinement [record_id:2878].

The record claims seven escapes, two public CVEs, and multiple additional disclosures. The named public cases concern n8n and Grist, giving this record the clearest advisory-level anchors in the corpus [record_id:2878]. It also distinguishes Node.js from Deno embeddings: an escape into Node.js commonly gives immediate host code execution, whereas Deno can reduce impact if its permissions were constrained, though the researchers found at least one default configuration that still enabled full RCE [record_id:2878].

Its principal contribution is a more precise model of WASM isolation. The talk argues that evaluators must trace all routes from guest language features through Emscripten and into the host, then separately assess host permissions. This is more rigorous than inferring security from the mere presence of WebAssembly.

### Writing to Shadow Stacks

The sole-authored shadow-stack talk is the most mitigation-focused and technically low-level record. It presents three families of techniques for placing chosen data in shadow-stack memory without simply turning CET off [record_id:2911]. The breadth matters: one route exploits forced kernel memory access, another manipulates page-fault-backed population, and a third uses a CPU instruction designed for shadow-stack writes.

The record also describes both corrective action and residual exposure. A Linux commit was merged to restrict the initial `/proc/self/mem` path, but the `fork`/`ptrace` variant allegedly survives, and the `userfaultfd` method is outside that patch’s scope [record_id:2911]. The claim that no distribution yet shipped the new default is time-sensitive and should be treated as reflecting the talk description’s 2026 context, not a durable statement about current deployment.

The bare-metal validation against dnsmasq, libinput, and rsync vulnerabilities, including a claimed root shell with CET enabled, is the talk’s most important evidence [record_id:2911]. Its unique technical contribution is the combination of multiple shadow-stack write channels with a correction to the machine-code encoding used by prior `WRSSQ` proof-of-concept work.

## Gaps, Limits, And Open Questions

The corpus is narrow: three abstracts from the same conference and year. It provides no earlier or later work from Tokarev, no biography, and no basis for determining whether these subjects represent a long-term specialization or an unusually concentrated DEF CON 34 program. Authorship is also collaborative in two of the three records, so the source text does not permit reliable attribution of individual discoveries or techniques between Tokarev and his co-authors [record_id:2858] [record_id:2878].

The records make substantial technical claims but do not include exploit code, patches, presentation slides, disclosure timelines, affected-version ranges, or independent reproductions. The two Pyodide CVEs and the cited Linux commit are externally identifiable anchors, but the abstracts alone do not establish the full scope, severity, or present patch status of every reported issue [record_id:2878] [record_id:2911]. The llama.cpp and Ollama record does not identify CVE numbers or describe vendor remediation [record_id:2858].

Several technical questions remain open:

- What exact scheduling, heap-shaping, and allocator conditions are necessary to make the llama.cpp server dangling pointer into stable remote code execution? The record only claims an attacker-controlled dereference and says further steps remain [record_id:2858].
- Which Ollama versions and quantization paths accept the malicious GGUF metadata, how much heap data can be disclosed, and what controls the repeatability or contents of the leak [record_id:2858]?
- Across the seven claimed Pyodide escapes, which findings are distinct architectural patterns and which are repeated instances of the same exposed bridge [record_id:2878]?
- What hardening measures are sufficient beyond denylists—removal of foreign-function interfaces, capability-based host APIs, separate-process isolation, Deno permissions, OS sandboxing, or some combination [record_id:2878]?
- Under what kernel configurations and privilege restrictions are `userfaultfd`, `/proc/self/mem`, and `ptrace` available to an attacker? The abstract does not map the techniques across distributions, containers, hardening profiles, or production defaults [record_id:2911].
- Does the ability to write selected shadow-stack values generalize cleanly to contemporary vulnerabilities beyond the three cited CVEs, and what additional primitives are required for reliable code reuse under CET or GCS [record_id:2911]?
- How have patches, distribution defaults, and product configurations changed since the 2026 descriptions? This is especially important for the time-sensitive claim that distributions had not yet shipped the new shadow-stack-related default [record_id:2911].

There is also a distinction between demonstrating that a security boundary can be crossed and establishing the final impact. The Pyodide record acknowledges this by making Deno impact permission-dependent [record_id:2878]. The AI record similarly differentiates complete code execution from incomplete primitives [record_id:2858]. Future research should preserve these distinctions and avoid treating every boundary failure as automatically equivalent to unauthenticated remote code execution.

## Coverage And Evidence Notes

All three expected records are substantively relevant and none is merely logistical.

The llama.cpp and Ollama talk covers native exploitation in local AI runtimes, including an Android use-after-free exploit, a server-side dangling-pointer primitive, and a Go/C out-of-bounds disclosure issue [record_id:2858]. It is the corpus’s main evidence for AI infrastructure, JNI, concurrency, model lifecycle, GGUF metadata, and cross-language memory-safety research.

The Pyodide talk covers WebAssembly sandbox assumptions, CPython/Emscripten host integration, escape through `ctypes` or reflection, Node.js and Deno post-escape impact, and CI or software supply-chain consequences [record_id:2878]. Its public CVE references provide the clearest externally named vulnerability evidence, although the record itself remains an abstract rather than a full advisory or technical report.

The shadow-stack talk covers Linux kernel paths and CPU mechanisms that reportedly permit writes to CET or GCS shadow stacks, along with a kernel response, surviving variants, a corrected `WRSSQ` encoding, and exploitation demonstrations against three known vulnerabilities [record_id:2911]. It is the strongest record for mitigation bypass and low-level kernel/architecture research.

Evidence strength is therefore best characterized as technically detailed but source-limited. The descriptions include precise allocation sizes, APIs, instructions, CVE identifiers, a kernel commit, host-runtime distinctions, and stated exploit outcomes, which makes them richer than generic talk announcements. Nevertheless, all claims remain claims in conference record text until corroborated through slides, code, advisories, patches, or independent testing.