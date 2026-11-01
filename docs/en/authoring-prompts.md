---
id: authoring-prompts
language: en
version: 1.0.1
title: Authoring prompts and image creation
---


# Authoring prompts and image creation

A prompt defines a task for an image: its purpose, character, material, lighting, composition and constraints. Open examples show how these requirements are expressed when preparing project artwork.

## From intent to an image

Start with the image's role and place in the composition. Choose references and describe required variants. A layer needs a transparent background, consistent scale, anchor points and compatibility with adjacent layers. A complete illustration needs a coherent camera and a readable frame.

The artistic task describes the desired image. Theme JSON defines selection conditions, stacking and opacity. During routine updates, the server uses prepared images and exact rules.

Review the result within the scene: perspective, light, supports, character identity and action at viewing size. A successful standalone image still needs review alongside the other materials.

## Open examples

- [Inhabitants and objects](../../prompts/teahouse-objects.json).
- [Image and material studies](../../prompts/teahouse-visitors.json).
- [Examples of individual artistic tasks](../../prompts/teahouse-desktop-0.23.json).
- [Examples of vertical composition preparation](../../prompts/teahouse-phone-0.3.json).

These materials illustrate methods. Texts retain their original language. References such as Image 1 / Image 2 require the corresponding visual references.

Repeating a prompt does not guarantee identical image bytes. Exact frame reproduction needs theme sources and a build recipe. Authorship, AI involvement and reference rights remain distinct from the technical contract.

## Catalogue task prompts

The 41 tasks from the existing public package are retained: weekly selection, personal/planned/recommended cards, synthesis, series, history, recognition, names, translation, columns and journal. Each records input, output and next step. [Index and complete original-language prompts](../../prompts/README.md).

Reading order: [Contents](../../README.en.md) · Previous: [Site theme packages](theme-packages.md) · Next: [Sources and methods](sources.md)
