import pytest


@pytest.fixture
def sample_vault(tmp_path):
    """Create a temporary vault with sample documents."""
    vault = tmp_path / "vault"
    vault.mkdir()

    (vault / "note1.md").write_text("# First Note\n\nThis is about Python programming.")
    (vault / "note2.md").write_text("---\ntags: [recipe]\n---\n# Pasta Recipe\n\nBoil water...")
    (vault / "daily").mkdir()
    (vault / "daily/2024-01-01.md").write_text("# Daily Note\n\nToday I learned about Whoosh.")

    return vault


@pytest.fixture
def configured_settings(sample_vault, monkeypatch):
    """Configure settings to use sample vault."""
    monkeypatch.setenv("OBSIDIAN_VAULT_PATH", str(sample_vault))
    monkeypatch.setenv("INDEX_PATH", str(sample_vault / ".index"))

    import importlib
    import src.config

    importlib.reload(src.config)

    from src.config import settings

    return settings
