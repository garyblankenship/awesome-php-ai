# Changelog

## v0.1.0 (2026-06-15)

### Features
- Add the PHP README/site generator and interactive static site workflow.
- Add developer-themed PHP AI curation, including MCP and agent tooling entries.
- Extract the generated site template into a dedicated template file.

### Fixes
- Correct generated GitHub repository URLs.
- Harden generated site output for untrusted catalog text, URLs, and embedded JSON.
- Reject unknown top-level `readme.json` sections during generation.

### Documentation
- Regenerate the public README and docs site from `readme.json`.
- Document the source-of-truth curation workflow for contributors.
