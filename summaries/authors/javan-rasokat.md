# Topic: Author: Javan Rasokat

## Executive Summary

The two records attributed to Javan Rasokat are both BSidesLV 2025 sessions focused on a single, coherent security thesis: traditional application security practices—bug bounties, vulnerability reports, developer education, “shifting left,” and repeated patching—do not scale well enough to prevent recurring web vulnerability classes. Rasokat’s proposed alternative is to use modern browser-native security mechanisms to eliminate or substantially reduce entire classes of bugs at organizational scale, particularly XSS and related cross-origin or client-side attack classes [record_id:2433], [record_id:2580].

Both records emphasize proactive defense over reactive remediation. They highlight Content-Security-Policy v3, Trusted Types, and Sec-Fetch-Metadata as core browser features that can be integrated, automated, monitored, and enforced across many services [record_id:2433], [record_id:2580]. The shorter talk frames this as “XSS is dead” and positions browser features as a way to “automate, scale, and forget entire bug classes” [record_id:2580]. The longer workshop expands the same premise into a hands-on training format, promising practical exercises with a training application, group challenges, adoption measurement, and enforcement at scale [record_id:2433].

The evidence base is narrow but internally consistent. The records do not provide the actual slide content, technical implementation details, source code, case study names, or empirical results. However, they clearly establish Rasokat’s recurring contribution in this dataset: advocating for browser-enforced, secure-by-design web application defenses as a scalable replacement or supplement for conventional vulnerability-by-vulnerability patching.

## Research Landscape

The corpus consists of two BSidesLV 2025 records, both attributed to Javan Rasokat and both centered on application security. One is a 20-minute talk, “XSS is dead - Browser Security Features that Eliminate Bug Classes,” scheduled in the Ground Floor / Florentine E track [record_id:2580]. The other is a longer hands-on workshop, “Eliminating Bug Classes at Scale: Leveraging Browser Features for Proactive Defense,” scheduled in the Training Ground / Diamond track for a four-hour block [record_id:2433].

The records therefore represent conference programming rather than long-form written research papers, blog posts, tool releases, or formal technical specifications. They appear to be closely related, likely covering overlapping material in different formats: one as a concise conceptual and case-study-driven presentation, the other as an interactive workshop focused on applying the same browser security mechanisms in practice [record_id:2433], [record_id:2580].

The overall research area is modern web application defense using browser-native controls. The records situate this work against common application security processes that are described as insufficiently scalable: “bug bounties, vulnerability reports, and endless patching” [record_id:2580], along with “firefighting the same issues” [record_id:2433]. The browser is treated not merely as an execution environment but as a security enforcement layer capable of preventing vulnerabilities before they are exploitable. In both records, the relevant mechanisms are opt-in standards and headers that organizations can deploy centrally or systematically: Content-Security-Policy v3, Trusted Types, and Sec-Fetch-Metadata [record_id:2433], [record_id:2580].

The source landscape is thin but focused. There are no dissenting records, no unrelated talks, and no evidence of a broader portfolio in this dataset beyond this browser-security theme. As a result, the best-supported conclusion is not that Rasokat’s full body of work is limited to browser security, but that the records available here portray him as presenting on scalable web application defense through browser features.

## Major Themes And Trends

### From reactive patching to proactive prevention

The dominant theme across both records is dissatisfaction with reactive application security. The shorter talk explicitly says “traditional application security is broken” and describes organizations as trapped in “a cycle of bug bounties, vulnerability reports, and endless patching” [record_id:2580]. The workshop similarly begins from the premise that “traditional patching has failed to scale” and argues that it is “time for a new approach” [record_id:2433].

This framing matters because Rasokat’s records are not primarily about finding individual bugs or improving one specific patching workflow. Instead, they advocate a shift in security strategy: rather than repairing individual instances of XSS, CSRF, clickjacking, or cross-origin vulnerabilities after discovery, organizations should deploy mechanisms that prevent whole categories of attacks from working in the first place [record_id:2580]. The workshop makes the same point by contrasting “fixing issues” with “scaling security across an organization” [record_id:2433].

### Eliminating bug classes rather than fixing instances

