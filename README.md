# LSP Kunststoffen – website

Compacte, snelle website voor LSP Kunststoffen (Schijndel), gebouwd met [Astro](https://astro.build).
Statische output, geen JavaScript in de browser. Huisstijl afgeleid van het logo en de bedrijfsbus: zwart/antraciet met brons-goud.

## Structuur

| Pagina | URL |
|---|---|
| Home | `/` |
| Diensten (overzicht) | `/diensten` |
| CNC-frezen | `/diensten/cnc-frezen` |
| Draaien & frezen | `/diensten/draaien-en-frezen` |
| Kunststof lassen | `/diensten/kunststof-lassen` |
| Maatwerk | `/diensten/maatwerk` |
| Galerij | `/galerij` |
| Over ons | `/over-ons` |
| Contact | `/contact` |

## Inhoud aanpassen

- **Bedrijfsgegevens, social links, diensten, machinepark en USP's:** `src/data/site.ts`.
  Controleer de LinkedIn- en Facebook-URL (gemarkeerd met `TODO`).
- **Galerij-foto's:** zet jpg/png/webp-bestanden in `src/assets/galerij/`. Ze verschijnen automatisch en worden
  geoptimaliseerd (webp, responsive formaten, lazy loading). De bestandsnaam wordt het onderschrift en de alt-tekst,
  dus gebruik beschrijvende namen (bv. `pp-bak-gelast.jpg`).
- **Foto bij een dienst:** het veld `image` in `services` verwijst naar een bestandsnaam (zonder extensie) uit de galerij.
- **Nieuwe dienst:** voeg een item toe aan `services`. De detailpagina, footer-links en interne links komen er vanzelf bij.
- **Logo en bedrijfsbus:** `src/assets/foto/`.

## SEO

- Unieke title en meta description per pagina (met "Schijndel" voor lokale vindbaarheid), canonical-URL's en Open Graph-tags
- Gestructureerde data (JSON-LD): `LocalBusiness` (met adres, KvK/BTW, eigenaar), `Service` en `BreadcrumbList`
- `sitemap-index.xml` + `robots.txt`
- Interne links: home ↔ diensten ↔ galerij ↔ contact, "andere diensten" op elke dienstpagina, kruimelpaden en een footer met alle pagina's en diensten

## Commando's

```bash
npm install
npm run dev      # lokaal ontwikkelen op http://localhost:4321
npm run build    # productie-build naar dist/
npm run preview  # build lokaal bekijken
```
