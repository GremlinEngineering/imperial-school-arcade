---
id: dynamic-wallpapers
language: en
version: 1.0.1
title: Dynamic theme specification
---


# Dynamic theme specification

Dynamic wallpapers are complete still frames that change with data and events. A theme contains artwork and JSON rules. The server selects and composites layers for one device; applications receive a ready JPEG and its build description.

A collection declares `type: dynamic`. Every device profile owns its dimensions, assets and rules. Schema 0.2 adds base and life phases; supported 0.1 themes retain their compatibility.

| Element | Meaning |
| --- | --- |
| `asset` | Prepared artwork identifier |
| `layers[].id` | Compositing channel, not necessarily one object |
| `order` | Integer stacking order; lower values are behind |
| `opacity` | Opacity from 0 to 1 |
| `when` | Exact selection condition |
| `phase` | `base` or `life`, defaulting to `base` |

One layer can contain several objects. Devices use their own full-resolution artwork. Omitted layers are empty. Missing inputs do not authorize guessed objects. Categorical codes describe season, day period, Moon, weather and game events; numeric fields carry measurements. The registry defines units and contract limits. Theme thresholds are artistic choices. Comparison operators are `=`, `!=`, `<`, `<=`, `>`, `>=`, combined as the schema permits. Missing numbers are not zero. Base rules cannot depend on the life hour.

RGBA layers are composited over a background by `order`, using both image alpha and layer opacity. A cup rim or railing may require a foreground layer. One object may occupy multiple depths. Equal inputs and machine state must produce the same recipe. Multiplying variant counts is only an upper bound for independent channels; exclusions and calendar relationships reduce reachable combinations.

The base recipe is compared with the previous successful build for that theme/device context. Layer membership, artwork, order or opacity changes count; unrelated numeric fluctuations do not.

| Condition | `derived.life_slot` |
| --- | --- |
| First build | `null` |
| Changed base | `null`; block the rest of the local hour |
| Hour already blocked | `null` |
| Stable base and eligible hour | Local hour 0–23 |

Skipped scenes are not queued. Returning to an earlier base does not unblock the hour. Life rules are skipped for null; household poses do not erase current game indicators. See [formats](formats.md) and the [delivery API](dynamic-api.md).

A device's artwork may stage its own scene or recompose a shared story. This artistic choice preserves the meaning of input codes and is expressed through prepared artwork and profile rules. A phone profile need not copy the desktop number of channels, objects or variants. One device's composition does not impose the same design on the entire collection. See [screen approaches](wallpapers.md).

## Exact channel resolution

Within either phase, matching rules cannot select two layers with the same id. Base is resolved first. A selected life layer sharing a base id replaces that layer entirely: asset, order and opacity come from life; absent opacity means 1, not inheritance. Final orders are unique. Conflicts are theme errors, not last-rule-wins selection.

The base key includes selected artwork and SHA-256, dimensions, layer identity and renderer. Replacing bytes under the same filename changes the base. Machine context includes theme, device, source, location/world revision and timezone. Changed contexts do not inherit previous state. An identical repeated request reuses the saved decision; an older instant cannot move the machine backwards. Successful composition commits the machine state; delivery is separate.

Reading order: [Contents](../../README.en.md) · Previous: [Weather clients: full contract 1.7](weather-client-contract.md) · Next: [Dynamic frames, JSON and archives](dynamic-api.md)


