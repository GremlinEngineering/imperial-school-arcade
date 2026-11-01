---
id: composition
language: en
version: 1.0.1
title: Teahouse composition, depth and lighting
---


# Teahouse composition, depth and lighting

The aim is a photographic house and drawn inhabitants sharing one underwater environment. Lighting, depth, contact and occlusion establish common space while preserving the materials.

The fixed camera defines separate planes for floor, walls, beams and tabletop. A wall scroll follows the wall perspective; a volumetric inhabitant retains its own form. A shelf above eye level exposes its front rim and underside. Objects need support, a grip, suspension or clearly expressed swimming. This is an artistic 2.5D construction, not a complete measured 3D room; final canvas size does not establish original 4K detail.

## Alpha and occlusion

For foreground F over opaque background B:

`C = a * F + (1 - a) * B`

Here `a` combines artwork alpha and layer opacity. For a translucent background, output alpha is `aF + aB * (1 - aF)`. Order matters. Contact edges establish weight, glass highlights pass in front of contents, and a tray rim covers figurine bases. Depth masks divide the continuous dragon without dividing its identity.

## Water and light

A simplified homogeneous-medium model uses:

`T(d) = exp(-sigma * d)`

`C(d) = T(d) * C_surface + (1 - T(d)) * C_water`

Distance maps and coefficients are chosen for this fixed-camera artwork, not presented as measurements of actual seawater. The distant reef loses more contrast than a nearby column.

Caustic patterns result from refraction, whose physical basis includes Snell's law: `n1 * sin(theta1) = n2 * sin(theta2)`. The scene uses prepared patterns projected onto each receiving plane. Curved local light fields on drawn characters preserve outlines and contact edges.

Common colour and directed light connect photography and drawing. Particle size and sharpness establish depth: distant particles are smaller and weaker; near particles may be larger and softer. Effects protect faces. The whale remains photographic and distant, the dolphin mixes realistic volume with drawn expression, and the dragon retains drawn form. These are artistic applications of compositing and light models; see [sources](sources.md).

## Screen shape changes staging

Desktop Teahouse uses the room's width and relationships among its objects. The phone foundation reveals the building's height: weather surfaces sit above an inhabited lower terrace. It is a separate camera and composition within one world. Its supports, perspective, lighting and occlusion still need to be fixed in production phone sources.

Recomposing a shared story instead preserves the main action while redistributing participants, scale and open space. Both approaches require review of the complete image at viewing size. A well-painted detail still fails when a phone notification hides it or reduction makes it unreadable.

Reading order: [Contents](../../README.en.md) · Previous: [Sunken Teahouse · Keepers of Finds](sunken-teahouse.md) · Next: [Specifications and open formats](formats.md)
