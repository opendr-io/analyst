#!/usr/bin/env python3
"""Build the explicit, human-readable summary-routing smoke-test cases."""

from __future__ import annotations

import json
from pathlib import Path

APP_DIR = Path(__file__).resolve().parents[1]
OUTPUT_PATH = APP_DIR / "config" / "summary_routing_smoke.json"


# Each entry deliberately uses routing language that is less direct than the
# canonical topic title. The final two fields are plausible distractors used
# by cross-topic cases.
TOPIC_CUES: dict[str, tuple[list[str], str, str]] = {
    "malware-analysis-and-reverse-engineering": (
        ["unpacking a suspicious executable", "recovering behavior from firmware", "extracting indicators from a binary", "dynamic analysis in a sandbox", "understanding an obfuscated payload"],
        "patch prioritization",
        "endpoint alert tuning",
    ),
    "exploit-development-and-vulnerability-discovery": (
        ["turning a memory corruption bug into code execution", "building a proof of concept for a privilege boundary bypass", "finding a new attack surface", "validating whether a crash is exploitable", "chaining weaknesses into remote compromise"],
        "routine patch operations",
        "secure coding guidance",
    ),
    "vulnerability-management-and-intelligence": (
        ["deciding which exposed CVEs to fix first", "combining KEV and EPSS with asset context", "moving findings through remediation", "measuring exploitability instead of severity alone", "reducing a scanner backlog"],
        "writing a new exploit",
        "reverse engineering malware",
    ),
    "identity-oauth-and-access-delegation": (
        ["abusing a delegated token", "designing passkey and MFA flows", "service-to-service authorization", "confused-deputy failures in OAuth", "controlling who can act on whose behalf"],
        "network packet inspection",
        "source code generation",
    ),
    "application-security": (
        ["testing an API for broken access control", "finding flaws in a web application", "reviewing code for injection paths", "hardening an authentication flow", "preventing app-layer authorization mistakes"],
        "cloud posture management",
        "malware sandboxing",
    ),
    "threat-modeling": (
        ["finding abuse paths before code is written", "using attack trees during architecture review", "mapping trust boundaries and misuse cases", "applying STRIDE to a proposed design", "challenging security assumptions before implementation"],
        "production alert triage",
        "post-incident forensics",
    ),
    "cloud-infrastructure-and-cdr": (
        ["investigating suspicious Kubernetes activity", "securing infrastructure as code", "using cloud telemetry for response", "finding risky container configuration", "operating detection across cloud control planes"],
        "desktop endpoint telemetry",
        "application source review",
    ),
    "ot-and-iot-security": (
        ["testing an industrial protocol", "analyzing firmware from a connected appliance", "protecting a SCADA environment", "finding weaknesses in an embedded controller", "defending cyber-physical operations"],
        "enterprise OAuth",
        "software package signing",
    ),
    "detection-engineering-soc-siem-and-threat-hunting": (
        ["turning telemetry into reliable alerts", "reducing noisy SIEM detections", "hunting across event data", "validating whether a detection catches an attack", "improving analyst triage in the SOC"],
        "writing exploit code",
        "governance audits",
    ),
    "ai-security-prompt-injection-and-jailbreaking": (
        ["stopping untrusted instructions from taking over an agent", "testing jailbreak resistance", "red teaming an LLM application", "preventing malicious tool use by an assistant", "defending against indirect prompt injection"],
        "general prompt-writing lessons",
        "model serving performance",
    ),
    "rag-and-graphrag-security": (
        ["poisoning documents retrieved by an assistant", "enforcing permissions during vector search", "preventing knowledge-graph leakage", "securing a retrieval pipeline", "isolating tenants in a grounded chatbot"],
        "training-time model robustness",
        "ordinary database tuning",
    ),
    "software-supply-chain-security": (
        ["detecting a malicious dependency", "protecting a CI build from tampering", "using an SBOM during incident response", "securing package publication", "verifying provenance and signatures"],
        "network intrusion detection",
        "employee phishing awareness",
    ),
    "privacy-and-data-leakage": (
        ["testing whether a model memorized private records", "preventing unintended disclosure", "measuring deanonymization risk", "designing privacy-preserving data use", "finding sensitive information leakage"],
        "egress policy enforcement",
        "vulnerability patching",
    ),
    "machine-learning-model-security": (
        ["extracting a model through repeated queries", "testing adversarial examples", "finding a backdoor in training data", "hardening model deserialization", "evaluating robustness against model inversion"],
        "prompt injection in an agent",
        "GPU capacity planning",
    ),
    "data-loss-detection-and-prevention": (
        ["detecting secrets leaving the company", "classifying sensitive files before egress", "investigating insider data movement", "blocking uploads of regulated data", "tuning controls for exfiltration"],
        "privacy-preserving analytics",
        "malware reverse engineering",
    ),
    "governance-risk-and-compliance": (
        ["mapping controls to a regulatory obligation", "assessing third-party security risk", "preparing evidence for an audit", "setting responsible AI policy", "measuring enterprise risk against a framework"],
        "writing detection rules",
        "exploit validation",
    ),
    "network-security-and-ndr": (
        ["finding attacks in DNS traffic", "analyzing packets for tunneling", "using Zeek or Suricata telemetry", "detecting suspicious BGP behavior", "investigating lateral movement on the wire"],
        "host process injection",
        "application code review",
    ),
    "endpoint-security-and-edr": (
        ["detecting process injection on Windows", "using Sysmon and ETW for investigation", "analyzing a suspicious kernel driver", "hunting with host telemetry", "improving EDR coverage across desktops"],
        "packet-level monitoring",
        "cloud control-plane posture",
    ),
    "ai-applications-agents-and-workflow-automation": (
        ["building an assistant that completes business tasks", "orchestrating tools with an LLM", "automating document summarization", "using agents for domain workflows", "designing practical non-security AI automation"],
        "jailbreak testing",
        "model training infrastructure",
    ),
    "ai-infrastructure-data-engineering-and-model-systems": (
        ["routing requests across model servers", "building data pipelines for AI applications", "managing long-term context and memory", "engineering GPU-backed inference systems", "designing retrieval and knowledge-graph infrastructure"],
        "prompt-writing education",
        "AI coding assistants",
    ),
    "ai-assisted-software-development-and-developer-tooling": (
        ["using a coding agent to change a repository", "generating tests from requirements", "reviewing code with an LLM", "improving developer workflows with AI", "automating software maintenance"],
        "general business automation",
        "model serving infrastructure",
    ),
    "blockchain-and-cryptocurrency-security": (
        ["auditing a smart contract", "tracing stolen cryptocurrency", "protecting wallet keys", "finding protocol flaws in decentralized finance", "investigating exchange fraud"],
        "traditional payment-card fraud",
        "post-quantum migration",
    ),
    "censorship-circumvention-and-resilient-communications": (
        ["keeping communications available during an internet shutdown", "evading state network blocking", "building surveillance-resistant coordination tools", "preserving access to information under censorship", "making messaging resilient on hostile networks"],
        "enterprise firewall tuning",
        "ordinary disaster recovery",
    ),
    "cryptography-key-management-and-post-quantum-security": (
        ["planning migration away from vulnerable public-key algorithms", "operating keys inside an HSM", "designing cryptographic agility", "managing the lifecycle of signing keys", "deploying post-quantum protocols"],
        "cryptocurrency wallet fraud",
        "passwordless identity flows",
    ),
    "cyberbiosecurity-and-biotechnology-security": (
        ["securing automated laboratory workflows", "assessing abuse of AI-designed biology", "protecting bioinformatics pipelines", "threat modeling molecular engineering systems", "managing cyber risk in biotechnology"],
        "hospital endpoint operations",
        "general machine learning",
    ),
    "cybercrime-fraud-and-social-engineering": (
        ["disrupting an online scam operation", "studying how criminals monetize stolen accounts", "preventing social-engineering fraud", "mapping a darknet marketplace", "understanding victim targeting by fraud crews"],
        "nation-state attribution",
        "application penetration testing",
    ),
    "cybersecurity-market-and-vendor-strategy": (
        ["comparing security vendors for buyers", "analyzing product positioning in the security market", "studying investment trends in cyber companies", "understanding buyer behavior for security tools", "planning a vendor go-to-market strategy"],
        "technical product testing",
        "enterprise control audits",
    ),
    "digital-forensics-preservation-and-cyber-history": (
        ["recovering evidence from an old computing artifact", "preserving a disappearing security website", "researching the history of hacker communities", "archiving material for future forensic study", "reconstructing events from legacy digital media"],
        "live SOC alert handling",
        "current threat attribution",
    ),
    "election-security": (
        ["verifying that a voting system produced the right outcome", "testing ballot-marking devices", "securing election infrastructure", "evaluating risks in internet voting", "building public trust through auditable elections"],
        "general government compliance",
        "campaign disinformation analysis",
    ),
    "general-ai-education-and-prompt-engineering": (
        ["teaching staff how to write useful prompts", "building an introductory LLM course", "improving everyday model usage", "creating AI literacy training", "explaining prompt patterns to non-specialists"],
        "prompt injection defense",
        "model infrastructure engineering",
    ),
    "general-technology-productivity-and-non-security-applications": (
        ["using technology to improve a non-security business process", "applying software to health or education", "studying general productivity tools", "preserving software with no clear security angle", "finding technical work outside the security taxonomy"],
        "security operations",
        "AI red teaming",
    ),
    "hardware-rf-and-physical-security": (
        ["cloning a building access badge", "experimenting with software-defined radio", "testing covert entry techniques", "hacking a conference hardware badge", "finding weaknesses in physical access systems"],
        "wireless network monitoring",
        "embedded firmware analysis",
    ),
    "professional-development-workforce-and-hiring": (
        ["improving technical interview practices", "reducing burnout in a security team", "building a mentoring program", "expanding access to cybersecurity careers", "developing workforce skills and resilience"],
        "conference event planning",
        "security market analysis",
    ),
    "security-education-community-and-conference-operations": (
        ["running a security conference", "designing a community CTF", "organizing training for practitioners", "documenting conference culture and events", "planning non-research security programming"],
        "individual career coaching",
        "technical vulnerability research",
    ),
    "threat-intelligence-and-adversary-tracking": (
        ["tracking a campaign across multiple intrusions", "attributing activity to an adversary group", "using OSINT to investigate a threat actor", "mapping geopolitical cyber operations", "disrupting hacktivist or criminal infrastructure"],
        "SOC alert tuning",
        "consumer scam prevention",
    ),
}


def build_cases() -> list[dict[str, str]]:
    cases: list[dict[str, str]] = []
    for slug, (cues, distractor_a, distractor_b) in TOPIC_CUES.items():
        questions = [
            ("short", f"{cues[0]}?"),
            ("short", f"Need material on {cues[1]}."),
            ("indirect", f"What have practitioners learned about {cues[2]}?"),
            ("indirect", f"Where should I start with {cues[3]}?"),
            ("scenario", f"A team is {cues[4]}. What research would help?"),
            ("scenario", f"We need to make progress on {cues[0]} without starting from scratch."),
            ("ambiguous", f"Does the collection cover {cues[1]} and {cues[3]}?"),
            ("ambiguous", f"I have a problem involving {cues[2]}; point me to the closest body of work."),
            ("cross-topic", f"This is about {cues[4]}, not {distractor_a}. What should I read?"),
            ("cross-topic", f"The request mentions {distractor_b}, but the real issue is {cues[0]}."),
        ]
        cases.extend(
            {"question": question, "group": "topic", "slug": slug, "kind": kind}
            for kind, question in questions
        )
    return cases


def main() -> int:
    cases = build_cases()
    OUTPUT_PATH.write_text(
        json.dumps(cases, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {len(cases)} cases to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
