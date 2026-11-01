---
id: documentation
language: en
version: 1.0.1
title: Documentation maintenance
---


# Documentation maintenance

Russian is canonical; English accompanies the same material for GitHub. The website publishes Russian from the same Markdown, tables, schemas and examples, without a separately edited HTML edition.

Registry.json records documents, component/contract versions, per-language SHA-256 digests, document revisions and the Russian source digest reviewed for each translation. A changed original requires translation review. Digest checks detect edition mismatch, not translation quality.

Public behaviour changes update the relevant specification, examples, Russian article and translation together. Incompatible contracts receive new versions; new artwork does not automatically change a JSON schema version. The laboratory retains its independent authoritative documentation.

The bundle includes Markdown, JSON schemas/examples, Teahouse images and source-project references. Its checker validates the registry, digests, local links and translation correspondence without private settings or account access. If a documentation update fails, the previous published edition remains while games, music and wallpapers continue building. Server configuration, keys and administrative logs are excluded from the public bundle.

## One reading order

Seven parts cover the project, overall architecture, projects, artwork examples, specifications, practical material and maintenance. Registry.json reading_groups defines groups and page order for website navigation and PDF. README introduces the documentation, while chapter footers connect adjacent material. Add a chapter to exactly one group, review both editions and README contents, then run the checker.

Reading order: [Contents](../../README.en.md) · Previous: [Usage terms and authorship](scope-and-rights.md)
