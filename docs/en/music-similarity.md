---
id: music-similarity
language: en
version: 1.0.1
title: Rhythm, timbre and acoustic similarity
---


# Rhythm, timbre and acoustic similarity

Rhythm and sound continuation use measured audio features, not game-title genre guesses. A match describes similarity between selected sound descriptors; it does not establish identical melodies or a listener's preferences.

Up to three 20-second windows cover the beginning, middle and end. Unknown duration uses the beginning with `partial`; known tracks shorter than 12 seconds are excluded by default. Audio is mono at 22050 Hz and level-normalized before measurement.

| Feature family | Measurement |
| --- | --- |
| Timbre | Median and spread of MFCC 1–13 over 40 mel bands |
| Rhythm | Positive spectral-flux autocorrelation across 40–240 BPM |
| Harmony | Twelve pitch classes, compared across transpositions |
| Dynamics | Energy distribution and variation |

The rhythm profile folds half/double-tempo ambiguity. It is not a full meter or syncopation model. `rhythm_confidence` is a 0–1 reliability heuristic, not a probability of musical similarity.

Library-relative normalization handles timbre and dynamics. KD-tree retrieval selects a bounded candidate pool for descriptor reranking rather than allocating every pair. Retrieval is approximate, with no exact global top-k guarantee. Lower neighbor `distance` means closer descriptors, never a percentage. Low-confidence rhythm can have no rhythm neighbors.

Analysis is independent of listening. An absent index or failed original does not remove ordinary playback. An incomplete update does not replace a complete index. Compatible measurements are reused. The public contract is `assets/music-similarity.json`, schema 1, keyed by `SHA256:subsong`. See the [music API](music-api.md) and [method sources](sources.md).

Reading order: [Contents](../../README.en.md) · Previous: [Music and GremlinAmp players](music.md) · Next: [Views and wallpaper collections](wallpapers.md)
