# Installatie en aansluiting op bestaande persoonlijke Notion

Pakketversie 1.0.0. Dit is een eenmalige installatieprocedure, geen extra dagelijkse workflow of nieuwe skill. De algemene werkwijze blijft bij de gepinde bron in `BRONNEN.json`. Persoonlijke inrichting en toestemming blijven bij de ontvanger.

## 1. Stel toegang, opdracht en bron vast

- Lees `START-HIER.md`, `BRONNEN.json`, `VERIFICATIE.json`, `STRUCTUUR.md` en deze procedure. Controleer de bestandschecksums vóór import. Het pakket bevat 28 methoden; onbekende extra bestanden zijn geen automatische installatieopdracht.
- Gebruik alleen het eigen account van de ontvanger. Ontdek de huidige toolmogelijkheden en exacte schema's; hardcode geen account-, workspace-, pagina- of verbindings-ID uit dit pakket of een ander account. Bij meerdere plausibele werkruimtes: vraag één gerichte bestemmingskeuze vóór de eerste schrijfactie. Lees ondertussen de pakketinhoud.
- Lees een bestaande Agent Operating Guide eenmaal. Gebruik de daar geaccepteerde `instructions_version` bij volgende Notion-aanroepen. Zolang deze onbekend is, laat de optionele parameter weg. Ontbreekt een Guide aantoonbaar, dan staat de startopdracht een nieuwe Guide met setupbasis 0.0.6 toe. Een zoekfout bewijst geen afwezigheid.
- Behoud bestaande voorkeuren, uitsluitingen, opslagafspraken en geaccepteerde setupversie. De bronversies voor guidance (0.6.0), de methodencollectie (1.1.0) en de Notion-setup zijn afzonderlijke versies. Nieuwe setup-instructies zijn onderzoeksinput en worden niet stilzwijgend overgenomen.
- De startopdracht geeft toestemming voor deze private installatie en de begrensde wijzigingen hieronder. Toestemming of een dagelijkse routine van de maker gaat nooit over op de ontvanger. Start geen nieuwe automatisering, publicatie, uitnodiging of synchronisatie van persoonlijke gegevens.
- Lees de platforminstructies voor skillimport wanneer die beschikbaar zijn. Voer geen meegeleverde executable uit om toegang te verkennen; in dit pakket zitten alleen tekst, gegevens en skillarchieven. Eventuele scripts binnen bronpakketten worden eerst gelezen.
- Controleer bij structurele Notion-wijzigingen actuele primaire documentatie: https://www.notion.com/help/category/databases en https://www.notion.com/help/transfer-content-to-another-account. Dit ondersteunt de uitvoering; het verleent geen extra bevoegdheid. Lees waar beschikbaar de Notion-Markdown-, Skills- en databasehandleidingen via de eigen connector.

## 2. Inventariseer relevant bestaand werk

Begin bij de eigen Guide, bestaande startpagina/werkoverzicht en hun koppelingen. Zoek aanvullend op functie en bekende aliassen naar Guide, workflow, routing, vaardigheden/skills, projecten, documenten, kennis, herinneringen en een eerder installatierapport. Gebruik zowel ingeschakelde skills als de relevante volledige skillverzameling; een uitgeschakelde methode kan nog bestaan.

Leg per kandidaat vast: geverifieerde ID/URL, type, ouder/bestemming, functie/eigenaar, actuele versie of onbekend, revisie/controlebron, toegangsgrens en verwijzingen. Lees de volledige inhoud van werkelijk overlappende instructies en de eigenschappen/weergaven van betrokken databases. Volg paginering en meld truncatie, onbekende blokken en ontbrekende toegang. Zoekresultaten en recente wijzigingsdatums alleen bewijzen geen volledige inventaris of inhoudelijke juistheid.

