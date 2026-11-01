---
id: formats
language: en
version: 1.0.1
title: Specifications and open formats
---


# Specifications and open formats

| Area | Normative description |
| --- | --- |
| Weather collections | [API overview](weather-api.md), [full contract 1.7](weather-client-contract.md) |
| Dynamic wallpapers | [Composition and state machine 0.2](dynamic-wallpapers.md), [delivery/history](dynamic-api.md) |
| Numeric inputs | [All fields, units and ranges](numeric-fields.md) |
| Music | [JSON, identity and URLs](music-api.md), [acoustic selection](music-similarity.md) |
| Site themes | [Contract r11](theme-packages.md) |
| Clients | [Roles and integration](clients.md) |
| Laboratory | [Dedicated project documentation](laboratory.md) |
| Documentation | [Editions and maintenance](documentation.md) |

## Dynamic theme 0.2 schemas

- [Collection](../../schemas/dynamic/collection.schema.json).
- [Device theme](../../schemas/dynamic/v0.2/theme.schema.json).
- [Inputs](../../schemas/dynamic/v0.2/inputs.schema.json).
- [Recipe](../../schemas/dynamic/v0.2/recipe.schema.json).
- [Current frame](../../schemas/dynamic/v0.2/state.schema.json).
- [Build result](../../schemas/dynamic/v0.2/build.schema.json).
- [Life state machine](../../schemas/dynamic/v0.2/life-state.schema.json).
- [Codes](../../schemas/dynamic/v0.2/codes.json) and [numeric fields](../../schemas/dynamic/v0.2/numeric-fields.json).

Schemas are copied unchanged from the current server contract. Explanatory prose does not remove required fields. Examples: [collection](../../examples/collection.json), [theme](../../examples/theme.json), [inputs](../../examples/inputs.json). Example artwork filenames are illustrative, not an installable collection.

Full application and laboratory specifications remain in their own repositories. This collection connects them without changing their independent versions.

Reading order: [Contents](../../README.en.md) · Previous: [Teahouse composition, depth and lighting](composition.md) · Next: [Editorial data contracts](contracts.md)
