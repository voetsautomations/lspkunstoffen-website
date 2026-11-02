# LSP Kunststoffen – website

Compacte, snelle website gebouwd met [Astro](https://astro.build). Statische output, geen JavaScript nodig in de browser.

## Structuur

| Pagina | URL |
|---|---|
| Home | `/` |
| Diensten (overzicht) | `/diensten` |
| Dienst-detailpagina's | `/diensten/<slug>` (automatisch per dienst) |
| Galerij | `/galerij` |
| Over ons | `/over-ons` |
| Contact | `/contact` |

## Inhoud aanpassen

- **Bedrijfsgegevens, LinkedIn, diensten en USP's:** alles staat in `src/data/site.ts`. Zoek op `TODO` voor velden die nog ingevuld moeten worden.
- **Galerij-foto's:** zet jpg/png/webp-bestanden in `src/assets/galerij/`. Ze worden automatisch geoptimaliseerd (webp, responsive formaten, lazy loading). De bestandsnaam wordt de alt-tekst, dus gebruik beschrijvende namen (bv. `pe-plaat-gefreesd.jpg`).
- **Nieuwe dienst:** voeg een item toe aan `services` in `src/data/site.ts`. De detailpagina, het menu in de footer en alle interne links worden automatisch aangemaakt.

## SEO

- Unieke title en meta description per pagina, canonical-URL's en Open Graph-tags
- Gestructureerde data (JSON-LD): `LocalBusiness`, `Service` en `BreadcrumbList`
- `sitemap-index.xml` + `robots.txt`
- Interne links: Home ↔ diensten ↔ galerij ↔ contact, "andere diensten" op elke dienstpagina, en een footer met alle pagina's en diensten

## Commando's

```bash
npm install
npm run dev      # lokaal ontwikkelen op http://localhost:4321
npm run build    # productie-build naar dist/
npm run preview  # build lokaal bekijken
```