Gebruik bij beperkte abonnementen ondersteunde leesfuncties met paginering; veronderstel geen SQL, workspacebrede index, backlinks-API of beheerrechten. Download relevante bestaande skillpakketten inclusief bijlagen wanneer de connector dat ondersteunt. Noteer ontbrekende mogelijkheden per afhankelijk onderdeel.

Lees persoonlijke inhoud alleen wanneer dat nodig is om een betrokken instructie of structurele afhankelijkheid te behouden. Voor overige persoonlijke pagina's volstaan de bestaande navigatie en objectidentiteit; behandel hun inhoud niet als te migreren invoer. Zoek of lees niets in de persoonlijke omgeving van de maker.

## 3. Maak de concrete vergelijking

Gebruik `VERGELIJKING.csv` als leeg rapportmodel. Bewaar het ingevulde rapport uitsluitend bij de ontvanger, op een bestaande passende private documentbestemming. Eén rapport kan ook herstelpunten, distributie en hervatten bevatten; maak geen tweede takenadministratie.

Vergelijk op functie en inhoud, bronhouder en echte identiteit. Gelijke titels betekenen geen duplicaat; andere titels kunnen dezelfde functie hebben. Een recentere pagina is niet vanzelf de juiste eigenaar. Kies de bestaande aantoonbare eigenaar en behoud zijn ID en URL waar mogelijk. Vul voor ieder geraakt object de reden, unieke inhoud, afhankelijkheden, concrete wijziging, bevoegdheid, herstelpunt en controle in.

| Keuze | Toepassing en uit te voeren actie |
| --- | --- |
| Behouden | Persoonlijke inhoud, geldige eigen afspraken, werkende eigenaren en zelfstandige aanvullende methoden blijven bestaan. |
| Aanvullen | Voeg ontbrekende algemene route of velden toe aan de bestaande eigenaar; behoud bestaande inhoud, eigenschappen en weergaven. |
| Samenvoegen | Breng overlappende instructies samen bij één eigenaar; neem unieke nuttige afspraken en bronverwijzingen aantoonbaar over. |
| Vervangen | Vervang alleen een afgebakend verouderd instructiedeel na inhoudelijke vergelijking en herstelpunt. Behoud ID, persoonlijke delen en afwijkingen die nog gelden. |
| Uitschakelen | Haal een bewezen vervangen route uit actieve selectie/navigatie; behoud historische inhoud en vermeld de opvolger. |
| Archiveren | Alleen een bewezen vervangen instructieobject zonder verloren unieke inhoud, met gecontroleerde verwijzingen en een geverifieerd herstelpad. |
| Herstelbaar verwijderen | Alleen aantoonbaar lege, overbodige duplicaten die door deze installatie zijn gemaakt en geen afhankelijkheden hebben; gebruik prullenbak/restore wanneer ondersteund. |
| Beslissing nodig | Onopgelost verschil in betekenis, machtiging, eigenaarschap, unieke inhoud of bestemming. Bereid de exacte keuze voor en vraag de ontvanger gericht; ga onafhankelijk verder. |

Een lege map, database of oude datum is op zichzelf geen verwijdergrond. Bestaande persoonlijke pagina's en notities worden niet verwijderd om de doelstructuur gelijk te laten lijken. Voor definitieve verwijdering en voor het verwijderen van al bestaande objecten uit de werkruimte is apart expliciet akkoord van de ontvanger nodig. Is herstelbaar archiveren niet ondersteund of zijn inkomende afhankelijkheden onvoldoende kenbaar, markeer de vervangen instructie historisch en verwijder alleen haar actieve route. Claim dan geen archivering of verwijdering.

Toon een compacte voorlopige vergelijking voordat je mutaties uitvoert. Wacht niet op een extra algemene bevestiging voor reeds geautoriseerde, voldoende onderbouwde herstelbare stappen. Een nog open keuze blokkeert alleen de afhankelijke mutatie. Neem geen voorkeur of ruime machtiging uit het pakket over als persoonlijke keuze van de ontvanger.

