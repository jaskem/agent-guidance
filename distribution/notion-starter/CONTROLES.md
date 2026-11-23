# Acceptatie en gerichte controles

Deze controles vullen [de algemene installatie](../../INSTALL.md) aan voor de expliciet gekozen Notion-bestemming. Gebruik de gekozen commit en catalogus, plus `BRONNEN.json` bij een overdrachtspakket. Dit document stelt geen vaste pakketomvang of setupversie vast.

Noteer per controle de echte bron/uitvoer en de grens. 'Niet beschikbaar' en 'nog te doen' zijn geldige uitkomsten en worden geen geslaagde controle genoemd.

| Controle | Verwacht aantoonbaar resultaat |
| --- | --- |
| Bestandsintegriteit | Bij een pakket: alle payloadbestanden hebben de verwachte SHA-256 uit BRONNEN.json; bij een checkout: gekozen bronbestanden horen bij de exacte commit; geen ontbrekende of extra ongeïnspecteerde import |
| Juiste eigenaar | Alleen de geverifieerde werkruimte en bestemmingen die de ontvanger voor deze installatie koos, zijn gewijzigd |
| Eigen Guide | Bestaande ID waar mogelijk behouden; bestemmingen en werkelijk geaccepteerde setupversie teruggelezen; geen open verplichte placeholder; een nieuwe setupversie heeft aantoonbare toestemming |
| Persoonlijke inhoud | Alle geraakte persoonlijke delen behouden; geen eigen notitie/project als opruimobject gebruikt |
| Oude versus nieuwe route | Eén actieve algemene standaardroute; vervangen routes hebben een verklaarde opvolger |
| Databaseaansluiting | Bestaande gegevens, eigenschappen, weergaven en relaties behouden; geen linked view voor een zelfstandige database aangezien |
| Herstelpunt | Vóór mutaties opgeslagen en teruggelezen; niet-exporteerbare delen niet onherstelbaar gewijzigd |
| Catalogus en selectie | Catalogusomvang, collection_version en pakketversies afgeleid uit het gekozen skills/catalog.json; broncommit en eventuele manifestselectie komen overeen |
| Gekozen methoden | Alle bestanden en metadata van iedere gekozen methode teruggelezen; aanroepbeleid komt overeen met allow_implicit_invocation en daadwerkelijke hostondersteuning |
| Eigen extra skills | Zelfstandige bestaande aanvullingen behouden; totale accountomvang hoeft niet gelijk te zijn aan catalogus- of selectieomvang |
| Externe methoden | Alleen eigen geverifieerde en gekozen uitbreidingen actief; een ontbrekende optionele uitbreiding blokkeert de algemene installatie niet |
| Conflicten | Lokale maatwerkverschillen zonder betrouwbare basis niet stilzwijgend overschreven |
| Privacy | Geen pagina-ID of persoonlijke bronlink van de maker in geïnstalleerde methoden, templates of router; bronvermelding blijft toegestaan |
| Schrijfproef | Eén neutrale proefregel in het eigen installatierapport opgeslagen en teruggelezen |
| Bestaand project | Eén bestaand project via eigen overzicht naar dezelfde taak-/besluitbron gevonden; inhoud niet gewijzigd |
| Eenvoudige vraag | Een korte algemene vraag eindigt direct, zonder nieuwe projectregistratie of verplichte grill-me |
| Routekeuze | Een verzoek om instructierouting te onderhouden laadt de bijbehorende geïnstalleerde hoofdmethode en passende naslag |
| Ontbrekende toegang | Alleen de afhankelijke stap wacht; onafhankelijke inrichting gaat aantoonbaar door |
| Onderbreking/herhalen | Onzekere create/import eerst teruggelezen; een tweede passage maakt geen dubbele Guide, rapport of skill |
| Versiebeleid | Gekozen broncommit, guidance-/collectie-/pakketversies en eventuele bundelidentiteit geregistreerd; geen bronredactie of stilzwijgende upgrade/downgrade van setup of consumerpin |
| Nieuwe sessie | Een echte verse context leest de eigen Guide en vindt de juiste bron; anders expliciet nog te doen |

## Concrete nieuwe-chatproef voor de ontvanger

Na het opslaan van de ingangsregel kan de ontvanger in een nieuwe chat vragen:

> Controleer mijn centrale werkwijze via mijn eigen Guide. Noem de gebruikte setupversie en vind mijn werkoverzicht en skillcatalogus. Wijzig niets.

Een vervolgproef kan één bestaand project bij naam aanwijzen en uitsluitend laten vinden waar taken en besluiten thuishoren. Dit bewijst de gevonden routes in die sessie, niet foutloos toekomstig gedrag of toegang tot ononderzochte pagina's.

## Herstel

Herstel alleen eigen installatieacties uit dit verslag, in omgekeerde afhankelijkheidsvolgorde. Lees elk doel eerst opnieuw. Bij latere gebruikerswijzigingen: geen oude kopie integraal terugzetten; verzoen het betrokken verschil. Reacties, historie en rechten blijven bij hun oorspronkelijke object. Stop afhankelijk herstel wanneer de exacte oude toestand niet beschikbaar is en geef de concrete resterende keuze.
