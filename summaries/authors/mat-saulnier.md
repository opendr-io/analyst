# Topic: Author: Mat Saulnier

## Executive Summary

The available corpus for “Author: Mat Saulnier” contains two BSidesLV 2025 talk records attributed to Mat Saulnier. Together, they show a speaker working across two different but security-adjacent domains: password security in Active Directory and PHP application exploitation. One record is a solo talk on password auditing/cracking framed through compliance and adversary scenarios in organizations [record_id:2501]. The other is a co-authored technical exploitation presentation with Hiroki Matsukuma on bypassing PHP `__wakeup()` mitigations for PHP Object Injection using an Arbitrary Object Instantiation primitive [record_id:2567].

The evidence base is small but diverse. The records do not provide full slide decks, papers, transcripts, or implementation details beyond abstracts. Still, they suggest recurring concerns around practical offensive security, realistic attack paths, and the limitations of defensive controls when implemented narrowly. In the Active Directory talk, the emphasis appears to be on password-related attack scenarios and how organizations with different security maturity levels fare against a criminal group [record_id:2501]. In the PHP exploitation talk, the emphasis is on reviving supposedly mitigated exploit chains by shifting execution outside the specific protected path where `__wakeup()` would run [record_id:2567].

A downstream researcher should treat these records as evidence of Mat Saulnier’s BSidesLV 2025 speaking activity rather than as a complete profile of his research career. The strongest evidence is for two specific presentations and their advertised topics. Broader conclusions about Saulnier’s research agenda should remain tentative.

## Research Landscape

The topic consists of two BSidesLV 2025 records. Both are conference-talk abstracts, not long-form technical papers. They are concise descriptions of planned presentations, including title, event, track-like tags, authorship, and short abstract text.

The first record, “Password ~Audit~ Cracking in AD: The Fun Part of Compliance,” is a BSidesLV 2025 talk authored by Mat Saulnier. It is tagged with PasswordsCon and scheduled in the Tuscany room on Wednesday from 10:00–10:45 [record_id:2501]. Its raw abstract describes “the story of three organizations”: EvilCats, a criminal group; YOLO Corp, “a new company that don't have any security staff”; and CoolSec, “a company that goes above security compliance.” The talk promises to show how two corporations “fret against EvilCats during various attack scenarios that all involve passwords” [record_id:2501]. The record classifies the talk secondarily under governance, risk, and compliance, while its primary metadata topic is identity, OAuth, and access delegation. The raw abstract itself is more specifically about passwords, Active Directory, compliance, and attack scenarios.

The second record, “Unawakened Wakeup: A Novel PHP Object Injection Technique to Bypass __wakeup(),” is a BSidesLV 2025 talk co-authored by Mat Saulnier and Hiroki Matsukuma. It is tagged with Proving Ground and scheduled in the Firenze room on Tuesday from 14:30–14:55 [record_id:2567]. Its abstract is more technically detailed than the password-auditing record. It discusses PHP Object Injection, Property-oriented Programming gadgets, mitigation through `__wakeup()` methods that throw exceptions, and a bypass based on an Arbitrary Object Instantiation primitive [record_id:2567]. It also claims a live demo revives the retired Guzzle/RCE1 chain of PHPGGC and obtains remote code execution on a default Neos Flow installation [record_id:2567].

The overall research landscape, based only on these two records, is therefore mixed: one presentation appears to be scenario-driven and compliance-oriented, while the other is deeply exploit-development oriented. Both are practical security talks rather than policy essays or purely theoretical work.

## Major Themes And Trends

### Practical offensive security as a teaching frame

Both records describe security through attack scenarios. The Active Directory/password talk explicitly frames its content as a story involving a criminal group, EvilCats, and two organizations with different levels of security preparedness: YOLO Corp and CoolSec [record_id:2501]. This narrative structure suggests a pedagogical style that uses adversary scenarios to explain why password controls, auditing, or cracking matter in practice.

The PHP talk similarly focuses on bypassing an existing mitigation and demonstrating exploitation. It describes how some PHP libraries add a `__wakeup()` method that throws an exception in classes that could serve as Property-oriented Programming gadgets, and then introduces a technique to bypass that protection [record_id:2567]. The talk’s advertised demo—reviving a retired PHPGGC chain and achieving remote code execution—also places the work firmly in an applied offensive-security context [record_id:2567].