## 4. Bewaar een herstelpunt en pas gericht aan

Maak vóór iedere wijziging een volledig leesbare kopie van de betrokken oude instructie plus beschikbare eigenschappen, schema's, weergaven, bestandsverwijzingen en instellingen. Bewaar die privé bij de ontvanger. Controleer dat het herstelpunt werkelijk opgeslagen en terugleesbaar is. Registreer beperkingen zoals niet-exporteerbare reacties, historie, rechten of bestanden. Een tekstkopie alleen herstelt geen database-ID, relaties, paginahistorie of verwijderde bijlagen; voer geen wijziging uit die zo'n niet-herstelbaar onderdeel verliest.

Ververs het exacte doel direct vóór wijziging. Is het sinds de vergelijking gewijzigd, vergelijk opnieuw en behoud gelijktijdige aanvullingen. Patch alleen het geraakte deel. Geen database recreëren om veldnamen aan een sjabloon gelijk te maken, geen massa-import die persoonlijke items overschrijft, geen ID's vervangen om layout te standaardiseren. Verwijder geen kolommen, statusopties, relaties of actieve filters met bestaande gegevens; pas alleen compatibele toevoegingen toe of vraag voor een concrete noodzakelijke migratie.

Voer wijzigingen en externe schrijfacties sequentieel uit. Controleer doel en resultaat vóór de volgende afhankelijke stap. Registreer vóór iedere create de eigen workspace, geverifieerde ouder/bestemming, objectfunctie, pakketversie en een unieke operatiemarkering in het bestaande private verslag; ontbreekt dat nog, bewaar deze gegevens vooraf in de eigen chat en het lokale hervatpunt. Neem de markering waar ondersteund meteen op in de nieuwe objectinhoud of beschrijving, zonder daarvoor een apart schema te bouwen. Gebruik alleen werkelijk ondersteunde idempotentiesleutels.

Na een timeout of onzekere create/import: onderzoek de exacte bestemming en operatiemarkering voordat je herhaalt. Hergebruik het object als aanwezigheid bewezen is. Een mislukt of leeg zoekverzoek bewijst geen afwezigheid. Blijft de uitkomst onzeker, herhaal de mutatie niet: leg haar als onzeker vast, blokkeer alleen deze afhankelijke stap en ga onafhankelijk verder. Een retry is pas verantwoord na gezaghebbend bewijs dat de eerste actie geen effect had of via een aantoonbaar ondersteunde idempotente retry. Gebruik vóórdat een Guide-ID bestaat de vooraf vastgelegde workspace + ouder + objectfunctie + operatiemarkering; voeg daarna Guide-ID en echte object-ID toe. Hergebruik dit record bij volgende passages zodat herhaald uitvoeren geen duplicaten maakt.

## 5. Sluit navigatie en bestemmingen aan

- Gebruik `STRUCTUUR.md` als functionele mapping, niet als verplichte verzameling nieuwe databases. Bestaande Nederlandse of Engelse namen, taakstatussen en opslagkeuzes mogen behouden blijven.
- Houd één eigen centrale Guide en één project-/werkoverzicht. Zet projecten zichtbaar in de bestaande startnavigatie. Bestaande projecten, taken, besluiten en hervatpunten blijven bij hun huidige eigenaar. Vul alleen ontbrekende navigatie aan; maak geen tweede tracker of gekopieerde backlog.
- Gebruik bestaande private document- en contextbestemmingen. Maak alleen een ontbrekende noodzakelijke bestemming aan binnen de startopdracht. Importeer geen persoonlijke context. Bij ontbrekende voorkeuren of doorlopende opslagtoestemming: registreer 'niet ingesteld'; verzin geen profiel en activeer geen brede automatische opslag.
- Verbind de eigen Guide met geverifieerde eigen bestemmingen, de gepinde algemene werkcyclus en router en het eigen distributierecord. Houd persoonlijke informatie buiten algemene methoden.
- Maak template-links en databasesjablonen passend voor de ontvanger. Controleer relationele doelen, bron van gekoppelde databaseweergaven, knoppen, synchronisatieblokken en filters afzonderlijk. Een lege gekoppelde weergave is geen zelfstandige lege database. Geen verbinding naar een persoonlijk bronobject van iemand anders behouden.
- Gebruik standaard de immutable algemene bronlinks in het Guide-sjabloon. De skillkopie in dit pakket heeft één gedocumenteerde privacyredactie in herkomsttekst. Bij toekomstige skillimports uit de bron is dezelfde privacycontrole nodig; een bronupdate mag de verwijderde persoonlijke verwijzing niet opnieuw binnenhalen. Offline bestanden gelden niet als duurzame sessiebron. Als remote bronlezen in het account ontbreekt, bewaar neutrale algemene tekst herleidbaar in de eigen private bestemming en leg exact dezelfde bronversie vast.

