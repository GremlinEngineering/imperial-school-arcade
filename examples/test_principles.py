"""Observable invariants of the published excerpts, on synthetic inputs only."""
import copy
from types import SimpleNamespace
import unittest

from view_revision import pairs,signature
from series_revision import membership_state,membership_signature,membership_change_reason


def card(key='ra-101',ra=101,platform='nes',personal=True,description='Текст взгляда'):
    return SimpleNamespace(key=key,retroachievements_id=ra,platform=platform,
                           in_profile=personal,is_series_reference=False,description=description)


def series(*members):
    return {'slug':'demo-series','games':list(members),'ra_games':[]}


class ViewTests(unittest.TestCase):
    def test_same_edition_pairs_weekly_and_personal(self):
        week=card('2026-10-W43',personal=False)
        played=card()
        self.assertEqual(pairs([week,played]),[(week,played)])

    def test_same_name_other_platform_does_not_pair(self):
        self.assertEqual(pairs([card('2026-10-W43'),card(platform='snes')]),[])

    def test_missing_confirmed_id_does_not_pair(self):
        self.assertEqual(pairs([card('2026-10-W43',ra=None),card()]),[])

    def test_reference_card_is_not_personal_experience(self):
        self.assertEqual(pairs([card('2026-10-W43'),card(personal=False)]),[])

    def test_each_source_view_changes_the_basis(self):
        week=card('2026-10-W43');played=card()
        before=signature(week,played)
        week.description+=' Новая мысль.'
        self.assertNotEqual(signature(week,played),before)
        week.description='Текст взгляда';played.description+=' Новый опыт.'
        self.assertNotEqual(signature(week,played),before)

    def test_prompt_only_change_keeps_existing_basis(self):
        week=card('2026-10-W43');played=card()
        self.assertEqual(signature(week,played,'редакция 1'),signature(week,played,'редакция 2'))

    def test_weekly_issue_identity_changes_basis(self):
        played=card()
        self.assertNotEqual(signature(card('2026-10-W43'),played),signature(card('2026-11-W44'),played))


class MembershipTests(unittest.TestCase):
    def test_member_order_and_duplicate_are_not_new_context(self):
        one=card();two=card('ra-202',ra=202)
        self.assertEqual(membership_signature([series(one,two)]),membership_signature([series(two,one,one)]))

    def test_title_and_provider_metadata_do_not_change_context(self):
        row=series(card());before=membership_signature([row])
        row.update(name='Новое отображаемое имя',source='Другой поставщик',model='new-model')
        self.assertEqual(membership_signature([row]),before)

    def test_new_member_has_explainable_reason(self):
        previous=membership_state([series(card())])
        current=membership_state([series(card(),card('ra-202',ra=202))])
        self.assertEqual(membership_change_reason(previous,current),
                         'состав изменился: добавлено 1, убрано 0, личный статус 0')

    def test_reference_becomes_personal(self):
        old={'slug':'demo-series','games':[],'ra_games':[{'game_id':101}]}
        previous=membership_state([old]);current=membership_state([series(card())])
        self.assertEqual(membership_change_reason(previous,current),
                         'состав изменился: добавлено 0, убрано 0, личный статус 1')

    def test_confirmed_alias_normalizes_old_series_identity(self):
        row=series(card());row['slug']='new-demo';row['aliases']=['old-demo']
        previous={'schema':1,'series':[{'id':'old-demo','members':[['ra',101,True]]}]}
        self.assertEqual(membership_state([row],previous),membership_state([row]))

    def test_invalid_personal_flag_does_not_become_truth(self):
        previous={'schema':1,'series':[{'id':'demo-series','members':[['ra',101,1]]}]}
        with self.assertRaises(ValueError):membership_state([series(card())],previous)

    def test_comparison_does_not_modify_saved_snapshot(self):
        previous={'schema':1,'series':[{'id':'old-demo','members':[['ra',101,True]]}]}
        before=copy.deepcopy(previous);row=series(card());row['aliases']=['old-demo']
        membership_state([row],previous)
        self.assertEqual(previous,before)


if __name__=='__main__':unittest.main()
