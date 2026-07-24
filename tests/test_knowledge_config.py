from knowledge_indexing import knowledge_config as cfg


def test_text_config_files_load_expected_policy_terms():
    assert "the" in cfg.STOPWORDS
    assert "github" in cfg.BAD_TOPIC_TOKENS
    assert "gain insights" in cfg.BAD_TOPIC_PHRASES


def test_seed_topics_load_from_tsv():
    assert len(cfg.SEED_TOPICS) == 35
    seed_map = dict(cfg.SEED_TOPICS)
    assert "malicious software" in seed_map["Malware analysis and reverse engineering"]
    assert "proof-of-concept exploit work" in seed_map["Exploit development and vulnerability discovery"]
    assert "application security testing" in seed_map["Application security"]
    assert "sensitive data movement" in seed_map["Data loss detection and prevention"]
    assert "voting systems" in seed_map["Election security"]
    assert "adversary tracking" in seed_map["Threat intelligence and adversary tracking"]
