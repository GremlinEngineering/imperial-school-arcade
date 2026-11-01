---
id: music
language: en
version: 1.0.1
title: Music and GremlinAmp players
---


# Music and GremlinAmp players

The library connects game and series soundtracks. One native game-music file can contain multiple tracks. Each is listed separately while retaining its zero-based `subsong`; it need not become a separate MP3.

The web player appears in the media library and detailed cards with ready music. GremlinAmp for Android adds downloads, offline listening, system playback controls and collection updates. The Mac music application is a separate development effort; web or Android readiness does not establish its readiness.

NSF, NSFE, GBS, HES, SPC, VGM/VGZ, AY and SAP use emulated sound systems. Supplied recordings such as MP3 use ordinary audio playback. Supporting an extension does not imply supporting every chip inside it. YM2413 uses the shared GremlinAmp 0.2.4 emu2413 implementation; concrete format limitations require decoder checks.

| Web option | Rule |
| --- | --- |
| In order | Next queue entry; stop at the end |
| By rhythm / By sound | Continue using prepared acoustic features |
| After game | Finish remaining tracks of this game, then choose another game |
| After track | Choose after every composition |
| Previous / Next | Follow listening history, then the selected continuation policy |

Acoustic selection searches the whole library, as stated beside the controls. A manual selection starts a new queue. Changing policy preserves the current track and its in-progress load. Missing recommendations fall back to the ordinary queue, which stops when exhausted.

Acoustic similarity differs from game similarity by genre, platform or series. Android may offer those policies separately; the application's controls define their scope and repeat priority. Shared originals are downloaded once where possible and verified against published sizes and SHA-256. Rights to music remain with their holders. See the [music API](music-api.md) and [acoustic similarity](music-similarity.md).

Reading order: [Contents](../../README.en.md) · Previous: [Navigation, accessibility and metadata](accessibility.md) · Next: [Rhythm, timbre and acoustic similarity](music-similarity.md)
