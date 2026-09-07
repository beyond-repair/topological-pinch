"""Docs-presence checks. Not physics validation."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ("README.md", "CLAIM_STATUS.md", "GOVERNANCE.md", "LICENSE")


def test_required_docs_exist():
    missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
    assert missing == [], f"missing required docs: {missing}"


def test_claim_status_denies_validation():
    text = (ROOT / "CLAIM_STATUS.md").read_text(encoding="utf-8").lower()
    assert "unverified" in text
    assert "false" in text


def test_readme_is_research():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "RESEARCH" in text
    assert "hypothesis" in text.lower()
