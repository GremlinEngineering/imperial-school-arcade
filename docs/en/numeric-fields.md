---
id: numeric-fields
language: en
version: 1.0.1
title: 'Numeric inputs: units, ranges and conditions'
---


# Dynamic theme 0.2 numeric inputs

This is the complete active registry. Bounds constrain normalized input, not climatic records or provider availability for every date. Missing values are null or absent, never zero. An unbounded range still excludes NaN and infinity. Units below use °C, hPa, metres (м), m/s (м/с), millimetres (мм), centimetres (см), seconds (с), W/m² (Вт/м²), J/kg (Дж/кг), volumetric m³/m³ and degrees.

| Field | Unit | Accepted value | Operators |
| --- | --- | --- | --- |
| `weather.temperature_2m` | °C | −∞ … +∞ | `>` `<` `=` `>=` `<=` `!=` |
| `weather.apparent_temperature` | °C | −∞ … +∞ | `>` `<` `=` `>=` `<=` `!=` |
| `weather.dew_point_2m` | °C | −∞ … +∞ | `>` `<` `=` `>=` `<=` `!=` |
| `weather.wet_bulb_temperature_2m` | °C | −∞ … +∞ | `>` `<` `=` `>=` `<=` `!=` |
| `weather.soil_temperature_0cm` | °C | −∞ … +∞ | `>` `<` `=` `>=` `<=` `!=` |
| `weather.relative_humidity_2m` | % | ≥ 0; ≤ 100 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.cloud_cover` | % | ≥ 0; ≤ 100 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.cloud_cover_low` | % | ≥ 0; ≤ 100 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.cloud_cover_mid` | % | ≥ 0; ≤ 100 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.cloud_cover_high` | % | ≥ 0; ≤ 100 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.precipitation_probability` | % | ≥ 0; ≤ 100 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.pressure_msl` | hPa | > 0 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.surface_pressure` | hPa | > 0 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.visibility` | m | ≥ 0 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.wind_speed_10m` | m/s | ≥ 0 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.wind_gusts_10m` | m/s | ≥ 0 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.snow_depth` | m | ≥ 0 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.shortwave_radiation` | W/m² | ≥ 0 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.direct_radiation` | W/m² | ≥ 0 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.diffuse_radiation` | W/m² | ≥ 0 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.uv_index` | index | ≥ 0 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.cape` | J/kg | ≥ 0 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.wind_direction_10m` | ° | ≥ 0; < 360 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.precipitation` | mm | ≥ 0 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.rain` | mm | ≥ 0 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.showers` | mm | ≥ 0 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.snowfall` | cm | ≥ 0 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.sunshine_duration` | s | ≥ 0; ≤ 3600 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.freezing_level_height` | m | −∞ … +∞ | `>` `<` `=` `>=` `<=` `!=` |
| `weather.soil_moisture_0_to_1cm` | m³/m³ | ≥ 0; ≤ 1 | `>` `<` `=` `>=` `<=` `!=` |
| `weather.is_day` | 0/1 | 0, 1 | `=` `!=` |
| `weather.weather_code` | code | ≥ 0; ≤ 99 | `=` `!=` |
| `sun.azimuth` | ° | ≥ 0; < 360 | `>` `<` `=` `>=` `<=` `!=` |
| `sun.elevation` | ° | ≥ -90; ≤ 90 | `>` `<` `=` `>=` `<=` `!=` |
| `sun.daylight_duration` | s | ≥ 0; ≤ 86400 | `>` `<` `=` `>=` `<=` `!=` |
| `derived.pressure_change_3h` | hPa | −∞ … +∞ | `>` `<` `=` `>=` `<=` `!=` |
| `derived.temperature_change_3h` | °C | −∞ … +∞ | `>` `<` `=` `>=` `<=` `!=` |
| `derived.life_slot` | hour | ≥ 0; ≤ 23 | `=` `!=` `<` `<=` `>` `>=` |

Precipitation, rain, showers, snowfall and sunshine_duration cover the preceding hour. Three-hour pressure/temperature differences require history; otherwise they are missing. Pressure is hPa, visibility metres and wind m/s. Solar angles use the place and instant; daylight duration is seconds. Azimuth and wind direction normalize modulo 360. Weather codes are categorical: the 0–99 reserved range does not define every integer's meaning.

```json
{"all": [{"field": "weather.pressure_msl", "op": "<", "value": 1005}, {"code": "time.day"}]}
```

Comparisons against missing numbers, including !=, are false. Combine range bounds with all and alternatives with any. Schema 0.2 has no not syntax. Thresholds are artistic choices; a number changing does not necessarily change an image. Life_slot is a state-machine output, null or eligible local hour 0–23, and is unavailable to base rules. See the [registry](../../schemas/dynamic/v0.2/numeric-fields.json) and [machine specification](dynamic-wallpapers.md).

Reading order: [Contents](../../README.en.md) · Previous: [Dynamic frames, JSON and archives](dynamic-api.md) · Next: [Site theme packages](theme-packages.md)
