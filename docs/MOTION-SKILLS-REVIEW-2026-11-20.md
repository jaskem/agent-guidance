# Review iart-ai motion-skills — 20 november 2026

## Besluit in het kort

- **Selectief verwerken; geen 56 extra methoden of toolpakketten installeren.** De bron levert veel concrete techniek, maar vermengt die met commerciële workflows, vaste smaakregels, platformclaims en soms onjuiste voorbeelden.
- **Interactieve beweging hoort bij `motion-design`.** React presence/layout, GSAP, scroll, CSS/WAAPI, SVG/Lottie en canvas/WebGL zijn implementatietakken binnen die ene methode.
- **Een getimede vertelling of film blijft bij `visual-storytelling`.** Voeg daar alleen relevante formatdetails aan toe: data, kaarten, wiskunde, productdemonstraties, captions, bestaande sprekeropnamen en transparante overlays. De bron voor feiten blijft onafhankelijk van het script.
- **De kern ontbreekt inmiddels niet meer in de onderzochte nieuwe motion-methode.** De in deze batch gelezen kandidaat `skills/motion-design/SKILL.md` met zijn drie inhoudelijke referenties behandelt de belangrijke UI-gaten hieronder. Dat is een inhoudelijke bronvergelijking, geen uitvoerings- of installatiebewijs.
- **Bewijsgrenzen niet importeren uit succesmeldingen van scripts.** Een aangetroffen audit kan na een mislukte livecontrole alsnog `CLEAN` melden. Contact sheets, metadata, daadwerkelijke bediening, afspelen en luisteren bewijzen verschillende zaken.

Dit document is een onderzoeksresultaat. Het accepteert geen externe installatie, nieuwe provider, betaling, publicatie of wijziging van persoonlijke instellingen.

## Bronidentiteit en onderzoeksgrens

De hub is via de GitHub-plugin gelezen op `master`, commit **`e8ba1f4eb2bcca3d1639d7545b9cd2bcfe4a3c6f`**, commitdatum **2026-11-18 06:14:32 UTC**. De bijbehorende tree is `25734a32299e01287680170cfc06e7f90e1749df` en was niet afgekapt.