### Defensive controls that appear sufficient but may be incomplete

A recurring concern across the two records is the gap between formal or nominal controls and real-world attack resistance. In the password talk, this appears through the contrast between a company with no security staff, a company that “goes above security compliance,” and a criminal group attacking through password-related scenarios [record_id:2501]. The title itself, “Password ~Audit~ Cracking in AD: The Fun Part of Compliance,” suggests that compliance-driven password auditing may involve or benefit from password cracking, and that merely satisfying compliance may not be enough [record_id:2501].

The PHP talk makes this theme more explicit at the technical level. It says some PHP libraries mitigate PHP Object Injection by adding `__wakeup()` methods that throw exceptions in potentially dangerous gadget classes, “eliminating them in one stroke” [record_id:2567]. The proposed bypass undermines this assumption by triggering dynamic class instantiation “entirely outside the process of `unserialize()`,” so the guarding `__wakeup()` “never runs” [record_id:2567]. This is a clear example of a defense that works only within a particular execution path and can be avoided by changing the exploitation route.

### Security maturity and organizational contrast

The password talk uses organizational archetypes to highlight differences in security maturity. YOLO Corp is described as “a new company that don't have any security staff,” while CoolSec is described as “a company that goes above security compliance” [record_id:2501]. EvilCats, the criminal group, acts as the adversarial pressure against which these organizations are evaluated [record_id:2501]. This framing suggests the talk is likely concerned not only with technical password cracking but also with how organizational capacity and compliance posture affect resilience.

There is no equivalent organizational maturity framing in the PHP Object Injection record. That talk is focused on libraries, language behavior, exploit chains, and remediation advice for pentesters and developers [record_id:2567]. However, the developer takeaways—“migrating to JSON or adding HMAC-protected serialization”—do imply that secure engineering choices and defensive architecture matter [record_id:2567].

### Reviving or reinterpreting known attack paths

The second record’s most distinctive theme is the resurrection of previously “dead” or retired exploit chains. It says the technique can “revive” the retired Guzzle/RCE1 chain of PHPGGC and gain remote code execution on a default Neos Flow installation [record_id:2567]. The abstract frames this as a broader lesson for pentesters: “learn how to resurrect ‘dead’ chains and locate AOI primitives” [record_id:2567].

This theme is less explicit in the password talk, but the title’s correction-like styling—“Password ~Audit~ Cracking”—suggests a reinterpretation of password auditing as password cracking in the context of Active Directory and compliance [record_id:2501]. In both cases, the records point toward a practical security mindset that revisits familiar controls or familiar attack chains and asks whether they remain exploitable under altered assumptions.

## Methods, Tools, And Approaches Discussed

The Active Directory/password record provides limited methodological detail, but its title and abstract indicate a scenario-based treatment of password auditing and cracking in AD environments [record_id:2501]. The talk appears to use fictional entities—EvilCats, YOLO Corp, and CoolSec—to compare how organizations respond to password-related attack scenarios [record_id:2501]. The methodological approach is likely educational simulation or narrative case study rather than a single tool release, though the record does not specify tools, datasets, cracking rigs, password audit procedures, or AD configurations.

The PHP exploitation record is much more explicit about techniques and tools. It discusses PHP Object Injection, `unserialize()`, `__wakeup()`, Property-oriented Programming gadgets, and an Arbitrary Object Instantiation primitive [record_id:2567]. The central method is to trigger dynamic class instantiation outside the `unserialize()` process so that the protective `__wakeup()` method is not invoked [record_id:2567]. According to the abstract, the only prerequisite is a POP gadget that executes `new $className(...)` [record_id:2567]. This reframes exploitation around finding AOI primitives rather than depending on interpreter bugs.

The same record also names PHPGGC, the Guzzle/RCE1 chain, and Neos Flow. The talk claims to revive the retired Guzzle/RCE1 chain of PHPGGC and achieve remote code execution on a default Neos Flow installation [record_id:2567]. The practical defensive recommendations listed in the abstract are to migrate to JSON or add HMAC-protected serialization [record_id:2567]. These defenses indicate an emphasis on avoiding unsafe native serialization paths or ensuring serialized data integrity.

