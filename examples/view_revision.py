"""Editorial data comparison examples. SPDX-License-Identifier: MIT."""
from __future__ import annotations
import hashlib,json,re


def pairs(games: list[catalog.Game]) -> list[tuple[catalog.Game, catalog.Game]]:
    """Pair each weekly issue with a complete played card of the same port."""
    weekly_games = []
    played_by_id = {}
    for game in games:
        identifier = game.retroachievements_id
        if not identifier:
            continue
        if re.fullmatch(r"\d{4}-\d{2}-W\d{2}", game.key):
            weekly_games.append(game)
        elif game.in_profile and game.key == f"ra-{identifier}":
            played_by_id[identifier] = game
    return [(game, played_by_id[game.retroachievements_id]) for game in weekly_games
            if game.retroachievements_id in played_by_id and game.platform and
            game.platform == played_by_id[game.retroachievements_id].platform]


def signature(week: catalog.Game, played: catalog.Game, prompt: str | None = None) -> str:
    payload = {"ra_id": week.retroachievements_id, "week": week.key,
               "platform": week.platform, "weekly_view": week.description,
               "played_view": played.description}
    data = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(data.encode("utf-8")).hexdigest()