A second recurring theme is the concept of “bug classes.” Both titles use the phrase “eliminate bug classes,” and the raw texts repeatedly contrast class-level prevention with issue-by-issue remediation [record_id:2433], [record_id:2580]. This moves the discussion from vulnerability management as a queue of tickets to security architecture as a set of systemic guardrails.

The talk claims that browser-native protections can “systematically prevent issues like XSS, CSRF, clickjacking, and cross-origin attacks” [record_id:2580]. The workshop emphasizes XSS “among others” and says participants will tackle XSS vulnerabilities “but not as you are used to it,” suggesting the goal is not traditional exploit-and-fix training but learning how to make classes of exploit patterns nonviable through platform controls [record_id:2433].

### Browser security features as scalable enforcement mechanisms

Both records identify the same technical mechanisms: Content-Security-Policy v3, Trusted Types, and Sec-Fetch-Metadata [record_id:2433], [record_id:2580]. The repeated trio indicates that these are central to Rasokat’s BSidesLV 2025 material.

The records present these features as “modern browser security features” and “browser-native protections” that can be used to automate and scale security [record_id:2580]. In this framing, the browser provides enforcement that does not rely solely on each developer remembering and correctly applying every secure coding best practice. The talk makes that explicit by saying these features can remove vulnerabilities “without relying solely on developers remembering best practices” [record_id:2580].

The workshop extends this into operational scale: it discusses “measuring adoption across hundreds of services,” “automating enforcement,” and “applying defense-in-depth beyond single vulnerabilities” [record_id:2433]. This suggests a trend from single-application hardening toward fleet-wide governance of browser-enforced controls.

### Secure defaults, automation, and organizational adoption

Both records stress automation and adoption measurement. The talk promises to cover “practical ways to integrate these features, automate security headers, enforce secure defaults, and measure adoption effectively” [record_id:2580]. The workshop similarly promises instruction on “monitoring their effectiveness,” “enforcing it at scale,” and “measuring adoption across hundreds of services” [record_id:2433].

This is significant because it frames the problem as socio-technical rather than purely technical. The records do not simply say “enable CSP” or “use Trusted Types.” They emphasize rollout, measurement, enforcement, and scaling across many teams or services. Rasokat’s distinctive contribution in these records appears to be tying browser security controls to organizational security operations: adoption tracking, automated enforcement, and secure defaults that reduce reliance on individual developer behavior [record_id:2433], [record_id:2580].

### Education through both lecture and hands-on practice

The two records also show a pedagogical split. The shorter talk appears designed to persuade and orient developers or security engineers through examples and “real-world case studies” [record_id:2580]. The longer workshop is explicitly “hands-on” and uses “interactive group challenges” with a training application [record_id:2433].

This dual format suggests that the topic is intended both as an argument and as a practical training path. The talk introduces the strategic case for browser-native elimination of bug classes; the workshop gives participants a chance to apply those ideas in a guided environment [record_id:2433], [record_id:2580].

## Methods, Tools, And Approaches Discussed

The records discuss several browser security mechanisms and organizational approaches, although they do so at an abstract conference-description level rather than with implementation detail.

Content-Security-Policy v3 is the most prominent mechanism, appearing in both records [record_id:2433], [record_id:2580]. CSP is presented as a browser feature that can go “beyond traditional recommendations” and help prevent vulnerabilities at scale [record_id:2433]. The records do not specify the exact directives, rollout sequence, nonce/hash strategy, reporting configuration, or bypass considerations, but CSP is clearly part of Rasokat’s recommended platform-level defense model.

Trusted Types is also named in both records as a key modern browser defense [record_id:2433], [record_id:2580]. Its inclusion is especially relevant to XSS prevention, because Trusted Types is designed to constrain dangerous DOM injection sinks. The records do not describe specific policies, migration workflows, framework integration, or compatibility constraints, but they position Trusted Types as one of the “powerful opt-in mechanisms” that can help prevent recurring client-side vulnerabilities [record_id:2580].

