---
id: music-api
language: en
version: 1.0.1
title: Music API and track identity
---


# Music API and track identity

JSON metadata and original music files are separate. A client reads the catalogue, opens a set manifest, selects an entry and loads its asset. JSON does not contain audio.

| Resource | Site-root path |
| --- | --- |
| Music sets | `music/index.json` |
| Game and track library | `assets/gallery-music.json` |
| Set manifest | The published `manifest` value |
| Similar tracks | `assets/music-similarity.json` |
| GremlinAmp release metadata | `assets/arcade/music-app/release.json` |

`schema_version: 1` identifies the JSON structure, not the application or analyzer release. Resolve a track's relative `asset.url` against its manifest; resolve the library's set paths against the site root.

`game_id` identifies the game set, `index` its tracklist position, `id` the entry, and `subsong` the composition inside the original file. `asset.sha256` and `asset.bytes` describe the downloaded bytes. The physical audio key is `SHA256:subsong`; optional library `audio_key` exposes it without opening every manifest.

When a manifest changes, an old index can refer to different material. Recommendation playback verifies the set, track identifier and physical key rather than guessing from a title. `duration_known` distinguishes known duration from a playback limit. `play_ms` and `fade_ms` use milliseconds; unknown duration is neither zero nor proof of a short file. See [formats](formats.md). The similarity index remains optional for ordinary playback.

## Similarity index fields

Tracks is keyed by physical audio identity. Entries provide refs `{game_id, track_id, index}`, estimated bpm, rhythm_confidence, partial and neighbors. Neighbor lists rhythm and sound contain key/distance candidates and may be empty. Analyzer_version and engine identify the method; fingerprint identifies index contents. Distance is not a probability or percentage.

## Application release metadata

Application release.json provides title, description, icon_url, version, build, apk `{url, bytes, sha256}`, source_url and min_android. It does not require schema_version. Source-code links use source_url, not an APK filename.

[Manifest schema](../../schemas/music/manifest.schema.json), [gallery schema](../../schemas/music/gallery.schema.json), [similarity schema](../../schemas/music/similarity.schema.json), [app release schema](../../schemas/music/app-release.schema.json). These descriptive schemas document current public fields while allowing optional extensions. The [synthetic example](../../examples/music-manifest.json) contains no redistributed audio.

Reading order: [Contents](../../README.en.md) · Previous: [Editorial data contracts](contracts.md) · Next: [Weather API specification](weather-api.md)
