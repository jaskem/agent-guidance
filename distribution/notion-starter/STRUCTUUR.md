# Functionele doelstructuur

Deze tabel vult de [algemene installatie](../../INSTALL.md) aan voor een door de ontvanger gekozen Notion-bestemming. Zij beschrijft verantwoordelijkheden. Hergebruik bestaande namen, locaties en databases zodra ze dezelfde functie goed vervullen. Er is geen verplicht aantal databases en geen verhuizing van persoonlijke pagina's nodig. Niet-gekozen optionele functies blijven niet ingesteld.

| Functie | Inhoud die mag worden ingericht | Bestaand werk behouden |
| --- | --- | --- |
| Centrale Guide | Eigen bestemmingen, versie, algemene route en persoonlijke grenzen | Bestaande Guide-ID, voorkeuren en eigen machtigingen |
| Werkoverzicht | Zichtbare toegang tot projecten, methoden en hervatten | Bestaande projectregistraties en pagina's |
| Projectregistratie | Identiteit, aliassen, bronnen en eigenaren, huidig hervatpunt | Bestaande taak-, besluit- en producteigenaren |
| Documenten | Private algemene instructies en installatierapport | Alle eigen documenten en bestaande indeling |
| Persoonlijke context | Alleen een eigen bestemming en reeds geldende opslagafspraken | Eigen herinneringen; geen contextimport uit het pakket |
| Skills | Volledige gekozen pakketten uit het geselecteerde skills/catalog.json, met versie en aanroepbeleid uit die bron | Nuttige eigen skills en aangepaste inhoud; catalogusomvang is geen vereist totaal voor het account |
| Distributierecord | Versies, bronhashes, installatiedoelen, instellingen en bewijsgrenzen | Bestaande installatieregistratie hergebruiken |
| Werkcyclus en router | Gepinde algemene bron, geen extra concurrerende standaardprocedure | Projectspecificaties en lokale consumerpins |

## Bestaande databases aansluiten

De minimale betekenis is leidend, niet de veldnaam. Maak een mapping naar aanwezige velden; voeg alleen echt ontbrekende noodzakelijke velden toe.

| Record | Gewenste betekenis | Voorbeelden van namen |
| --- | --- | --- |
| Project | Stabiele identiteit, titel en aliassen | Project-ID; Naam; Aliassen |
| Project | Eigenaar van code/inhoud, eisen, taken en besluiten | Bronnen; Taakbron; Besluitbron |
| Project | Huidig bewezen resultaat en volgende stap | Hervatpunt; Controle; Bewijsgrens |
| Document | Titel en context/bestemming | Naam of Title; projectrelatie indien bestaand |
| Skill | Echte native skillstatus, naam en omschrijving | Gebruik de schema's van de actuele skilltools |
| Distributie | Exacte broncommit, catalogusselectie, eventuele bundelidentiteit en gecontroleerde installatie | Bron; Versie; Selectie; Hashes; Doel; Gecontroleerd |

Houd het werkoverzicht compact: projecten zichtbaar, de algemene werkwijze en catalogus rechtstreeks bereikbaar, persoonlijke informatie op haar bestaande plek. Verbeter bruikbaarheid waar dit nodig is; verander kleuren, iconen en layout niet alleen om een ander account na te bootsen. Lege herbruikbare project-/documenttemplates mogen worden toegevoegd als ze nog ontbreken, zonder bestaande templates te verwijderen.
