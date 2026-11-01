GAME-SPECIFIC ARTISTIC WORLD & ERA:
Identify the visual world, release year, and region of this game, then choose a period-appropriate advertising style (1970s magazine art, 1980s airbrush/acrylic poster, 1990s anime/game-box illustration, etc.). Region, year, and platform provide context without overriding art direction. Describe setting, rendering language, line/shading, palette, equipment vocabulary, and mood. Integrate Gremlin and Fox while preserving reference anatomy. Do not force generic dark fantasy, cinematic realism, steampunk, or universal distressed retro styles.

UNIFIED MEDIUM & ERA-APPROPRIATE LIGHTING:
ALL elements in the image—including the Gremlin, vehicles, background, explosion effects, enemies, and typography—MUST be rendered in the EXACT SAME artistic medium, brush technique, and color palette. Adapt the rendering technique and lighting strictly to the game's release era. NEVER use modern 3D soft bounce light, glossy digital render effects, or raytraced lighting that clash with period print techniques. Use bold graphic contrast and era-accurate shading where characters and scene elements share the identical physical medium.

REIMAGINING MINIMALIST AND ARCADE GRAPHICS:
For primitive or low-res games (e.g., 1970s–1980s arcades or 8-bit systems), NEVER output raw pixelated 8-bit sprites, blocky artifacts, or arcade scanner/HUD frames. ALL gameplay mechanics (enemies, lasers, explosions, terrain, humans) MUST be fully reimagined as high-quality illustrated artwork sharing the identical rendering style, line weight, and lighting as the main character.

ONE UNIFIED PHYSICAL SCENE:
Construct ONE physical scene with Gremlin (and Fox if included) INSIDE the action. REJECT isolated portrait frames, UI windows, sidebars, or floating panels. REJECT gameplay screenshots surrounded by avatars. Seamlessly blend lighting and graphic edges across the cockpit, character, and background. Establish focal hierarchy, movement, scale, and depth.
When include_fox=true, integrate BOTH characters into the scene naturally. Describe pose, support/cockpit seating, scale, and occlusion.

ERGONOMICS AND OBJECT INTEGRITY:
All devices, weapons, controls, and equipment must maintain strict geometric validity and ergonomic alignment. Control surfaces, buttons, screens, and handles MUST point naturally toward the character, NEVER artificially turned flat toward the camera.

LETTERING & METADATA:
Use poster_text / expected_text as authoritative lettering. Arcade platform is "Arcade". Title contains only game name; year and platform form a subordinate block. Render each supplied string exactly once. Do not add fake UI, score counters, or extra text.

LAYOUT FREEDOM:
Title, platform, and year placement is an editorial design choice (bottom, side, or top). Ensure text is clear, unclipped, and readable.

Deliverable: 1024×1536 pixels, portrait 2:3, flat advertising poster. Use gremlin_fox_reference.png for identity:
- Gremlin: compact sturdy body, broad head, large pointed sideways ears (orange inner fur), amber-golden eyes, short broad nose, wide mouth with small teeth, green skin. MUST ALWAYS wear clearly visible physical headwear (helmet, cap, bandanna, etc.).
- Fox (when include_fox=true): adult feminine proportions, full layered orange-red hair, pointed upright ears, amber-brown eyes, short muzzle, single bushy white-tipped tail.

Return JSON:
{
  "art_direction": "Period advertising treatment",
  "scene": "Описание сцены по-русски",
  "editorial_connection": "Связь с мнением статьи",
  "recognition": "Узнаваемые детали игры",
  "characters": {
    "gremlin": "Identity anchors, role, pose, costume, mandatory headwear",
    "fox": "Adult identity anchors, role, pose, costume, or null"
  },
  "layout": {
    "composition": "Arrangement, scale, focus",
    "title": "Placement, lettering, size, color",
    "platform": "Subordinate placement",
    "year": "Subordinate placement"
  },
  "visual_prompt": "Complete English rendering brief for unified poster"
}