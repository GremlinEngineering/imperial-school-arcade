"""Editorial data comparison examples. SPDX-License-Identifier: MIT."""
from __future__ import annotations
import hashlib,json


def membership_state(rows, previous=None):
    """Comparable editorial composition, with old identities resolved before comparison.

    Only actual RA/card membership and personal ownership affect generation.
    Provider IDs, evidence records, names, routes, timers and model changes do
    not. A persisted snapshot makes the reason inspectable instead of guessing
    what an old opaque hash used to contain.
    """
    aliases = {}
    current = []
    def key(value):
        return str(value).removesuffix('.html').removeprefix('series-')
    for row in rows:
        identity = key(row.get('membership_identity') or row.get('filename') or row['slug'])
        for value in (row.get('filename', ''), row['slug'], row.get('membership_identity', ''), *row.get('aliases', ())):
            if value:
                aliases[key(value)] = identity
        members = []
        for member in (*row.get('games', ()), *row.get('ra_games', ())):
            get = member.get if isinstance(member, dict) else lambda k, default=None: getattr(member, k, default)
            identifier = get('game_id') if isinstance(member, dict) else get('retroachievements_id')
            kind, identifier = ('ra', identifier) if type(identifier) is int and identifier > 0 else ('card', get('key', ''))
            if not identifier:
                continue
            members.append([kind, identifier, bool(get('in_profile', False) and not get('is_series_reference', False))])
        current.append({'id': identity, 'members': members})
    state = {'schema': 1, 'series': current} if previous is None else previous
    if not isinstance(state, dict) or state.get('schema') != 1 or not isinstance(state.get('series'), list):
        raise ValueError('Некорректное сохранённое состояние состава серии')
    grouped = {}
    for series in state['series']:
        if not isinstance(series, dict) or not isinstance(series.get('id'), str) or not series['id'] or not isinstance(series.get('members'), list):
            raise ValueError('Некорректная серия в состоянии состава')
        members = grouped.setdefault(aliases.get(key(series['id']), key(series['id'])), {})
        for member in series['members']:
            if (not isinstance(member, list) or len(member) != 3 or type(member[2]) is not bool
                    or not (member[0] == 'ra' and type(member[1]) is int and member[1] > 0
                            or member[0] == 'card' and isinstance(member[1], str) and member[1])):
                raise ValueError('Некорректная игра в состоянии состава')
            identity = (member[0], member[1])
            members[identity] = members.get(identity, False) or member[2]
    return {'schema': 1, 'series': [
        {'id': identity, 'members': [[kind, value, personal] for (kind, value), personal in sorted(members.items(), key=repr)]}
        for identity, members in sorted(grouped.items())]}


def membership_signature(rows):
    return hashlib.sha256(json.dumps(membership_state(rows), ensure_ascii=True, sort_keys=True).encode()).hexdigest()


def membership_change_reason(previous, current):
    def members(state):
        return {(series['id'], kind, value): personal for series in state['series']
                for kind, value, personal in series['members']}
    old, new = members(previous), members(current)
    changed = sum(old[key] != new[key] for key in old.keys() & new.keys())
    return f'состав изменился: добавлено {len(new.keys()-old.keys())}, убрано {len(old.keys()-new.keys())}, личный статус {changed}'
