---
id: weather-client-contract
language: en
version: 1.0.1
title: 'Weather clients: full contract 1.7'
---


# Weather clients: contract 1.7

Normative companion to the [API overview](weather-api.md). Every relative URL in weather JSON resolves against `https://games.oopssre.ru/assets/arcade/views/`, including paths inside nested forecasts. Document version 1.7, JSON schema numbers and opaque content versions are distinct.

## Documents

| Document | Purpose |
| --- | --- |
| `manifest-v3.json` | Collection, format and download catalogue; schema 3 |
| `weather/C/current.json` | Last refresh snapshot; schema 1, type weather |
| `weather/C/forecast-D.json` | Prepared schedule for device D; schema 1, document_type weather-forecast |
| `weather/C/assets.json` | Prepared image catalogue; schema 1 |
| Download ZIP | Artwork for a collection and device, not a live forecast |

Current is a snapshot, not a clock. Once its interval ends, select the next image from the forecast. Overall ready means at least one format; test the selected format separately.

## Current fields

| Fields | Meaning |
| --- | --- |
| `collection_id`, `title` | Artwork identity and title |
| `source_id`, `world_id`, `source` | real or game-world; nullable world and source description |
| `location`, `location_revision`, `timezone` | Name, coordinates and zone; opaque revision; IANA timezone |
| `formats`, `package_versions` | Declared formats and their package versions |
| `status`, `reason` | Overall readiness and nullable reason |
| `files`, optional `format_status` | Ready files and per-format availability |
| `season`, `time_of_day`, `weather`, `weather_code` | Available state; weather group and code may be null |
| Optional `state_id`, `state_title`, `moon_phase`, `world_date` | State identity, caption, Moon and game-world date |
| Optional `valid_from`, `valid_until`, `forecast_valid_until` | Availability boundaries |
| `weather_fetched_at`, `refresh_after` | Nullable fetch time and refresh recommendation |
| `refresh_error` | Nullable `{at, message}` |
| Optional `preview`, `preview_format` | Preview and its format |
| `last_successful_image` | Nullable last successful picture |
| `delivery.direct_image.enabled` | Stable image-address availability |

Current does not require generated_at, document_type or contract_version. It does not promise the full numeric temperature/wind dataset used by dynamic composition.

An image file has `url`, `format: jpeg`, `rendition`, `width`, `height`, `aspect`, `bytes`, `sha256`, `cache_key`. The task cache key is not the byte digest. Current's selected file may additionally provide state identity, caption, stable image_url and previews. Optional previews provide URL, format, dimensions, byte count and digest. Ordinary thumbnails have a longest edge up to 640 px; player previews are separate renditions.

## Forecasts and intervals

A ready forecast provides collection_id, format, source_id, world_id, contract_version, optional package_version, location, location_revision, timezone, generated_at, valid_until, refresh_after, weather_fetched_at, source, season_months, astronomy and intervals. Compare opaque versions for equality. A ready document need not have a top-level status. An unavailable forecast may be abbreviated to status unavailable, null generation/expiry times and an empty interval list.

The horizon covers 24 hours from generated_at, not until midnight. Select `valid_from <= now < valid_until`, preserving absolute offsets and exact boundaries. Adjacent equal states may merge, so interval count is variable. Refresh_after recommends a new request and is not an image-expiry timestamp.

Intervals provide boundaries, world_date, season, time_of_day, weather, weather_code, state_id, moon_phase and status. A ready interval supplies file and image_url equal to file.url, rather than current's stable address; previews are optional. An unready interval supplies a reason and null image_url, with no ready file.

Astronomy describes engine, days, solar depression and Moon policy. Day records contain dawn, sunrise, sunset, dusk and moon_phase; polar solar events can be null. Clients consume prepared intervals rather than recomputing Astral. The legacy ordinary-calendar value local is not the weather source's timezone.

## State vocabulary

Seasons: spring, summer, autumn, winter. Day periods: dawn, day, dusk, night. Moon: none, new_moon, waxing_crescent, first_quarter, waxing_gibbous, full_moon, waning_gibbous, last_quarter, waning_crescent. None means no lunar variant, not new moon.

| Weather group | Source codes |
| --- | --- |
| clear | 0 |
| partly-cloudy | 1, 2 |
| overcast | 3 |
| fog | 45, 48 |
| drizzle | 51, 53, 55 |
| rain | 61, 63, 80, 81 |
| heavy-rain | 65, 82 |
| freezing-precipitation | 56, 57, 66, 67 |
| snow | 71, 73, 77, 85 |
| heavy-snow | 75, 86 |
| thunderstorm | 95 |
| severe-thunderstorm | 97 |
| thunderstorm-hail | 96, 99 |

Code 97 is a project mapping, not a promise that Open-Meteo returns it. These 13 prepared-weather groups differ from dynamic themes' six groups. State IDs are season-period-weather; the weather component itself may contain hyphens.

## Readiness and failure

Statuses: ready, not_ready, unresolved_weather, unavailable, stale. Unknown statuses are not ready. Reasons: weather_unavailable, forecast_expired, unknown_weather_code, state_not_in_collection, prototype_only, artwork_planned, prepared_variant_missing, prepared_file_missing, prepared_file_damaged. Unknown future reasons must not crash a client.

HTTP 200 does not guarantee a ready image. Network, HTTP and JSON errors are delivery failures. A previously installed image may remain with an honest caption; do not label it current or silently switch sources/worlds. Last_successful_image captions come from the selected device's file. Applied_at is server metadata, not the client's installation time.

## ZIPs and compatibility

Select a download by collection, zip format and device rendition. Records provide identity, title, URL, bytes, SHA-256 and version. Use the published URL. A ZIP serves both weather sources but only one device.

It includes manifest.json (schema 3, document_type weather-wallpaper-package, type weather, id, title, version, format, ready_states, total_states, variants), weather-package.json (schema 1, type and format), README and JPGs. Variants identify state, title, Moon and file properties. ZIP paths are archive-relative. Match both state and Moon. Compare the archive version with this device's forecast.package_version; a collection's contract version may change because another device changed.

Assets.json describes identity, version, formats, availability and states. Each state supplies id, title, status, moon_mode, variants[phase][device] and optional previews. One ready device does not imply every device exists. An artwork ZIP does not grant an indefinite forecast.

Read a compatible current/forecast pair, checking source, world, location revision, device and declared versions. If publication occurs between requests, reread the pair. Individual JSON replacement is atomic; two HTTP requests are not a transaction. Download to a temporary file, verify bytes, SHA-256 and JPEG dimensions, then replace the local image. Ignore unfamiliar optional fields, but do not guess an incompatible schema.

Reading order: [Contents](../../README.en.md) · Previous: [Weather API specification](weather-api.md) · Next: [Dynamic theme specification](dynamic-wallpapers.md)
