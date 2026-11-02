import type { ImageMetadata } from 'astro';

// Alle foto's uit src/assets/galerij/. De bestandsnaam (zonder extensie) is de sleutel én de basis voor de alt-tekst.
// Nette onderschriften/alt-teksten per bestandsnaam. Staat een foto hier niet in, dan wordt de bestandsnaam gebruikt.
const captions: Record<string, string> = {
  'cnc-freesbank-werkplaats': 'CNC-freesbank in onze werkplaats',
  'petg-plaat-gezet-transparant': 'Transparante PETG-plaat, op maat gezet',
  'pp-trechter-met-onderstel-gelast': 'PP-trechter met onderstel, gelast',
  'transparante-houder-gefreesd': 'Transparante houder, gefreesd',
  'zwarte-frees-onderdelen-op-maat': 'Gefreesde onderdelen op maat',
  'zwarte-tandwielen-en-bussen': 'Tandwielen en bussen, gedraaid en gefreesd',
};

const files = import.meta.glob<{ default: ImageMetadata }>('../assets/galerij/*.{jpg,jpeg,png,webp}', { eager: true });

export const galleryImages = Object.entries(files)
  .sort(([a], [b]) => a.localeCompare(b))
  .map(([path, mod]) => {
    const name = path.split('/').pop()!.replace(/\.[^.]+$/, '');
    const fallback = name.replace(/[-_]+/g, ' ');
    const alt = captions[name] ?? fallback.charAt(0).toUpperCase() + fallback.slice(1);
    return { name, src: mod.default, alt };
  });

export const getImage = (name: string) => galleryImages.find((img) => img.name === name);

// Responsive breedtes zonder op te schalen boven het origineel.
export const widthsFor = (img: ImageMetadata, wanted = [480, 800, 1200]) => {
  const w = wanted.filter((x) => x < img.width);
  return [...w, img.width];
};