Sec-Fetch-Metadata is the third recurring mechanism [record_id:2433], [record_id:2580]. The talk associates browser-native protections including Sec-Fetch-Metadata with prevention of “CSRF, clickjacking, and cross-origin attacks” [record_id:2580]. The workshop includes it in the list of advanced browser defenses used to go beyond standard recommendations [record_id:2433]. The records do not describe policy logic, server-side request handling, fallback behavior, or deployment caveats, but they clearly treat Fetch Metadata request headers as part of a scalable defensive architecture.

Beyond individual mechanisms, the records discuss a set of operational approaches:

- Applying advanced browser defenses to both “new and legacy systems,” rather than limiting adoption to greenfield applications [record_id:2433].
- Monitoring effectiveness after deployment, implying some use of telemetry, reporting, or measurement processes [record_id:2433].
- Measuring adoption across “hundreds of services,” suggesting large-organization rollout patterns and service inventory concerns [record_id:2433].
- Automating security headers and enforcement, reducing the burden on individual application teams [record_id:2580].
- Enforcing secure defaults, which indicates a platform or governance approach where secure configurations are built into shared infrastructure or deployment pipelines [record_id:2580].
- Using defense-in-depth “beyond single vulnerabilities,” meaning these mechanisms are presented as layered controls rather than isolated fixes [record_id:2433].

The workshop record also describes a “training app that’s already secured” but says participants will “go further” by applying advanced browser defenses, monitoring effectiveness, and enforcing them at scale [record_id:2433]. This suggests a teaching method where learners start from a baseline-secured application and then explore additional hardening layers, rather than only patching intentionally vulnerable code.

The talk record mentions “real-world case studies” involving “leading organizations” that have used browser-native protections to eliminate vulnerabilities at scale [record_id:2580]. However, the raw record text does not name those organizations or summarize the case studies. Downstream agents should treat the existence of case studies as a claim in the abstract, not as independently evidenced results.

## Notable Talks, Records, And Evidence

The most representative record is the 20-minute BSidesLV 2025 talk, “XSS is dead - Browser Security Features that Eliminate Bug Classes” [record_id:2580]. It provides the clearest statement of Rasokat’s argument: traditional application security is stuck in repeated patching, and browser-native controls can automate and scale defense against XSS, CSRF, clickjacking, and cross-origin attacks [record_id:2580]. It is also the only record that explicitly mentions “real-world case studies” and “leading organizations,” although without naming them or providing details in the available text [record_id:2580]. For downstream researchers trying to understand Rasokat’s thesis, this record is the concise conceptual anchor.

The longer and more operationally detailed record is the BSidesLV 2025 workshop, “Eliminating Bug Classes at Scale: Leveraging Browser Features for Proactive Defense” [record_id:2433]. It matters because it translates the same thesis into a hands-on training format. The workshop promises practical work with CSP v3, Trusted Types, and Sec-Fetch-Metadata; exercises using a training app; monitoring of defense effectiveness; enforcement at scale; and adoption measurement across hundreds of services [record_id:2433]. It also identifies its audience broadly: developers, security engineers, and architects [record_id:2433]. This indicates that Rasokat’s material is not aimed solely at exploit developers or AppSec specialists, but at practitioners responsible for building and operating secure web systems.

Together, the two records strongly support a characterization of Rasokat’s BSidesLV 2025 contribution as advocating for class-level web vulnerability prevention through browser features. The overlap between the talk and workshop reinforces the centrality of this theme. The talk supplies the motivating narrative and high-level case for the approach [record_id:2580], while the workshop supplies the practical, training-oriented extension [record_id:2433].

## Gaps, Limits, And Open Questions

The main limitation is that the dataset contains only two records, both from the same event year and likely the same conference program. This makes the evidence strong for summarizing Rasokat’s BSidesLV 2025 topic, but weak for describing his broader career, publication history, tool development, or long-term evolution as a speaker.

Several technical gaps remain:

- The records name Content-Security-Policy v3, Trusted Types, and Sec-Fetch-Metadata, but do not provide implementation examples, deployment checklists, configuration patterns, code samples, or recommended policies [record_id:2433], [record_id:2580].
- The records claim these features can eliminate or prevent classes such as XSS, CSRF, clickjacking, and cross-origin attacks, but do not provide empirical metrics, before-and-after