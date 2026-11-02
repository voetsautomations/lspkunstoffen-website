// Alle bedrijfsgegevens en teksten staan centraal in dit bestand.
// Velden met "TODO" moeten nog worden gecontroleerd/ingevuld met de echte gegevens van LSP Kunststoffen.

export const site = {
  name: 'LSP Kunststoffen',
  url: 'https://lspkunststoffen.nl',
  tagline: 'Maatwerk in kunststof',
  description:
    'LSP Kunststoffen levert maatwerk in kunststof: van plaatmateriaal op maat tot complete werkstukken. Persoonlijk, vakkundig en snel geleverd.',
  // TODO: echte contactgegevens invullen
  contact: {
    phone: '+31 6 00000000',
    phoneDisplay: '06 - 00 00 00 00',
    email: 'info@lspkunststoffen.nl',
    street: 'Straatnaam 1',
    postalCode: '0000 AA',
    city: 'Plaats',
    country: 'NL',
    kvk: '00000000',
  },
  // TODO: echte LinkedIn-URL invullen
  social: {
    linkedin: 'https://www.linkedin.com/company/lsp-kunststoffen',
  },
};

export const nav = [
  { href: '/', label: 'Home' },
  { href: '/diensten', label: 'Diensten' },
  { href: '/galerij', label: 'Galerij' },
  { href: '/over-ons', label: 'Over ons' },
  { href: '/contact', label: 'Contact' },
];

export type Service = {
  slug: string;
  title: string;
  short: string;
  intro: string;
  points: string[];
};

// TODO: diensten afstemmen op het daadwerkelijke aanbod van LSP Kunststoffen
export const services: Service[] = [
  {
    slug: 'kunststof-op-maat',
    title: 'Kunststof op maat',
    short: 'Plaatmateriaal en profielen exact op maat gezaagd en gefreesd.',
    intro:
      'Heeft u kunststof nodig in een specifieke maat of vorm? Wij zagen, frezen en boren plaatmateriaal en profielen precies volgens uw tekening of opgave.',
    points: [
      'Zagen en frezen op maat',
      'Boren, tappen en afkanten',
      'Van enkel stuk tot kleine serie',
      'Advies over het juiste materiaal',
    ],
  },
  {
    slug: 'maatwerk-producten',
    title: 'Maatwerk producten',
    short: 'Complete werkstukken in kunststof, van ontwerp tot eindproduct.',
    intro:
      'Van beschermkap tot displaybak: wij maken complete kunststof producten op basis van uw idee, schets of technische tekening.',
    points: [
      'Meedenken over ontwerp en uitvoering',
      'Buigen, lijmen en lassen van kunststof',
      'Prototypes en kleine series',
      'Afgewerkt en klaar voor gebruik',
    ],
  },
  {
    slug: 'montage-en-reparatie',
    title: 'Montage & reparatie',
    short: 'Plaatsing, aanpassing en reparatie van kunststof onderdelen.',
    intro:
      'Wij monteren kunststof onderdelen op locatie en repareren of passen bestaande installaties en werkstukken aan.',
    points: [
      'Montage op locatie',
      'Reparatie van kunststof onderdelen',
      'Aanpassen van bestaande installaties',
      'Snel ter plaatse in de regio',
    ],
  },
];

export const usps = [
  { title: 'Echt maatwerk', text: 'Elk project wordt gemaakt volgens uw wensen en specificaties.' },
  { title: 'Persoonlijk contact', text: 'Korte lijnen: u spreekt direct met de vakman.' },
  { title: 'Snel geleverd', text: 'Heldere afspraken en een snelle doorlooptijd.' },
];