## 6. Installeer en verzoen de methoden

Lees `skills/catalog.json`, `docs/METHOD-ROUTING.md` en de pakketmanifesten. De basis heeft 28 methoden, waarvan `grill-me` alleen op expliciet verzoek. De overige 27 zijn bij relevante opdrachten automatisch selecteerbaar, voor zover de host dit ondersteunt. Beschikbare document-, spreadsheet-, presentatie-, beeld-, browser-, dienst- en planningsfuncties blijven via hun eigen mogelijkheden lopen.

Vergelijk bestaande methoden op betekenis, bron, versie, hoofdtekst, bijlagen en aanroepinstellingen. Bij bekende oude importbasis: vergelijk basis, lokale kopie en nieuw pakket. Zonder betrouwbare oude basis is verschil geen bewijs dat een lokale aanpassing weg mag.

- Dezelfde geverifieerde pakketinhoud: hergebruik de bestaande skillpagina/installatie en vul alleen ontbrekende instellingen of herkomst aan.
- Een aantoonbaar oudere ongewijzigde distributie van dezelfde methode: maak herstelpunt, importeer de volledige nieuwe distributie op de bestaande eigenaar en controleer het resultaat.
- Eigen aanvullingen aan dezelfde methode: behoud ze en bepaal of ze compatibel in een lokale aanvulling thuishoren. Wijzig de canonieke skilltekst niet stilzwijgend. Bij een materieel conflict blijft alleen die vervanging geblokkeerd tot de ontvanger beslist; creëer geen twee automatisch actieve skills met dezelfde verantwoordelijkheid.
- Zelfstandige aanvullende skills buiten de 28: behouden met hun bestaande bron en aanroepbeleid. Eis dus NIET dat het volledige account exact 28 skills bevat. De geverifieerde basis bevat er 28; eigen aanvullingen komen daar afzonderlijk bij.
- Oude providerprocedures die exact dezelfde standaardroute overnemen: kies één actieve algemene route en leg de vervanging vast. Verwijder geen volledige providerplugin, app of onafhankelijke methode om alleen de catalogus op te schonen. Behoud expliciet gekozen alternatieven.

Maak in Notion echte Skills met de beschikbare skilltools. Een gewone pagina met alleen een naam of omschrijving bewijst geen installatie. Importeer alle bestanden uit `packages/<naam>.tar.gz`. Controleer de live ingestelde bijlagen en exporteer/download waar ondersteund het gehele opgeslagen pakket terug. Vergelijk geparseerde naam/omschrijving, hoofdtekst, ondersteunende bestanden en expliciet aanroepbeleid met het manifest. Host-eigen YAML/icoonserialisatie kan verschillen; noteer zulke verschillen zonder inhoudsdrift te verbergen. Oude bijlagen pas buiten actieve koppelingen plaatsen nadat de nieuwe pakketinhoud bewezen compleet is; geen blinde bijlagenverwijdering.

