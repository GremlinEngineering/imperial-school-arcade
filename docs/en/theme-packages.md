---
id: theme-packages
language: en
version: 1.0.1
title: Site theme packages
---


# Site theme packages

Site themes, wallpaper collections and dynamic device themes have distinct contracts. A site package controls calendar appearance, palette, resources and page artwork; it does not rename wallpaper devices.

## Contract r11

A package directory contains theme.json and manifest.json. Theme JSON has schema 1, id matching the directory, a nonempty title, and kind: default, season, manual, holiday, birthday, game, console or company.

| Field | Purpose |
| --- | --- |
| palette | Appearance palette |
| styles, scripts | Relative package resource lists |
| files | Public assets/... destination to local file mapping |
| calendar | Calendar entry sharing the package id; seasons require start |
| icons | Public icons declared in files |
| artwork | full by default, or none |
| media | visibility always, hidden or event-day; boolean preview/current |

Manifest JSON has schema 1 and images. Full artwork requires 22 approved scenes in day/night versions, totalling 44 images, keyed theme/scene/period. None requires an empty image map and other theme resources. Paths stay within the package. Missing artwork must not borrow another theme's picture. Shared public destinations across packages require identical bytes.

This describes portable resources and package behaviour. Programmatic extensions are not a general-purpose artwork format for arbitrary clients. Application installers and release JSON have separate contracts.

Reading order: [Contents](../../README.en.md) · Previous: [Numeric inputs: units, ranges and conditions](numeric-fields.md) · Next: [Authoring prompts and image creation](authoring-prompts.md)
