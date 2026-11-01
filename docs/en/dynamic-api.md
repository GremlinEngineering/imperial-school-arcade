---
id: dynamic-api
language: en
version: 1.0.1
title: Dynamic frames, JSON and archives
---


# Dynamic frames, JSON and archives

Composition and delivery are separate operations. Publication uses a prepared result; clients consume it. A theme-matrix entry alone does not mean an image is available.

Base URL: `https://games.oopssre.ru/assets/arcade/views/`. `T` is a theme and `D` a declared device.

| Material | Path |
| --- | --- |
| Current JPEG | `dynamic/T/devices/D/current.jpg` |
| Preview | `dynamic/T/devices/D/current-preview.jpg` |
| Current JSON | `dynamic/T/devices/D/current.json` |
| State history | `dynamic/T/devices/D/states.zip` |
| Device theme archive | `downloads/theme-T-D.zip` |

Sunken Teahouse's `desktop_3456x2234` is a 3456 × 2234 composition. Other profiles must be discovered, not inferred.

The state envelope identifies theme, device, moment, image and preview. `inputs` records selection data, `recipe` the selected layers, and `asset_sha256` the source artwork. Schema 0.2 adds the machine decision in `life`. `image.sha256` describes the final JPEG. Reproduction uses recorded inputs and matching artwork, not the current forecast or clock. Byte-identical JPEGs also require the declared renderer and JPEG implementation.

The server keeps one current raster frame and preview per device. `states.zip` stores daily/context JSON history, not every historical JPEG; actual entries determine coverage. Theme archives are device-specific and may be updated at stable URLs without preserving earlier artwork versions. An old state remains reproducible when its matching original archive has been retained locally.

Clients verify identity, dimensions, validity and digests. Weather and household selection are already resolved by the server. Temporary failures may leave applied wallpaper in place without turning it into a new state. See [schemas](formats.md) and [theme rules](dynamic-wallpapers.md).

Reading order: [Contents](../../README.en.md) · Previous: [Dynamic theme specification](dynamic-wallpapers.md) · Next: [Numeric inputs: units, ranges and conditions](numeric-fields.md)