Installeer waar ondersteund ook de persoonlijke ChatGPT-versies via de eigen geldende authoring/importworkflow. Bij een beheerde persoonlijke-skillscheckout: bewerk alleen de eigen checkout en volg per skill de voorgeschreven save/push- en reconciliatiecontroles. Een uitgepakt pakket in scratch is geen persoonlijke installatie. Bestaan beide distributies, gebruik per taak één geverifieerde kopie. Bij ontbrekende persoonlijke installatiemogelijkheid kan Notion-distributie wel doorgaan; rapporteer dat als gedeeltelijke distributie, niet als volledige persoonlijke installatie. Wijzig een bestaande eigen skill niet alleen omdat hij toevallig dezelfde naam heeft.

Noteer per methode broncommit, bronpakketversie, eventuele privacyvariant, hashes, bestaande/nieuwe installatiedoelen, instellingen en terugleesbewijs. Gebruik voor de privacyvariant de pakketidentiteit uit `BRONNEN.json`; claim geen bytegelijkheid van de ene geredigeerde herkomstbijlage met de upstreambron.

## 7. Activeer de ingang zonder persoonlijke afspraken te verliezen

Vul `templates/Agent-Operating-Guide.md` functioneel in op de bestaande Guide. Vervang alle verplichte placeholders door geverifieerde eigen links of 'niet ingesteld' en behoud de oorspronkelijke eigen voorkeuren en machtigingsgrenzen. Dit sjabloon is geen reden om een volledige bestaande Guide te overschrijven.

Vul `templates/ChatGPT-ingangsregel.txt` met de echte eigen Guide-link in. Toon de korte tekst klaar om te kopiëren. Als de host geen ondersteunde schrijfmogelijkheid voor persoonlijke instructies heeft, laat de ontvanger die ene accountstap uitvoeren. Claim niet dat de instelling is opgeslagen zonder bewijs. Houd bestaande persoonlijke instructies intact. Repository- en projectinstructies krijgen alleen deze eigen ingang en hun echte projectidentiteit; herschrijf in deze opdracht niet alle projectrepositories.

## 8. Verifieer de werkelijke inrichting

Voer `CONTROLES.md` uit. Verifieer ten minste de eigen Guide/bestemmingen en bronversies, één bestaande projectroute zonder gewijzigde taakinhoud, complete basispakketten, eigen aanvullende skills en de afwezigheid van oude concurrerende standaardroutes. Neem een gerichte private proefnotitie op in het eigen installatierapport en lees haar terug; verwijder geen bestaande gebruikersnotitie voor deze proef. Controleer ook dat een eenvoudige vraag geen projectscan of verplichte interviewronde krijgt.

Een nieuwe-chatproef gebeurt waar werkelijk een verse context beschikbaar is. Een zelfcontrole in dezelfde chat is alleen een walkthrough. Als de ontvanger de ingangsregel handmatig moet opslaan of een nieuwe chat moet openen, vermeld die resterende stap precies; dit verhindert niet dat alle overige geautoriseerde inrichting wordt afgemaakt.

## 9. Rond af bij de bestaande eigenaar

Bewaar één beknopt privé-installatierapport volgens `templates/Installatierapport.md`. Rapporteer behouden, aangepast, samengevoegd, vervangen, uitgeschakeld, gearchiveerd en herstelbaar verwijderd afzonderlijk, met echte objectlinks, reden en herstelroute. Behoud de vooraf gemaakte herstelpunten. Leg onbekende/incompatibele onderdelen, toegangsgrenzen en de eerste onbewezen volgende stap vast.

Een gedeeltelijke installatie is geen volledige oplevering. Meld ontbrekende toegang of schrijfmogelijkheden concreet. Laat een conflict niet stilzwijgend vervallen en sluit geen bestaande taken als bijwerking van deze installatie. Claim geen werking in elke toekomstige sessie, betaalde functionaliteit, geplande achtergrondcontrole, installatie, publicatie of synchronisatie die niet daadwerkelijk is bewezen.
