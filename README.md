# Slim-Mobiel website

Nieuwe homepage voor Slim-Mobiel B.V., importeur van Bellier brommobielen en Ellectra voor Nederland en België.
Statische HTML/CSS/JS: geen build-stap, geen framework, geen tracking. Laadt snel en is eenvoudig te hosten.

## Deployen op Vercel

1. Zet deze map in een (nieuwe) GitHub-repository.
2. Ga in Vercel naar **Add New → Project** en importeer die repository.
3. Framework preset: **Other**. Build command en output directory leeg laten.
4. Deploy. Koppel daarna het domein `slimmobiel.nl` onder **Settings → Domains**.

`vercel.json` regelt nette URL's (`/privacy` in plaats van `/privacy.html`), security-headers, caching
en 301-redirects van de oude WordPress-adressen (`/site/...`) naar de nieuwe pagina. Zo blijft de
opgebouwde vindbaarheid in Google behouden.

Lokaal bekijken: `python3 -m http.server 8080` en open http://localhost:8080.

## Voordat de site live gaat

- **Foto's vervangen.** In `images/` staan plaatshouders. Overschrijf ze met echte foto's, met dezelfde
  bestandsnaam en verhouding 3:2 (minimaal 1200 x 800 px, JPG, liefst onder 250 kB):
  - `hero-bellier-b8.jpg`: grote foto bovenaan
  - `bellier-b8.jpg`, `bellier-docker.jpg`, `ellectra-kimsi.jpg`
  - `og-image.jpg` (1200 x 630): de afbeelding die verschijnt als de link gedeeld wordt
- **Logo.** `images/logo-slim-mobiel.svg` is een nieuw getekend woordmerk in de huisstijl (geel #ffdd00 + grafiet).
  Wil je het originele logo houden? Zet het bestand in `images/` en pas het pad aan in de `<header>` en `<footer>`.
- `scripts/download-originals.sh` haalt de afbeeldingen van de oude site op naar `images/original/`.
- **Folders (pdf).** De links wijzen nog naar `www.slimmobiel.nl/pdf/...`. Zet de pdf's bij voorkeur in een map
  `pdf/` in deze repository en pas de links aan, anders werken ze niet meer na de verhuizing.
- **Gegevens controleren.** Adres, telefoon, modellen en het privacybeleid door de eigenaar laten nakijken.
- **Formulier.** Het proefritformulier opent nu een ingevulde e-mail (werkt zonder server). Voor een echt
  formulier: zet de `action` op een dienst zoals Formspree, of voeg een Vercel-functie toe.

## SEO

- Eén duidelijke H1, logische koppenstructuur, title en meta description per pagina.
- Schema.org JSON-LD: Organization/AutomotiveBusiness met adres en contact, WebSite, WebPage en de modellen als Product.
- Open Graph- en Twitter-tags, canonical URL, `robots.txt`, `sitemap.xml` en `llms.txt` voor AI-zoekmachines.
- Lettertypes (Barlow, SIL Open Font License) worden lokaal gehost: sneller en zonder datadeling met Google.
- Afbeeldingen hebben vaste afmetingen (geen layout-verspringing) en laden lazy buiten beeld.

Na livegang: domein toevoegen in Google Search Console en de sitemap indienen.

## Bestanden

```
index.html            homepage
privacy.html          privacybeleid
404.html              foutpagina
assets/css/styles.css alle stijlen (inclusief lettertypes)
assets/js/main.js     mobiel menu en proefritformulier
assets/fonts/         Barlow en Barlow Condensed (woff2)
images/               logo's, iconen en (plaatshouder)foto's
scripts/              hulpscripts voor afbeeldingen
```
