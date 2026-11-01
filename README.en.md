# Imperial School Arcade

[Русский](README.md) · [Open the website](https://games.oopssre.ru/)

Dmitry Malykhin's autobiography built from play data and told through retro games. **When I play, the website changes.** The catalogue, journal, music, artwork, applications and research connect through shared games and events.

## How to read this documentation

Start with the [project idea](docs/en/project.md), then the [catalogue](docs/en/catalog.md), [journal](docs/en/journal.md) and [media library](docs/en/media.md). These explain the reader's experience. The next part introduces overall architecture, followed by individual projects and artwork examples. Exact contracts and complete task prompts come later in the reference/practical parts.

The documentation serves readers, material authors and integration developers. Application-specific instructions remain in application repositories; JSON and theme rules belong to the corresponding specification below.

## Contents

### 1. The project and its website

What the project is, who it serves and what readers can find.

- [Imperial School Arcade](docs/en/project.md)
- [Game catalogue and data sources](docs/en/catalog.md)
- [Journal and personal play experience](docs/en/journal.md)
- [Media library, viewing and search](docs/en/media.md)

### 2. How the system works

From component relationships to data, editorial tasks and revision policies.

- [Architecture of the Arcade](docs/en/architecture.md)
- [Components and subsystems](docs/en/site-engines.md)
- [The semantic engine](docs/en/meaning-system.md)
- [When materials change](docs/en/editorial-feedback.md)
- [From data to writing and artwork](docs/en/prompt-pipeline.md)
- [Navigation, accessibility and metadata](docs/en/accessibility.md)

### 3. Projects and applications

Music, collections, applications and the laboratory.

- [Music and GremlinAmp players](docs/en/music.md)
- [Rhythm, timbre and acoustic similarity](docs/en/music-similarity.md)
- [Views and wallpaper collections](docs/en/wallpapers.md)
- [Wallpaper applications and device capabilities](docs/en/clients.md)
- [Game-world weather](docs/en/game-world.md)
- [Laboratory — a separate project](docs/en/laboratory.md)

### 4. Artwork and case studies

How visual identity works and how a particular scene expresses the shared idea.

- [Site and game visual identity](docs/en/visual-identity.md)
- [Sunken Teahouse · Keepers of Finds](docs/en/sunken-teahouse.md)
- [Teahouse composition, depth and lighting](docs/en/composition.md)

### 5. Specifications and formats

Exact fields, codes, conditions and compatibility rules for authors and developers.

- [Specifications and open formats](docs/en/formats.md)
- [Editorial data contracts](docs/en/contracts.md)
- [Music API and track identity](docs/en/music-api.md)
- [Weather API specification](docs/en/weather-api.md)
- [Weather clients: full contract 1.7](docs/en/weather-client-contract.md)
- [Dynamic theme specification](docs/en/dynamic-wallpapers.md)
- [Dynamic frames, JSON and archives](docs/en/dynamic-api.md)
- [Numeric inputs: units, ranges and conditions](docs/en/numeric-fields.md)
- [Site theme packages](docs/en/theme-packages.md)

### 6. Prompts and practical examples

Original tasks and small reproducible examples after their purpose has been explained.

- [Authoring prompts and image creation](docs/en/authoring-prompts.md)
- [41 original task prompts: inputs, outputs and full tasks](prompts/README.md)
- [Standalone Python examples](examples/README.md)

### 7. Sources and maintenance

Provenance, project links, usage terms and documentation maintenance.

- [Sources and methods](docs/en/sources.md)
- [Project resources and contact](docs/en/resources.md)
- [Usage terms and authorship](docs/en/scope-and-rights.md)
- [Documentation maintenance](docs/en/documentation.md)
- [MIT](LICENSE)

## Application and research repositories

- [GremlinAmp](https://github.com/GremlinEngineering/gremlinamp)
- [Imperial School Views](https://github.com/GremlinEngineering/imperial-school-views)
- [Tennis for Two](https://github.com/malyhind/tennis-for-two)

Russian is canonical. Website pages, PDF and ZIP share the same Markdown and reading order. Prompts retain their original language. See [documentation maintenance](docs/en/documentation.md) for checks and updates.
