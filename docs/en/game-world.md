---
id: game-world
language: en
version: 1.0.1
title: Game-world weather
---


# Game-world weather

Weather artwork and weather source are independent. One collection can depict another game's environment. The published source identifies the active world, not the picture's style.

The Imperial Capital's Weather is the real server source. Game World is a prepared game environment with its own climate and calendar. A user-selected Open-Meteo city is a separate scenario on supporting clients; that city is not the server source's label.

The world's year and initial season need not match Earth's current year or month. After its origin, one game day passes per real day. `world_date` carries the current world date. An initial season must not replace the current interval season. Climate drives the world's weather, while light and Moon information follow the corresponding environment and date. Clients consume ready results; opening an image does not create a new world.

`world_id` identifies a world. `location_revision` distinguishes environmental changes even when that identity remains. Old schedules must not automatically survive a revision change. Availability follows API status. A compatible forecast may be used until it expires; a cached picture does not renew that deadline. See the [weather API](weather-api.md).

Reading order: [Contents](../../README.en.md) · Previous: [Wallpaper applications and device capabilities](clients.md) · Next: [Laboratory — a separate project](laboratory.md)
