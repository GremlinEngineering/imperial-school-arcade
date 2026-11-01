---
id: editorial-contracts
language: en
version: 1.0.1
title: Editorial data contracts
---


# Editorial data contracts

Each stage consumes prepared data and returns a defined result. Game identity, editorial inputs, series context and artwork metadata have distinct contracts.

## Game and version

A useful minimal record provides card identity, external identifiers, platform, title, available date precision and role: personal, planned, recommended or reference. A work-level identifier does not establish identity across every port. Confirmed series membership is distinct from title resemblance. Facts should retain value, source, precision and observation time.

## Perspective synthesis

```json
{"title":"Demonstration game","year":1991,"platform":"NES","weekly_view":"First discovery: precise jumps and short stages.","played_view":"After completion, route choices become clearer."}
```

The response supplies a nonempty view string. This stage rejects headings, URLs and citation markers. RA ID and platform must match before synthesis. Its basis also includes the weekly issue key and exact original texts. [Input](../../examples/view-input.json) and [response](../../examples/view-output.example.json) are synthetic examples.

## Series context and membership

The series task receives series and saved_game_texts. Series supplies identity, title, source, known participants and possible incompleteness; saved games supply ra_id, title, platform, view, place_in_history and series_context. External facts, generated writing and authored notes retain their origin.

```json
{"schema":1,"series":[{"id":"demo-series","members":[["ra",101,true],["ra",202,false]]}]}
```

Identifiers are illustrative. Each third member value marks personal participation. Canonical membership, rather than naming changes alone, determines the reason for revision.

## Themes and laboratory

A theme package connects appearance, its own calendar, display policy and a selection of up to ten games. Artwork registries record status and original digests. Laboratory entries use laboratory_id, not an invented RA ID. A theme missing required resources is excluded as a whole and available fallback artwork is selected. Its resources are validated before selection. Laboratory records describe original, reconstruction, sources, controls, application and poster. Historical devices and browser reconstructions remain distinct, including in structured metadata. Current device-theme contracts are documented in [formats](formats.md).

Reading order: [Contents](../../README.en.md) · Previous: [Specifications and open formats](formats.md) · Next: [Music API and track identity](music-api.md)
