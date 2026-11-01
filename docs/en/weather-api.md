---
id: weather-api
language: en
version: 1.0.1
title: Weather API specification
---


# Weather API specification

Weather 1.7 retains the source, interval and format model of the API 1.x family. A document revision is not its `schema` value. Base URL: `https://games.oopssre.ru/assets/arcade/views/`. Resolve all weather JSON relative paths against this base, including paths inside nested forecasts.

| Resource | Base-relative path | Schema |
| --- | --- | --- |
| Catalogue | `manifest-v3.json` | 3 |
| Real current state | `weather/C/current.json` | 1 |
| Real device forecast | `weather/C/forecast-D.json` | 1 |
| World current state | `weather/C/sources/game-world/current.json` | 1 |
| World forecast | `weather/C/sources/game-world/forecast-D.json` | 1 |
| Prepared artwork | `weather/C/assets.json` | 1 |
| Direct current JPEG | `weather/C/current-D.jpg` | Image |
| Direct world JPEG | `weather/C/sources/game-world/current-D.jpg` | Image |

`C` is a collection ID; `D` is a declared format. Direct images are used when declared in published data. Format support and a particular image's readiness are separate checks.

A collection selects artwork; `source_id` selects weather. Sources are `real` and `game-world`; real weather does not require `/sources/real/`. `world_id` identifies a game environment, and `location_revision` an environmental revision. Caption using `source.setting`, falling back to `source.name`. Take season, light and `world_date` from the current interval and switch at its boundaries.

Stable URLs may change bytes. Use published versions and SHA-256. A digest mismatch requires refreshing metadata, not accepting unverified artwork. A compatible forecast can survive a network error only until its stated expiry. `weather_fallback` is a separate unavailability illustration, not a fabricated weather state or a device-size JPEG.

Solar events depend on date, coordinates and an explicit timezone. Moon phases use the eight declared values. Follow precise schedule boundaries where provided; device-local dates must not replace a game world's calendar. See the [full client contract](weather-client-contract.md), [dynamic wallpapers](dynamic-wallpapers.md) and [formats](formats.md).

Reading order: [Contents](../../README.en.md) · Previous: [Music API and track identity](music-api.md) · Next: [Weather clients: full contract 1.7](weather-client-contract.md)