[Vastgelegde hub](https://github.com/iart-ai/motion-skills/tree/e8ba1f4eb2bcca3d1639d7545b9cd2bcfe4a3c6f) · [README](https://github.com/iart-ai/motion-skills/blob/e8ba1f4eb2bcca3d1639d7545b9cd2bcfe4a3c6f/README.md) · [licentie](https://github.com/iart-ai/motion-skills/blob/e8ba1f4eb2bcca3d1639d7545b9cd2bcfe4a3c6f/LICENSE)

**Belangrijke structuurwijziging:** deze hub bevat 12 tree entries en **geen `SKILL.md`**. Zijn README verwijst naar 19 zelfstandige repositories. Die links zijn gevolgd; per repository is de toenmalige default-branchhead afzonderlijk vastgelegd. Het zijn geen door de hub gelockte submodules. De complete, niet afgekapt geretourneerde pack-trees bevatten samen 641 entries, waaronder **56 `SKILL.md`-bestanden en 98 referentiebestanden**. Er zijn **55 verschillende skillnamen**: `lower-thirds` bestaat in twee inhoudelijk verschillende packs.

Onderzoeksvraag: welke bruikbare beslissingen en technieken ontbreken of verdienen verdieping tegenover de bestaande visuele en UI-methoden, bij welke eigenaar horen ze, en welke tool- en bewijsgrenzen moeten behouden blijven?

De gepubliceerde vergelijkingsbaseline is [jaskem/agent-guidance, commit `12d698190450d6077016d8c62ff94d86376d25b5`](https://github.com/jaskem/agent-guidance/commit/12d698190450d6077016d8c62ff94d86376d25b5). De hoofdsessie heeft vastgesteld dat diens tree overeenkomt met de tijdelijke lokale snapshot `bfd504878f4c9707cd41b3a68f7d32f6be49b2f2` (tree `a3e3a00efcfdbf6823bc791e305575abbd2be9cd`). Tijdens deze review ontstond een nieuwe kandidaat. Deze vergelijking is gebaseerd op de daadwerkelijk gelezen bestanden, niet op een claim dat die nieuwe werkbestanden al in de gepubliceerde baseline zitten.

Gelezen lokale vergelijkingsbasis:

- `visual-storytelling/SKILL.md`, `editorial-html.md`, `web-presentation.md`, `motion-video.md`;
- `design-ui-improvements/SKILL.md`, `art-direction.md`, `visual-handoff.md`;
- `audit-ui-ux/SKILL.md`, `criteria.md`;
- `test-user-flows/SKILL.md`, `flow-evidence.md`;
- `image-art-direction/SKILL.md`;
- de nieuwe kandidaat `motion-design/SKILL.md`, `interaction-contracts.md`, `implementation-branches.md`, `spatial-scenes.md`.

De geaccepteerde sessiecontext gebruikt Agent Operating Guide `instructions_version 0.0.6`. Er zijn voor deze review geen Notion-wijzigingen gedaan.

## Wat werkelijk is gelezen

| Materiaal | Dekking | Betekenis |
| --- | --- | --- |
| Hub | README, LICENSE, showcase HTML, GIF-rendercode, verify-README en drie helpers volledig gelezen | Code en instructies beoordeeld; showcase niet afgespeeld |
| Pack-hoofdteksten | Alle 56 `SKILL.md` en alle 19 root-README's gelezen | Hoofdprocedures en toepassingsgrenzen onderzocht |
| Referenties | 24 van 98 volledig gelezen, hieronder exact vermeld | Gericht op de beslissende UI-, render-, data-, audio- en herstelvragen |
| Overige referenties | 74 geïnventariseerd, niet inhoudelijk gelezen | Geen claim van volledige ondersteunende code- of cookbook-review |
| Licenties | Hub plus 18 packs verwijzen naar dezelfde MIT-tekst/blob | Eén tekst gelezen; identieke Git-blobidentiteit per andere locatie gecontroleerd |
| Gedeelde verify-toolkit | 14 packs bevatten dezelfde vier bestanden als de hub-toolkit | Eén inhoudelijke lezing; overeenkomst vastgesteld via blob-SHA's |
| Extra code | JS render/asset/layout-audit, soundtrack sync-check, lower-thirds render, b-roll transcript/render/template/timingtests, talking-head core/providers/pipeline/render, twee package manifests en CI-workflow gelezen | Statische bronanalyse; niets geïnstalleerd of uitgevoerd |
| Voorbeeldmateriaal | Talking-head `examples/one-idea/README.md` gelezen | Auteursverslag van één run; geen eigen reproductie |
| Media en overige voorbeelden | GIFs, MP4, audio, beelden en overige voorbeeldimplementaties niet bekeken/beluisterd/uitgevoerd | Geen uitspraak over hun feitelijke visuele of auditieve kwaliteit |

230 geselecteerde tekstpaden zijn via de GitHub-plugin opgehaald; dit waren 213 unieke blobs. Elke teruggegeven blob-SHA kwam overeen met de gepinde tree. **Opgehaald is niet hetzelfde als gelezen**: de inhoudelijke leesdekking staat hierboven en in de bijlage. De 19 pack-README's zijn gelezen met exacte dubbele alinea's slechts eenmaal getoond; de bronvolgorde per bestand bleef herkenbaar.

Tijdelijke bronontvangsten en trees staan onder `scratch/motion-review` buiten het canonieke pakket. Dit rapport bevat de blijvende bronpinnen en de inhoudelijke conclusie. Geen upstreamscript, installer, API-call naar een mediaprovider, pakketinstallatie, git-commit of push is uitgevoerd.

## Interactieve motion: bruikbare verdieping en eigenaar

De bestaande UI-methoden behandelen taakgericht ontwerp, behoud van bruikbare dichtheid, identiteit en visuele inspectie al goed. `test-user-flows` behandelt echte bediening en bewijsgrenzen. De onderscheidende aanvulling is **motion als gedrag met een eigen lifecycle**. Een losse animatiecurve of bevroren toestand is daarvoor onvoldoende.

| Techniek uit de bron | Concrete toevoeging die waarde heeft | Eigenaar en beoordeling van de nieuwe kandidaat |
| --- | --- | --- |
| React presence/shared layout | Stabiele keys; een presence-owner die tijdens exit blijft bestaan; bewuste overlap/wait/pop-layout; gedeelde objectidentiteit; tekst- en radiusvervorming bij schaal bewaken; frequente waarden buiten React state houden | `motion-design` implementatiereferentie. Afgedekt. Routerintegratie blijft echte appacceptatie |
| GSAP timelines, SplitText, Flip | Eén eigenaar per timeline/object; scoped context en cleanup; SplitText terugdraaien; fonts en afbeeldingen gereed vóór geometrie; herberekenen bij echte layoutwijziging; listeners en triggers opruimen zonder andere appanimatie te stoppen | `motion-design`. Afgedekt; API-recepten alleen na versiecontrole |
| ScrollTrigger met smooth scrolling | Onderscheid tussen scrollvoortgang, trigger en eventuele smooth-scroll-driver; één gesynchroniseerde klok met juiste eenheden; resize/beelden/fonts, anchors, nested scrollers en terugscrollen meenemen; bruikbaar native alternatief | `motion-design`. Afgedekt. Lenis is een keuze, geen vereiste |
| CSS/WAAPI en FLIP | Nieuwe entry/exit-, discrete display/overlay- en intrinsic-size-functies alleen gebruiken waar ondersteund; gewone eindlayout behouden; vóórmeting, mutatie en nameting groeperen; hit targets en leesvolgorde laten aansluiten | `motion-design`. Afgedekt; geen algemeen compositor- of FPS-bewijs |
| View Transitions | Unieke namen voor gedeelde objecten; gewone navigatie als fallback; werkelijke vooruit/terug/direct-entry controleren; focus en routebetekenis onafhankelijk houden | `motion-design` plus `test-user-flows`. Afgedekt. Geen private-routerfix als standaard |
| Reduced motion en lifecycle | Volledige alternate route met betekenis en content; live OS-voorkeurwijziging stopt en vervangt ook JS/canvas/smooth-scroll; herhaalde toggles, onderbreken en omkeren testen | `motion-design`; toegankelijkheidseisen blijven bij toepasselijke bron/assessment. Afgedekt |
| Canvas/WebGL/R3F | Klok, camera, input, scène en resources gescheiden; DPR/framebuffercoördinaten juist; loops/mixers eerst stoppen; materialen/texturen/render targets apart beheren; gedeelde caches niet blind disposen; remounts vergelijken met stabiele baseline | `motion-design/spatial-scenes`. Afgedekt. Werkende GPU/software-renderer eerst aantonen |
| SVG en Lottie | ViewBox, pivot, padstructuur, IDs en morph-eindpunten controleren; asset load/error, segments, thema's, interactie en fallback behandelen; onzichtbare loops waar passend pauzeren | `motion-design` als optionele tak. Afgedekt. Exportpariteit en lage kosten niet aannemen |

Belangrijkste bronnen: de gepinde web-, webgl-, motion-design- en freelance-packs in de inventaris; met name de in de leesbijlage genoemde referenties.

**Niet uit de bron zelf voldoende verkregen:** een volledig contract voor snelle omkering, dubbele bediening, annulering, focus en bedrijfsstatus. De nieuwe lokale motion-methode voegt juist die gedragsvragen toe. Dat is nuttiger dan de upstreamvolgorde “HTML-demo → drie screenshots → klaar” algemeen overnemen.

## Verhalende HTML en film: resterende gerichte kansen

De bestaande `visual-storytelling`-kern bevat al brontrouw, betekenisvolle transformatie, continuïteit, deterministische tijd, echte audioankers, renderer/encoder-proef en onderscheid tussen preview en export. Deze punten hoeven niet als tweede lifecycle terug te komen.

| Gerichte verdieping | Wat toevoegen of explicieter maken | Eigenaar en grens |
| --- | --- | --- |
| Shotlijst als data | Shot, actiebeat, camera/framing, objecttracking, overgang en eventuele audio-event laten verwijzen naar hetzelfde tijdmodel; toets een still op het beslissende actiepunt tegen de shotbeschrijving | Optionele filmreferentie van `visual-storytelling`; geen verplichte BPM-grid voor iedere vertelling |
| Continu wereldmodel | Objectposities en ankerpunten over shots behouden; camera wisselt van blik, props blijven aan handen/mond/pivots gekoppeld; eerst een terugkerend karakter of complexe asset los inspecteren | Vertelling/film; daadwerkelijke assetfamilie bij `image-art-direction`, identiteit bij bestaande brand/logo-owner |
| Datafilm en batches | Parse/validatie, eenheden, tijdas, ontbrekende waarden, schaal en nummerformaat apart houden van visuele interpolatie. Test echte props, lange labels, lege/all-zero/negatieve data en iedere gevraagde aspectratio vóór grote batches | `visual-storytelling`, met exacte plot/diagramcapaciteit. Geen automatische imputatie, stille afronding of verzonnen precisie |
| Narratie en captions | Tijdstempels herleiden tot de daadwerkelijk gebruikte opname; woordtiming niet uit gelijke verdeling van zinnen verzinnen. Meet clips, reken overlap en frame-afronding mee. Captions en audio blijven optioneel binnen de opdracht | `visual-storytelling`; een taalgeschikt transcriptietool en daadwerkelijke audioinspectie zijn aparte capabilities |
| Bestaande sprekeropname | Per zin kiezen: spreker, overlay of volledig beeld. Oorspronkelijke opname/audio behouden wanneer dat de opdracht is; grafiekstructuur mag voorbereiden, nieuwe feiten/punchlines pas op hun werkelijke anker leesbaar maken | Filmreferentie. De bron noemt zes frames lead expliciet een redactionele default, geen universele waarnemingswet |
| Transparante overlays | Eerste/laatste frame bewust leeg of volgens de montage; hold leesbaar op donker en licht beeld; langste naam; masker/wipe-clipping; codec én werkelijk gedecodeerde alpha inspecteren; doelapp/browser apart controleren | Film/exportreferentie. De nieuwe dedicated lower-thirds-route is iets anders dan de oudere MP4-lower-third in het TikTok-pack |
| Kaarten en wiskunde | Eén projectie/coördinatenmodel voor kaart, pin en route; randgevallen zoals antimeridiaan. Voor wiskunde: correcte formules, termenidentiteit, assen en glyphs vóór animatie. Manim/LaTeX of geodata alleen wanneer aanwezig/nodig | Gerichte narrative-format-referentie; geen algemene plicht tot Earth Studio, AE, Manim of 12fps-stijl |
| Gegenereerde talking head | Onderscheid een bestaande opname verrijken van nieuw spreken genereren; gebruikte audio en teruggeleverde transcriptie niet verwarren met de oorspronkelijke TTS. Wordingverschillen controleren, echte likeness/lipsync alleen na kijken/luisteren beoordelen | Alleen conditionele film/providerroute; geen generieke avatar- of voice-clone-default |
| Herstel van betaalde runs | Bron/plan/asset-fingerprint, exclusieve run-lock, meteen opgeslagen response/request-ID, onzeker resultaat apart van mislukking, bestaande job hervatten; grafische her-render zonder opnieuw providers te betalen | Bestaande work-cycle/herstel-owner houdt algemeen beleid; filmreferentie beschrijft alleen concrete afhankelijkheden |
| Levering en rechten | Werkelijke codec/dimensies/fps/duur/audio/alpha versus gewenste spec; editable bron en relevante data/assets; rechten en bronvermelding per font, afbeelding, geodata, muziek en provider | `visual-storytelling` met native opslag/exportcapability. Providerrechten volgen niet uit de MIT-code of het feit dat iets AI-gegenereerd is |

Voor gegenereerde sprites is het bruikbare idee: **bewerkbare onafhankelijke assets, expliciete pivots, transparantie en een gedeeld compositiecontract**. Gebruik de bestaande native beeldcapability. De externe generatornamen, sleutelroute en regex-achtergrondverwijdering zijn geen vereiste; de hoofdtekst en referentie spreken elkaar daar bovendien tegen.

## Wat niet rechtstreeks overgenomen moet worden

Onderstaande bevindingen zijn statische observaties of expliciet gemarkeerde interpretaties. Er is geen runtimefout gereproduceerd en er is geen platformconformiteit getest.

| Bron en waarneming | Gevolg voor gebruik |
| --- | --- |
| JS `asset-audit.mjs` vangt iedere livecheckfout af en kan daarna bij nul statische hits `CLEAN`/exit 0 geven | “Niet uitgevoerd” moet apart blijven van “geslaagd”. Dit script bewijst dan geen nul netwerkafhankelijkheden |
| Hub `probe-mp4.sh` assert alleen optionele resolutie en fps binnen 0,5; andere codec is waarschuwing, duur wordt alleen geprint | Geen decode-, framecount-, duurcontract-, audio- of afspeelbewijs |
| Hub `seek-shot.sh` gebruikt `npx -y playwright`, een vaste wachttijd en controleert geen toegepast tijdcontract | Geen installer als capability-proef; readiness en juiste frozen state aantonen met beschikbare tools |
| JS `layout-check.mjs` controleert geregistreerde `LAYOUT`-boxen op samples van standaard 0,1 s, met minimumoverlap 4 px | Mist ongeregistreerde inhoud, kleinere/tussenliggende conflicten, glyphproblemen en maskerclipping; geen volledige lay-outgarantie |
| JS `sync-check.mjs` gebruikt energie-onsets met standaard ±100 ms/+6 dB; begin/einde worden uitgesloten en nul events kan succes geven | Redactionele heuristiek, geen luisteren, spraaksync-, luidheidsnorm- of schrikvrij-bewijs |
| B-roll `SKILL.md` noemt lokaal Whisper als eerste keuze; `transcribe.mjs` kiest ElevenLabs eerst wanneer een sleutel beschikbaar is | Providerkeuze en toegestane dataoverdracht expliciet bepalen; sleutelbeschikbaarheid is geen opdracht |
| Countdown schrijft `T × fps` frames voor en toont `ceil(T − frame/fps)`, maar eist 00:00 op het laatste frame | Op `frame = T×fps−1` is de uitkomst 1, geen 0. Eindhold/afronding bewust ontwerpen. Dit volgt uit de getoonde formule |
| Bar-chart-race belooft vloeiende rankinterpolatie, maar kent na sorteren per frame een gehele rang en direct `top` toe | De getoonde code interpoleert waarden, niet de rangpositie. Een overname heeft een echte crossovercontrole nodig |
| Caption-reference gebruikt `useCurrentFrame()` in een geneste `Sequence` terwijl tokenstarts absoluut zijn; het voorbeeld bevat ook een CSS-kleurtransition | Lokale en absolute tijdas eerst verenigen; geen determinismeclaim uit alleen een frameworknaam afleiden |
| CSV-parser zet lege numerieke cellen met `Number()` om en adviseert standaard forward-fill/interpolatie; voorbeeldkleurfunctie gebruikt index in plaats van naam | Databetekenis en missingness aan bronhouder laten; datavolledigheid/stabiele kleuridentiteit niet uit typed props alleen afleiden |
| Next-routevoorbeeld noemt dezelfde `template.tsx` remountend én geschikte persistente exit-owner; FrozenRouter gebruikt `next/dist`-internals | Interne spanning en versieafhankelijkheid. Geen standaardfix kopiëren; echte router/commit/fallback onderzoeken |
| Generative-illustration-main verwijdert achtergrond via bbox, zijn asset-reference waarschuwt daartegen en verwijdert via near-white fill | Beide heuristieken kunnen te veel wissen. Transparant resultaat inspecteren; native editroute blijft eigenaar |
| Veel webvoorbeelden heten self-contained terwijl CDN-scripts, Google Fonts of losse Lottie-assets nodig zijn | Eén HTML-bestand is geen bewijs van offlinewerking. Afhankelijkheden inlinen of de beperking melden en offline testen |
| Veel teksten bevatten vaste duurbanden, “altijd stagger”, “nooit lineair”, een 1/3-regel, vaste grids/persoonlijkheden en universele veilige zones | Inspiratie met taakgerichte keuze. Geen algemene normen; tijd/data/scroll kan juist een constante verhouding vereisen |
| Short-form-teksten noemen exacte kijk-/retentiepercentages; kleur-, AE-, WCAG- en platformspecs worden soms absoluut gesteld | Niet als feiten of garanties overnemen zonder taakgebonden primaire verificatie. Bestaande bronconservativiteit blijft sterker |
| Studio-briefing/revisieteksten verlangen vaste sign-offs, prijzen, contracten en het versturen van mails | Buiten deze visuele methode. Bestaande autorisatie en opdracht blijven leidend; een template is geen verzendopdracht |

De bron heeft tegelijk nuttig tegenbewijs tegen een te brede afwijzing: de recente talking-head-workflow maakt providerkosten, onzekere submissions, hervatten, teruggeleverde audio en beperkte voorbeelddekking juist duidelijk. Die precisie is herbruikbaar; zijn concrete providers blijven conditioneel.

## Tools en grenzen

Dit is een **broninventaris**, geen bevestiging dat onderstaande middelen in de huidige host werken.

| Tak | Bron noemt/vereist | Eerst aantonen; alternatief bij ontbreken |
| --- | --- | --- |
| Web/CSS/WAAPI | Targetbrowser; soms GSAP/React/Motion/Lottie via CDN of projectdependency | Werkelijke versie, feature, controls en fallback; gebruik bestaande stack |
| Browser-frame-export | Node 18+, Playwright/Core, Chrome/Chromium en FFmpeg/ffprobe | Browserstart, assets/fonts/readiness, representatieve framecapture en echte encoding. Bron/HTML kan bruikbaar blijven, MP4 blijft onvoltooid |
| Remotion | React/Remotion, renderer/bundler en soms zod/D3/captions/media-utils | Geïnstalleerde versies en werkelijke props/stills/video; geen automatisch `npx`-downloadpad |
| Manim | Python/Manim CE, FFmpeg; LaTeX voor Tex/MathTex, Pango voor gewone tekst | Echte formule/glyphrender; geen install- of 3Blue1Brown-kwaliteitgarantie |
| WebGL/R3F | GPU of software-WebGL, Three/R3F en eventueel loaders/composer | Echte context, DPR/resize, load/error, disposal en representatieve prestatie; statische bruikbare fallback |
| Alpha-video | Encoder/decoder met gevraagde VP9-alpha of ProRes 4444-ondersteuning | Gedecodeerde pixels en doelapp; upstream Safari-HEVC-route noemt macOS, niet zomaar beschikbaar op Linux |
| Transcriptie | Lokale whisper.cpp + taalgeschikt model, of toegestane externe dienst | Werkelijke engine, timing/tekst/namen/cijfers, luistercheck. Geschatte tijden expliciet houden |
| Talking head | Bronpakket Node 22+, pnpm, FFmpeg/ffprobe, fal en ElevenLabs; package 0.1.1 pinnt `@fal-ai/client` 1.10.1 en `@napi-rs/canvas` 1.0.13 | Providers/limieten/rechten/budget actueel controleren; dit pakket rendert lokaal via native canvas, niet via een browser |
| Kaarten/AE | Geodata/projectie of Earth Studio + Adobe-omgeving en export | Geodata-/beeldrechten, credits en echte camera/overlay-sync; niet noodzakelijk voor een gewone explainer |
| Audio | Web Audio offline score of bestaande/toegestane muziekdienst; mux/decoder | Bestaan van audio, juiste bron/tijdas, meten én werkelijk luisteren apart. Automatische muziekgeneratie is geen standaardvoorwaarde |

Talking-head `--max-video-seconds` beperkt volgens documentatie en code de H3-uitvoerseconden. Het is **geen geldbudget**; TTS wordt al vóór die tijdcontrole gemaakt. Een lokale timeout annuleert de providerjob niet. De bron meldt één beperkte echte voorbeeldrun; voice-clone-herstel wordt daar geen bewezen werkelijke clonekwaliteit door.

## Licentie en hergebruik

- Hub en 18 packs hebben dezelfde **MIT License, Copyright (c) 2026 iart.ai**. Bij het kopiëren van code of substantiële tekst de copyright- en toestemmingsnotice behouden.
- **`generative-illustration-skills` is een uitzondering:** op de onderzochte pin staat geen LICENSE in de volledige tree; ook de gelezen README en `SKILL.md` geven geen licentie. De MIT-notice van een andere repository niet automatisch daarop toepassen. Geen kopieerimport hieruit aanbevelen zonder opheldering; technieken kunnen onafhankelijk worden beschreven.
- Fonts, modelservices, muziek, geodata, screenshots en portret-/stemrechten hebben eigen voorwaarden. De bewering “AI-generated → royalty-free” uit de generatieve bron is geen bruikbare rechtencontrole.
- Dit onderzoek heeft geen upstreamcode of uitvoerbare toolchain in een canonieke skill opgenomen. Het is een beoordeling en mapping, geen pakketupgrade of providerinstallatie.

## Aanbevolen integratie en eerstvolgende stap

1. Behoud de nieuwe `motion-design`-methode als compacte eigenaar van interactieve beweging; de gelezen kandidaat heeft de belangrijke technische takken en gedragscontracten.
2. Verwerk gerichte narratieve formatkeuzes en overlay/providergrenzen conditioneel in `visual-storytelling`-referenties. Herhaal diens bestaande bron-/tijd-/exportregels niet in elk formaat.
3. Houd brand motion tokens bij het bestaande brand/design-systemrecord; beeldassets bij image-art-direction; echte bediening bij test-user-flows; prestatieclaims bij gemeten runtimebewijs.
4. Neem geen commerciële rates, automatische muziek/providerkeuze, contractstops, universele platformgetallen of scripts met te brede succesclaims over.

**Volgende technische stap:** parent vergelijkt de uiteindelijke lokale referenties met deze mapping en controleert uitsluitend de werkelijk gewijzigde routes en gedragscases. Deze review zelf veranderde alleen dit document; er zijn geen foundation-/skilltests, rendering of providerproeven uitgevoerd.

## Bijlage: exacte bronpinnen en skillinventaris

Alle onderstaande hoofdteksten zijn gelezen. De link naar iedere repository gebruikt de vastgelegde commit; skillnamen verwijzen naar `skills/<naam>/SKILL.md` binnen die pin.

| Pack en exacte commit | Commitdatum UTC | Alle gelezen hoofdteksten | Referenties: gelezen/totaal |
| --- | --- | --- | --- |
| [tiktok-video-skills](https://github.com/iart-ai/tiktok-video-skills/tree/88e7152fc2710fa16852d013959cfd988a8adc8b)<br>`88e7152fc2710fa16852d013959cfd988a8adc8b` | 2026-11-11 16:12:54 | [caption-animation](https://github.com/iart-ai/tiktok-video-skills/blob/88e7152fc2710fa16852d013959cfd988a8adc8b/skills/caption-animation/SKILL.md), [countdown-video](https://github.com/iart-ai/tiktok-video-skills/blob/88e7152fc2710fa16852d013959cfd988a8adc8b/skills/countdown-video/SKILL.md), [lower-thirds](https://github.com/iart-ai/tiktok-video-skills/blob/88e7152fc2710fa16852d013959cfd988a8adc8b/skills/lower-thirds/SKILL.md), [short-form-video](https://github.com/iart-ai/tiktok-video-skills/blob/88e7152fc2710fa16852d013959cfd988a8adc8b/skills/short-form-video/SKILL.md) | 1/5 |
| [text-message-video-skills](https://github.com/iart-ai/text-message-video-skills/tree/10ae6bb32e89519c904b8f7950479ff655f839aa)<br>`10ae6bb32e89519c904b8f7950479ff655f839aa` | 2026-11-11 16:13:11 | [text-message-animation](https://github.com/iart-ai/text-message-video-skills/blob/10ae6bb32e89519c904b8f7950479ff655f839aa/skills/text-message-animation/SKILL.md) | 0/2 |
| [youtube-video-skills](https://github.com/iart-ai/youtube-video-skills/tree/7838388571a3a6301bf5633e91941f9dfed0abfd)<br>`7838388571a3a6301bf5633e91941f9dfed0abfd` | 2026-11-11 16:13:29 | [audiogram](https://github.com/iart-ai/youtube-video-skills/blob/7838388571a3a6301bf5633e91941f9dfed0abfd/skills/audiogram/SKILL.md), [youtube-intro-outro](https://github.com/iart-ai/youtube-video-skills/blob/7838388571a3a6301bf5633e91941f9dfed0abfd/skills/youtube-intro-outro/SKILL.md) | 0/2 |
| [ecommerce-video-skills](https://github.com/iart-ai/ecommerce-video-skills/tree/a430fbbb7660783c421ad0a145bcc1c98d6f0b7b)<br>`a430fbbb7660783c421ad0a145bcc1c98d6f0b7b` | 2026-11-11 16:13:42 | [photo-slideshow](https://github.com/iart-ai/ecommerce-video-skills/blob/a430fbbb7660783c421ad0a145bcc1c98d6f0b7b/skills/photo-slideshow/SKILL.md), [product-demo-video](https://github.com/iart-ai/ecommerce-video-skills/blob/a430fbbb7660783c421ad0a145bcc1c98d6f0b7b/skills/product-demo-video/SKILL.md), [promo-video](https://github.com/iart-ai/ecommerce-video-skills/blob/a430fbbb7660783c421ad0a145bcc1c98d6f0b7b/skills/promo-video/SKILL.md) | 0/7 |
| [ad-video-skills](https://github.com/iart-ai/ad-video-skills/tree/cc8071678f4225ee7bdccc4506f2468722bb3515)<br>`cc8071678f4225ee7bdccc4506f2468722bb3515` | 2026-11-11 16:13:51 | [ad-creative-video](https://github.com/iart-ai/ad-video-skills/blob/cc8071678f4225ee7bdccc4506f2468722bb3515/skills/ad-creative-video/SKILL.md), [launch-video](https://github.com/iart-ai/ad-video-skills/blob/cc8071678f4225ee7bdccc4506f2468722bb3515/skills/launch-video/SKILL.md), [testimonial-video](https://github.com/iart-ai/ad-video-skills/blob/cc8071678f4225ee7bdccc4506f2468722bb3515/skills/testimonial-video/SKILL.md) | 0/5 |
| [data-animation-skills](https://github.com/iart-ai/data-animation-skills/tree/6570c0c4fbc9daa8d7ac1f1163a890352344206b)<br>`6570c0c4fbc9daa8d7ac1f1163a890352344206b` | 2026-11-11 16:14:03 | [animated-infographic](https://github.com/iart-ai/data-animation-skills/blob/6570c0c4fbc9daa8d7ac1f1163a890352344206b/skills/animated-infographic/SKILL.md), [chart-animation](https://github.com/iart-ai/data-animation-skills/blob/6570c0c4fbc9daa8d7ac1f1163a890352344206b/skills/chart-animation/SKILL.md), [presentation-video](https://github.com/iart-ai/data-animation-skills/blob/6570c0c4fbc9daa8d7ac1f1163a890352344206b/skills/presentation-video/SKILL.md) | 2/5 |
| [explainer-video-skills](https://github.com/iart-ai/explainer-video-skills/tree/3c13a1bc360c08503f24f9c9a99fda6d3d35de56)<br>`3c13a1bc360c08503f24f9c9a99fda6d3d35de56` | 2026-11-11 16:14:11 | [diagram-animation](https://github.com/iart-ai/explainer-video-skills/blob/3c13a1bc360c08503f24f9c9a99fda6d3d35de56/skills/diagram-animation/SKILL.md), [explainer-video](https://github.com/iart-ai/explainer-video-skills/blob/3c13a1bc360c08503f24f9c9a99fda6d3d35de56/skills/explainer-video/SKILL.md), [isometric-animation](https://github.com/iart-ai/explainer-video-skills/blob/3c13a1bc360c08503f24f9c9a99fda6d3d35de56/skills/isometric-animation/SKILL.md), [whiteboard-animation](https://github.com/iart-ai/explainer-video-skills/blob/3c13a1bc360c08503f24f9c9a99fda6d3d35de56/skills/whiteboard-animation/SKILL.md), [wrapped-video](https://github.com/iart-ai/explainer-video-skills/blob/3c13a1bc360c08503f24f9c9a99fda6d3d35de56/skills/wrapped-video/SKILL.md) | 0/8 |
| [map-animation-skills](https://github.com/iart-ai/map-animation-skills/tree/c8ef8463f5a4a8aa35ff0c6c17f42e52bbf588a5)<br>`c8ef8463f5a4a8aa35ff0c6c17f42e52bbf588a5` | 2026-11-11 16:14:37 | [map-animation](https://github.com/iart-ai/map-animation-skills/blob/c8ef8463f5a4a8aa35ff0c6c17f42e52bbf588a5/skills/map-animation/SKILL.md) | 0/2 |
| [web-animation-skills](https://github.com/iart-ai/web-animation-skills/tree/ed3a045192679b24d32090ee7a983871311ababd)<br>`ed3a045192679b24d32090ee7a983871311ababd` | 2026-11-11 16:14:56 | [60fps-animation](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/60fps-animation/SKILL.md), [accessible-animation](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/accessible-animation/SKILL.md), [ascii-animation](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/ascii-animation/SKILL.md), [glassmorphism](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/glassmorphism/SKILL.md), [gsap-web](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/gsap-web/SKILL.md), [lottie-animation](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/lottie-animation/SKILL.md), [micro-interaction](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/micro-interaction/SKILL.md), [page-transition-animation](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/page-transition-animation/SKILL.md), [svg-animation](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/svg-animation/SKILL.md) | 9/11 |
| [motion-design-skills](https://github.com/iart-ai/motion-design-skills/tree/b85e50c4cef5ff17aa2187a10d49d2dae9226c74)<br>`b85e50c4cef5ff17aa2187a10d49d2dae9226c74` | 2026-11-11 16:15:07 | [after-effects](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/after-effects/SKILL.md), [animation-principles](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/animation-principles/SKILL.md), [beat-sync-editing](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/beat-sync-editing/SKILL.md), [color-motion](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/color-motion/SKILL.md), [logo-animation](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/logo-animation/SKILL.md), [motion-art-direction](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/motion-art-direction/SKILL.md), [motion-background](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/motion-background/SKILL.md), [remotion-video](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/remotion-video/SKILL.md), [shot-composition](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/shot-composition/SKILL.md) | 0/16 |
| [kinetic-typography-skills](https://github.com/iart-ai/kinetic-typography-skills/tree/2b79c81230c6647a344844f9ed53b6fa07f3f1f9)<br>`2b79c81230c6647a344844f9ed53b6fa07f3f1f9` | 2026-11-11 16:15:17 | [kinetic-typography](https://github.com/iart-ai/kinetic-typography-skills/blob/2b79c81230c6647a344844f9ed53b6fa07f3f1f9/skills/kinetic-typography/SKILL.md) | 0/1 |
| [freelance-motion-skills](https://github.com/iart-ai/freelance-motion-skills/tree/9f294eb6df73cde7e2dea235f42275df11a16466)<br>`9f294eb6df73cde7e2dea235f42275df11a16466` | 2026-11-11 16:15:31 | [brand-motion-guidelines](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/brand-motion-guidelines/SKILL.md), [client-revisions](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/client-revisions/SKILL.md), [creative-brief](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/creative-brief/SKILL.md), [motion-pricing](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/motion-pricing/SKILL.md), [video-delivery-specs](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/video-delivery-specs/SKILL.md) | 0/16 |
| [webgl-animation-skills](https://github.com/iart-ai/webgl-animation-skills/tree/0041933813688c357804f7b13dcb85095c5a3210)<br>`0041933813688c357804f7b13dcb85095c5a3210` | 2026-11-11 16:15:52 | [particle-system](https://github.com/iart-ai/webgl-animation-skills/blob/0041933813688c357804f7b13dcb85095c5a3210/skills/particle-system/SKILL.md), [shader-glsl](https://github.com/iart-ai/webgl-animation-skills/blob/0041933813688c357804f7b13dcb85095c5a3210/skills/shader-glsl/SKILL.md), [threejs-animation](https://github.com/iart-ai/webgl-animation-skills/blob/0041933813688c357804f7b13dcb85095c5a3210/skills/threejs-animation/SKILL.md) | 2/4 |
| [manim-skills](https://github.com/iart-ai/manim-skills/tree/3e989cb044f6a6fed8c07b06dddade6e3463d7ac)<br>`3e989cb044f6a6fed8c07b06dddade6e3463d7ac` | 2026-11-11 16:16:02 | [manim](https://github.com/iart-ai/manim-skills/blob/3e989cb044f6a6fed8c07b06dddade6e3463d7ac/skills/manim/SKILL.md) | 0/3 |
| [generative-illustration-skills](https://github.com/iart-ai/generative-illustration-skills/tree/e7d62437c875fc8ad5eff6e90fe0e25b30e43933)<br>`e7d62437c875fc8ad5eff6e90fe0e25b30e43933` | 2026-06-30 14:47:25 | [generative-illustration](https://github.com/iart-ai/generative-illustration-skills/blob/e7d62437c875fc8ad5eff6e90fe0e25b30e43933/skills/generative-illustration/SKILL.md) | 3/3 |
| [javascript-animation-skills](https://github.com/iart-ai/javascript-animation-skills/tree/060f7467a6e5ae5b57c90c9cb1b3508c13b88e49)<br>`060f7467a6e5ae5b57c90c9cb1b3508c13b88e49` | 2026-11-11 16:16:20 | [javascript-animation](https://github.com/iart-ai/javascript-animation-skills/blob/060f7467a6e5ae5b57c90c9cb1b3508c13b88e49/skills/javascript-animation/SKILL.md), [soundtrack](https://github.com/iart-ai/javascript-animation-skills/blob/060f7467a6e5ae5b57c90c9cb1b3508c13b88e49/skills/soundtrack/SKILL.md) | 5/6 |
| [lower-thirds-skills](https://github.com/iart-ai/lower-thirds-skills/tree/58d3623da95a2c97a4890a2d3f6d9d67e040b3d7)<br>`58d3623da95a2c97a4890a2d3f6d9d67e040b3d7` | 2026-11-11 16:16:29 | [lower-thirds](https://github.com/iart-ai/lower-thirds-skills/blob/58d3623da95a2c97a4890a2d3f6d9d67e040b3d7/skills/lower-thirds/SKILL.md) | 1/1 |
| [b-roll-skills](https://github.com/iart-ai/b-roll-skills/tree/bcd56742a8a99edaa699a6f7bc5a45922a8ec567)<br>`bcd56742a8a99edaa699a6f7bc5a45922a8ec567` | 2026-11-11 16:16:47 | [talking-head-b-roll](https://github.com/iart-ai/b-roll-skills/blob/bcd56742a8a99edaa699a6f7bc5a45922a8ec567/skills/talking-head-b-roll/SKILL.md) | 0/0 |
| [talking-head-skills](https://github.com/iart-ai/talking-head-skills/tree/eac1f6b01467f6f95d8ab7602310ba0ff67ed91b)<br>`eac1f6b01467f6f95d8ab7602310ba0ff67ed91b` | 2026-11-11 16:16:56 | [talking-head](https://github.com/iart-ai/talking-head-skills/blob/eac1f6b01467f6f95d8ab7602310ba0ff67ed91b/skills/talking-head/SKILL.md) | 1/1 |

Alle pack-defaultbranches waren `main`. De hub gebruikt `master`. De volledige commit hierboven is de bronidentiteit; het woord “current” geldt uitsluitend voor het geobserveerde onderzoeksoment, niet voor toekomstige heads.

## Bijlage: gelezen ondersteuning

De 24 volledig gelezen referenties volgen hieronder met hun exacte gepinde bronlinks. Alle overige 74 referenties zijn alleen geïnventariseerd; de laatste bijlage noemt ze expliciet.

### Volledig gelezen referenties (24)

**web-animation-skills**

- [skills/60fps-animation/references/patterns-and-profiling.md](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/60fps-animation/references/patterns-and-profiling.md)
- [skills/accessible-animation/references/patterns.md](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/accessible-animation/references/patterns.md)
- [skills/gsap-web/references/scrolltrigger-cookbook.md](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/gsap-web/references/scrolltrigger-cookbook.md)
- [skills/gsap-web/references/scrolltrigger-lenis.md](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/gsap-web/references/scrolltrigger-lenis.md)
- [skills/micro-interaction/references/css-recipes.md](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/micro-interaction/references/css-recipes.md)
- [skills/micro-interaction/references/framer-motion-recipes.md](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/micro-interaction/references/framer-motion-recipes.md)
- [skills/page-transition-animation/references/full-examples.md](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/page-transition-animation/references/full-examples.md)
- [skills/svg-animation/references/svg-techniques.md](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/svg-animation/references/svg-techniques.md)
- [skills/lottie-animation/references/integration-and-export.md](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/lottie-animation/references/integration-and-export.md)

**webgl-animation-skills**

- [skills/threejs-animation/references/resource-disposal.md](https://github.com/iart-ai/webgl-animation-skills/blob/0041933813688c357804f7b13dcb85095c5a3210/skills/threejs-animation/references/resource-disposal.md)
- [skills/threejs-animation/references/r3f-and-perf.md](https://github.com/iart-ai/webgl-animation-skills/blob/0041933813688c357804f7b13dcb85095c5a3210/skills/threejs-animation/references/r3f-and-perf.md)

**javascript-animation-skills**

- [skills/javascript-animation/references/storyboard.md](https://github.com/iart-ai/javascript-animation-skills/blob/060f7467a6e5ae5b57c90c9cb1b3508c13b88e49/skills/javascript-animation/references/storyboard.md)
- [skills/javascript-animation/references/forms.md](https://github.com/iart-ai/javascript-animation-skills/blob/060f7467a6e5ae5b57c90c9cb1b3508c13b88e49/skills/javascript-animation/references/forms.md)
- [skills/javascript-animation/references/qc.md](https://github.com/iart-ai/javascript-animation-skills/blob/060f7467a6e5ae5b57c90c9cb1b3508c13b88e49/skills/javascript-animation/references/qc.md)
- [skills/javascript-animation/references/character.md](https://github.com/iart-ai/javascript-animation-skills/blob/060f7467a6e5ae5b57c90c9cb1b3508c13b88e49/skills/javascript-animation/references/character.md)
- [skills/javascript-animation/references/techniques.md](https://github.com/iart-ai/javascript-animation-skills/blob/060f7467a6e5ae5b57c90c9cb1b3508c13b88e49/skills/javascript-animation/references/techniques.md)

**generative-illustration-skills**

- [skills/generative-illustration/references/asset-pipeline.md](https://github.com/iart-ai/generative-illustration-skills/blob/e7d62437c875fc8ad5eff6e90fe0e25b30e43933/skills/generative-illustration/references/asset-pipeline.md)
- [skills/generative-illustration/references/render-harness.md](https://github.com/iart-ai/generative-illustration-skills/blob/e7d62437c875fc8ad5eff6e90fe0e25b30e43933/skills/generative-illustration/references/render-harness.md)
- [skills/generative-illustration/references/craft.md](https://github.com/iart-ai/generative-illustration-skills/blob/e7d62437c875fc8ad5eff6e90fe0e25b30e43933/skills/generative-illustration/references/craft.md)

**lower-thirds-skills**

- [skills/lower-thirds/references/delivery.md](https://github.com/iart-ai/lower-thirds-skills/blob/58d3623da95a2c97a4890a2d3f6d9d67e040b3d7/skills/lower-thirds/references/delivery.md)

**data-animation-skills**

- [skills/chart-animation/references/data-pipeline.md](https://github.com/iart-ai/data-animation-skills/blob/6570c0c4fbc9daa8d7ac1f1163a890352344206b/skills/chart-animation/references/data-pipeline.md)
- [skills/chart-animation/references/bar-chart-race.md](https://github.com/iart-ai/data-animation-skills/blob/6570c0c4fbc9daa8d7ac1f1163a890352344206b/skills/chart-animation/references/bar-chart-race.md)

**tiktok-video-skills**

- [skills/caption-animation/references/word-timed-captions.md](https://github.com/iart-ai/tiktok-video-skills/blob/88e7152fc2710fa16852d013959cfd988a8adc8b/skills/caption-animation/references/word-timed-captions.md)

**talking-head-skills**

- [skills/talking-head/references/workflow.md](https://github.com/iart-ai/talking-head-skills/blob/eac1f6b01467f6f95d8ab7602310ba0ff67ed91b/skills/talking-head/references/workflow.md)

### Extra volledig gelezen code, manifests en voorbeeldverslag (17)

**javascript-animation-skills**

- [skills/javascript-animation/scripts/render.mjs](https://github.com/iart-ai/javascript-animation-skills/blob/060f7467a6e5ae5b57c90c9cb1b3508c13b88e49/skills/javascript-animation/scripts/render.mjs)
- [skills/javascript-animation/scripts/asset-audit.mjs](https://github.com/iart-ai/javascript-animation-skills/blob/060f7467a6e5ae5b57c90c9cb1b3508c13b88e49/skills/javascript-animation/scripts/asset-audit.mjs)
- [skills/javascript-animation/scripts/layout-check.mjs](https://github.com/iart-ai/javascript-animation-skills/blob/060f7467a6e5ae5b57c90c9cb1b3508c13b88e49/skills/javascript-animation/scripts/layout-check.mjs)
- [skills/soundtrack/scripts/sync-check.mjs](https://github.com/iart-ai/javascript-animation-skills/blob/060f7467a6e5ae5b57c90c9cb1b3508c13b88e49/skills/soundtrack/scripts/sync-check.mjs)

**lower-thirds-skills**

- [skills/lower-thirds/scripts/render.mjs](https://github.com/iart-ai/lower-thirds-skills/blob/58d3623da95a2c97a4890a2d3f6d9d67e040b3d7/skills/lower-thirds/scripts/render.mjs)

**b-roll-skills**

- [skills/talking-head-b-roll/scripts/transcribe.mjs](https://github.com/iart-ai/b-roll-skills/blob/bcd56742a8a99edaa699a6f7bc5a45922a8ec567/skills/talking-head-b-roll/scripts/transcribe.mjs)
- [skills/talking-head-b-roll/scripts/render.mjs](https://github.com/iart-ai/b-roll-skills/blob/bcd56742a8a99edaa699a6f7bc5a45922a8ec567/skills/talking-head-b-roll/scripts/render.mjs)
- [skills/talking-head-b-roll/scripts/timing.test.mjs](https://github.com/iart-ai/b-roll-skills/blob/bcd56742a8a99edaa699a6f7bc5a45922a8ec567/skills/talking-head-b-roll/scripts/timing.test.mjs)
- [skills/talking-head-b-roll/templates/b-roll.html](https://github.com/iart-ai/b-roll-skills/blob/bcd56742a8a99edaa699a6f7bc5a45922a8ec567/skills/talking-head-b-roll/templates/b-roll.html)

**talking-head-skills**

- [skills/talking-head/scripts/core.mjs](https://github.com/iart-ai/talking-head-skills/blob/eac1f6b01467f6f95d8ab7602310ba0ff67ed91b/skills/talking-head/scripts/core.mjs)
- [skills/talking-head/scripts/providers.mjs](https://github.com/iart-ai/talking-head-skills/blob/eac1f6b01467f6f95d8ab7602310ba0ff67ed91b/skills/talking-head/scripts/providers.mjs)
- [skills/talking-head/scripts/pipeline.mjs](https://github.com/iart-ai/talking-head-skills/blob/eac1f6b01467f6f95d8ab7602310ba0ff67ed91b/skills/talking-head/scripts/pipeline.mjs)
- [skills/talking-head/scripts/render.mjs](https://github.com/iart-ai/talking-head-skills/blob/eac1f6b01467f6f95d8ab7602310ba0ff67ed91b/skills/talking-head/scripts/render.mjs)
- [package.json](https://github.com/iart-ai/talking-head-skills/blob/eac1f6b01467f6f95d8ab7602310ba0ff67ed91b/package.json)
- [skills/talking-head/package.json](https://github.com/iart-ai/talking-head-skills/blob/eac1f6b01467f6f95d8ab7602310ba0ff67ed91b/skills/talking-head/package.json)
- [.github/workflows/check.yml](https://github.com/iart-ai/talking-head-skills/blob/eac1f6b01467f6f95d8ab7602310ba0ff67ed91b/.github/workflows/check.yml)
- [examples/one-idea/README.md](https://github.com/iart-ai/talking-head-skills/blob/eac1f6b01467f6f95d8ab7602310ba0ff67ed91b/examples/one-idea/README.md)

### Volledig gelezen hubmateriaal (8)

- [README.md](https://github.com/iart-ai/motion-skills/blob/e8ba1f4eb2bcca3d1639d7545b9cd2bcfe4a3c6f/README.md)
- [LICENSE](https://github.com/iart-ai/motion-skills/blob/e8ba1f4eb2bcca3d1639d7545b9cd2bcfe4a3c6f/LICENSE)
- [showcase.html](https://github.com/iart-ai/motion-skills/blob/e8ba1f4eb2bcca3d1639d7545b9cd2bcfe4a3c6f/showcase.html)
- [tools/showcase-to-gif.mjs](https://github.com/iart-ai/motion-skills/blob/e8ba1f4eb2bcca3d1639d7545b9cd2bcfe4a3c6f/tools/showcase-to-gif.mjs)
- [tools/verify/README.md](https://github.com/iart-ai/motion-skills/blob/e8ba1f4eb2bcca3d1639d7545b9cd2bcfe4a3c6f/tools/verify/README.md)
- [tools/verify/contact-sheet.sh](https://github.com/iart-ai/motion-skills/blob/e8ba1f4eb2bcca3d1639d7545b9cd2bcfe4a3c6f/tools/verify/contact-sheet.sh)
- [tools/verify/probe-mp4.sh](https://github.com/iart-ai/motion-skills/blob/e8ba1f4eb2bcca3d1639d7545b9cd2bcfe4a3c6f/tools/verify/probe-mp4.sh)
- [tools/verify/seek-shot.sh](https://github.com/iart-ai/motion-skills/blob/e8ba1f4eb2bcca3d1639d7545b9cd2bcfe4a3c6f/tools/verify/seek-shot.sh)

### Alleen geïnventariseerde referenties (74)

Deze bestanden zijn aanwezig in de gepinde trees, maar hun inhoud is niet beoordeeld. Ook eventuele scripts, templates, skill-README's en voorbeelden buiten de expliciet gelezen lijsten zijn geen onderdeel van de inhoudelijke review. Ophalen voor onderzoek verandert die status niet.

**tiktok-video-skills (4)**

- [skills/countdown-video/references/countdown-cookbook.md](https://github.com/iart-ai/tiktok-video-skills/blob/88e7152fc2710fa16852d013959cfd988a8adc8b/skills/countdown-video/references/countdown-cookbook.md)
- [skills/countdown-video/references/digit-flip.md](https://github.com/iart-ai/tiktok-video-skills/blob/88e7152fc2710fa16852d013959cfd988a8adc8b/skills/countdown-video/references/digit-flip.md)
- [skills/lower-thirds/references/lower-third-component.md](https://github.com/iart-ai/tiktok-video-skills/blob/88e7152fc2710fa16852d013959cfd988a8adc8b/skills/lower-thirds/references/lower-third-component.md)
- [skills/short-form-video/references/retention-pacing.md](https://github.com/iart-ai/tiktok-video-skills/blob/88e7152fc2710fa16852d013959cfd988a8adc8b/skills/short-form-video/references/retention-pacing.md)

**text-message-video-skills (2)**

- [skills/text-message-animation/references/bubble-recipes.md](https://github.com/iart-ai/text-message-video-skills/blob/10ae6bb32e89519c904b8f7950479ff655f839aa/skills/text-message-animation/references/bubble-recipes.md)
- [skills/text-message-animation/references/data-driven.md](https://github.com/iart-ai/text-message-video-skills/blob/10ae6bb32e89519c904b8f7950479ff655f839aa/skills/text-message-animation/references/data-driven.md)

**youtube-video-skills (2)**

- [skills/audiogram/references/waveform-render.md](https://github.com/iart-ai/youtube-video-skills/blob/7838388571a3a6301bf5633e91941f9dfed0abfd/skills/audiogram/references/waveform-render.md)
- [skills/youtube-intro-outro/references/intro-outro.md](https://github.com/iart-ai/youtube-video-skills/blob/7838388571a3a6301bf5633e91941f9dfed0abfd/skills/youtube-intro-outro/references/intro-outro.md)

**ecommerce-video-skills (7)**

- [skills/photo-slideshow/references/aspect-and-layout.md](https://github.com/iart-ai/ecommerce-video-skills/blob/a430fbbb7660783c421ad0a145bcc1c98d6f0b7b/skills/photo-slideshow/references/aspect-and-layout.md)
- [skills/photo-slideshow/references/ken-burns.md](https://github.com/iart-ai/ecommerce-video-skills/blob/a430fbbb7660783c421ad0a145bcc1c98d6f0b7b/skills/photo-slideshow/references/ken-burns.md)
- [skills/photo-slideshow/references/templating-folder.md](https://github.com/iart-ai/ecommerce-video-skills/blob/a430fbbb7660783c421ad0a145bcc1c98d6f0b7b/skills/photo-slideshow/references/templating-folder.md)
- [skills/photo-slideshow/references/timing-and-audio.md](https://github.com/iart-ai/ecommerce-video-skills/blob/a430fbbb7660783c421ad0a145bcc1c98d6f0b7b/skills/photo-slideshow/references/timing-and-audio.md)
- [skills/product-demo-video/references/annotation-and-transitions.md](https://github.com/iart-ai/ecommerce-video-skills/blob/a430fbbb7660783c421ad0a145bcc1c98d6f0b7b/skills/product-demo-video/references/annotation-and-transitions.md)
- [skills/product-demo-video/references/screenshot-demo.md](https://github.com/iart-ai/ecommerce-video-skills/blob/a430fbbb7660783c421ad0a145bcc1c98d6f0b7b/skills/product-demo-video/references/screenshot-demo.md)
- [skills/promo-video/references/promo-components.md](https://github.com/iart-ai/ecommerce-video-skills/blob/a430fbbb7660783c421ad0a145bcc1c98d6f0b7b/skills/promo-video/references/promo-components.md)

**ad-video-skills (5)**

- [skills/ad-creative-video/references/batch-ad-pipeline.md](https://github.com/iart-ai/ad-video-skills/blob/cc8071678f4225ee7bdccc4506f2468722bb3515/skills/ad-creative-video/references/batch-ad-pipeline.md)
- [skills/ad-creative-video/references/platform-specs.md](https://github.com/iart-ai/ad-video-skills/blob/cc8071678f4225ee7bdccc4506f2468722bb3515/skills/ad-creative-video/references/platform-specs.md)
- [skills/launch-video/references/launch-structure.md](https://github.com/iart-ai/ad-video-skills/blob/cc8071678f4225ee7bdccc4506f2468722bb3515/skills/launch-video/references/launch-structure.md)
- [skills/testimonial-video/references/batch-and-typography.md](https://github.com/iart-ai/ad-video-skills/blob/cc8071678f4225ee7bdccc4506f2468722bb3515/skills/testimonial-video/references/batch-and-typography.md)
- [skills/testimonial-video/references/quote-card.md](https://github.com/iart-ai/ad-video-skills/blob/cc8071678f4225ee7bdccc4506f2468722bb3515/skills/testimonial-video/references/quote-card.md)

**data-animation-skills (3)**

- [skills/animated-infographic/references/sequenced-infographic.md](https://github.com/iart-ai/data-animation-skills/blob/6570c0c4fbc9daa8d7ac1f1163a890352344206b/skills/animated-infographic/references/sequenced-infographic.md)
- [skills/presentation-video/references/sequencing.md](https://github.com/iart-ai/data-animation-skills/blob/6570c0c4fbc9daa8d7ac1f1163a890352344206b/skills/presentation-video/references/sequencing.md)
- [skills/presentation-video/references/slide-components.md](https://github.com/iart-ai/data-animation-skills/blob/6570c0c4fbc9daa8d7ac1f1163a890352344206b/skills/presentation-video/references/slide-components.md)

**explainer-video-skills (8)**

- [skills/diagram-animation/references/diagram-and-chart-recipes.md](https://github.com/iart-ai/explainer-video-skills/blob/3c13a1bc360c08503f24f9c9a99fda6d3d35de56/skills/diagram-animation/references/diagram-and-chart-recipes.md)
- [skills/explainer-video/references/script-to-screen-workflow.md](https://github.com/iart-ai/explainer-video-skills/blob/3c13a1bc360c08503f24f9c9a99fda6d3d35de56/skills/explainer-video/references/script-to-screen-workflow.md)
- [skills/isometric-animation/references/isometric-recipes.md](https://github.com/iart-ai/explainer-video-skills/blob/3c13a1bc360c08503f24f9c9a99fda6d3d35de56/skills/isometric-animation/references/isometric-recipes.md)
- [skills/whiteboard-animation/references/draw-on-recipes.md](https://github.com/iart-ai/explainer-video-skills/blob/3c13a1bc360c08503f24f9c9a99fda6d3d35de56/skills/whiteboard-animation/references/draw-on-recipes.md)
- [skills/whiteboard-animation/references/whiteboard-pipeline.md](https://github.com/iart-ai/explainer-video-skills/blob/3c13a1bc360c08503f24f9c9a99fda6d3d35de56/skills/whiteboard-animation/references/whiteboard-pipeline.md)
- [skills/wrapped-video/references/batch-pipeline.md](https://github.com/iart-ai/explainer-video-skills/blob/3c13a1bc360c08503f24f9c9a99fda6d3d35de56/skills/wrapped-video/references/batch-pipeline.md)
- [skills/wrapped-video/references/remotion-recipes.md](https://github.com/iart-ai/explainer-video-skills/blob/3c13a1bc360c08503f24f9c9a99fda6d3d35de56/skills/wrapped-video/references/remotion-recipes.md)
- [skills/wrapped-video/references/scene-grammar.md](https://github.com/iart-ai/explainer-video-skills/blob/3c13a1bc360c08503f24f9c9a99fda6d3d35de56/skills/wrapped-video/references/scene-grammar.md)

**map-animation-skills (2)**

- [skills/map-animation/references/earth-studio-to-ae.md](https://github.com/iart-ai/map-animation-skills/blob/c8ef8463f5a4a8aa35ff0c6c17f42e52bbf588a5/skills/map-animation/references/earth-studio-to-ae.md)
- [skills/map-animation/references/vector-maps.md](https://github.com/iart-ai/map-animation-skills/blob/c8ef8463f5a4a8aa35ff0c6c17f42e52bbf588a5/skills/map-animation/references/vector-maps.md)

**web-animation-skills (2)**

- [skills/ascii-animation/references/rendering.md](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/ascii-animation/references/rendering.md)
- [skills/glassmorphism/references/glass-recipes.md](https://github.com/iart-ai/web-animation-skills/blob/ed3a045192679b24d32090ee7a983871311ababd/skills/glassmorphism/references/glass-recipes.md)

**motion-design-skills (16)**

- [skills/after-effects/references/export-recipes.md](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/after-effects/references/export-recipes.md)
- [skills/after-effects/references/expression-library.md](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/after-effects/references/expression-library.md)
- [skills/after-effects/references/expressions.md](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/after-effects/references/expressions.md)
- [skills/after-effects/references/performance-triage.md](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/after-effects/references/performance-triage.md)
- [skills/after-effects/references/project-hygiene.md](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/after-effects/references/project-hygiene.md)
- [skills/animation-principles/references/easing-curves.md](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/animation-principles/references/easing-curves.md)
- [skills/animation-principles/references/easing-graph-editor.md](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/animation-principles/references/easing-graph-editor.md)
- [skills/animation-principles/references/twelve-principles.md](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/animation-principles/references/twelve-principles.md)
- [skills/beat-sync-editing/references/editing-techniques.md](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/beat-sync-editing/references/editing-techniques.md)
- [skills/color-motion/references/color-management.md](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/color-motion/references/color-management.md)
- [skills/color-motion/references/palettes-and-interpolation.md](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/color-motion/references/palettes-and-interpolation.md)
- [skills/logo-animation/references/logo-patterns.md](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/logo-animation/references/logo-patterns.md)
- [skills/motion-art-direction/references/direction-playbook.md](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/motion-art-direction/references/direction-playbook.md)
- [skills/motion-background/references/background-recipes.md](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/motion-background/references/background-recipes.md)
- [skills/remotion-video/references/api-and-patterns.md](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/remotion-video/references/api-and-patterns.md)
- [skills/shot-composition/references/camera-and-grids.md](https://github.com/iart-ai/motion-design-skills/blob/b85e50c4cef5ff17aa2187a10d49d2dae9226c74/skills/shot-composition/references/camera-and-grids.md)

**kinetic-typography-skills (1)**

- [skills/kinetic-typography/references/reveal-recipes.md](https://github.com/iart-ai/kinetic-typography-skills/blob/2b79c81230c6647a344844f9ed53b6fa07f3f1f9/skills/kinetic-typography/references/reveal-recipes.md)

**freelance-motion-skills (16)**

- [skills/brand-motion-guidelines/references/dos-and-donts.md](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/brand-motion-guidelines/references/dos-and-donts.md)
- [skills/brand-motion-guidelines/references/full-template.md](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/brand-motion-guidelines/references/full-template.md)
- [skills/brand-motion-guidelines/references/token-reference.md](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/brand-motion-guidelines/references/token-reference.md)
- [skills/client-revisions/references/email-templates.md](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/client-revisions/references/email-templates.md)
- [skills/client-revisions/references/feedback-translator.md](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/client-revisions/references/feedback-translator.md)
- [skills/client-revisions/references/sow-clauses.md](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/client-revisions/references/sow-clauses.md)
- [skills/creative-brief/references/clarifying-questions.md](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/creative-brief/references/clarifying-questions.md)
- [skills/creative-brief/references/vague-translator.md](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/creative-brief/references/vague-translator.md)
- [skills/creative-brief/references/worked-example.md](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/creative-brief/references/worked-example.md)
- [skills/motion-pricing/references/quote-template.md](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/motion-pricing/references/quote-template.md)
- [skills/motion-pricing/references/rate-card.md](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/motion-pricing/references/rate-card.md)
- [skills/motion-pricing/references/worked-example.md](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/motion-pricing/references/worked-example.md)
- [skills/video-delivery-specs/references/platform-specs.md](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/video-delivery-specs/references/platform-specs.md)
- [skills/video-delivery-specs/references/qc-checklist.md](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/video-delivery-specs/references/qc-checklist.md)
- [skills/video-delivery-specs/references/repurposing-matrix.md](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/video-delivery-specs/references/repurposing-matrix.md)
- [skills/video-delivery-specs/references/safe-areas.md](https://github.com/iart-ai/freelance-motion-skills/blob/9f294eb6df73cde7e2dea235f42275df11a16466/skills/video-delivery-specs/references/safe-areas.md)

**webgl-animation-skills (2)**

- [skills/particle-system/references/particle-recipes.md](https://github.com/iart-ai/webgl-animation-skills/blob/0041933813688c357804f7b13dcb85095c5a3210/skills/particle-system/references/particle-recipes.md)
- [skills/shader-glsl/references/glsl-cookbook.md](https://github.com/iart-ai/webgl-animation-skills/blob/0041933813688c357804f7b13dcb85095c5a3210/skills/shader-glsl/references/glsl-cookbook.md)

**manim-skills (3)**

- [skills/manim/references/3d-and-camera.md](https://github.com/iart-ai/manim-skills/blob/3e989cb044f6a6fed8c07b06dddade6e3463d7ac/skills/manim/references/3d-and-camera.md)
- [skills/manim/references/graphs-and-updaters.md](https://github.com/iart-ai/manim-skills/blob/3e989cb044f6a6fed8c07b06dddade6e3463d7ac/skills/manim/references/graphs-and-updaters.md)
- [skills/manim/references/math-and-text.md](https://github.com/iart-ai/manim-skills/blob/3e989cb044f6a6fed8c07b06dddade6e3463d7ac/skills/manim/references/math-and-text.md)

**javascript-animation-skills (1)**

- [skills/soundtrack/references/ai-music.md](https://github.com/iart-ai/javascript-animation-skills/blob/060f7467a6e5ae5b57c90c9cb1b3508c13b88e49/skills/soundtrack/references/ai-music.md)