A notable methodological contrast exists between the two records. The password talk appears designed around compliance and organizational attack scenarios [record_id:2501], while the PHP talk presents a precise exploit-development contribution with a named primitive, prerequisite conditions, expected durability against future patches, and a live demonstration [record_id:2567].

## Notable Talks, Records, And Evidence

The most technically detailed record is “Unawakened Wakeup: A Novel PHP Object Injection Technique to Bypass __wakeup()” [record_id:2567]. It matters because it identifies a specific bypass technique against a known mitigation pattern in PHP Object Injection. The abstract explains the mitigation: adding `__wakeup()` methods that throw exceptions in classes that could serve as POP gadgets [record_id:2567]. It then describes the bypass: using an Arbitrary Object Instantiation primitive to instantiate objects outside `unserialize()`, preventing the guard from running [record_id:2567]. The record also makes a strong claim of practical impact through a live demo that revives the retired Guzzle/RCE1 PHPGGC chain and gains RCE on default Neos Flow [record_id:2567]. Among the two records, this provides the clearest evidence of a unique technical contribution.

“Password ~Audit~ Cracking in AD: The Fun Part of Compliance” is notable for representing Saulnier’s work in password security, Active Directory, and compliance-driven security practice [record_id:2501]. The abstract is brief and stylized, but it indicates that the talk uses a comparative story involving a criminal group and two organizations with different security postures [record_id:2501]. Its importance lies in showing a separate area of engagement from PHP exploitation: enterprise identity and password risk. The title suggests the talk may challenge sanitized notions of password “auditing” by emphasizing cracking as a necessary or revealing part of compliance-oriented assessment [record_id:2501].

Taken together, the records show Mat Saulnier associated with both enterprise security education and advanced application exploitation at the same 2025 conference. The corpus does not establish whether these are isolated talks or part of a larger body of work, but it does show breadth across identity/password security and web application exploit research [record_id:2501] [record_id:2567].

## Gaps, Limits, And Open Questions

The largest limitation is corpus size. There are only two records, both from BSidesLV 2025. This is enough to summarize the included talks but not enough to characterize Mat Saulnier’s full research trajectory, publication history, employer context, tool authorship, or long-term thematic evolution.

The password-auditing record is especially thin. It does not state which Active Directory attack paths are covered, which password-cracking tools or techniques are used, what compliance frameworks are discussed, or how YOLO Corp and CoolSec differ in specific controls [record_id:2501]. It also does not specify whether the talk is primarily instructional, comedic, case-study based, or tool-driven. Downstream researchers interested in password audit methodology would need slides, a recording, or related materials.

The PHP Object Injection record is richer but still an abstract. It does not provide proof details, code, affected library versions, exact exploit-chain mechanics, or the boundaries of the Arbitrary Object Instantiation primitive [record_id:2567]. The claim that the technique relies “solely on core language behavior” and that future patches are “unlikely to break it” is important, but the record alone does not allow independent verification [record_id:2567]. Researchers should seek the talk recording, slides, proof-of-concept code, PHPGGC updates, Neos Flow issue history, or coordinated disclosure notes if available.

Open questions include:

- What specific AD password attack scenarios were demonstrated or discussed in the compliance talk [record_id:2501]?
- Did the password talk recommend particular cracking workflows, audit cadences, or controls for organizations trying to exceed compliance [record_id:2501]?
- How general is the AOI-based `__wakeup()` bypass across PHP libraries and frameworks [record_id:2567]?
- What exact patterns should developers search for to identify POP gadgets that execute `new $className(...)` [record_id:2567]?
- Were any new tools, PHPGGC chains, patches, or defensive checklists released alongside the PHP talk [record_id:2567]?
- How do the two talks relate, if at all, beyond shared authorship and practical offensive-security framing?

## Coverage And Evidence Notes

This report covers both records provided for the topic.

Record [record_id:2501] is a BSidesLV 2025 talk titled “Password ~Audit~ Cracking in AD: The Fun Part of Compliance,” authored by Mat Saulnier. Its raw text describes a story involving EvilCats, YOLO Corp