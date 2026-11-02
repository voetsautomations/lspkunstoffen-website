// Alle bedrijfsgegevens en teksten staan centraal in dit bestand.

export const site = {
  name: 'LSP Kunststoffen',
  url: 'https://lspkunststoffen.nl',
  tagline: 'Van ontwerp tot realisatie',
  slogan: 'Uw partner in machinaal bewerkte kunststof producten',
  description:
    'LSP Kunststoffen in Schijndel: CNC-frezen, draaien en lassen van kunststof. Kunststof producten op maat, van ontwerp tot realisatie.',
  owner: 'Leon Sprokholt',
  contact: {
    phone: '+31651562980',
    phoneDisplay: '06 51 56 29 80',
    email: 'lspkunststoffen@gmail.com',
    street: 'Van Leeuwenhoekweg 27',
    postalCode: '5482 TK',
    city: 'Schijndel',
    country: 'NL',
    kvk: '61786349',
    btw: 'NL001693485B27',
    maps: 'https://www.google.com/maps/search/?api=1&query=Van+Leeuwenhoekweg+27+5482+TK+Schijndel',
  },
  // TODO: controleer of dit de juiste profielen zijn
  social: {
    linkedin: 'https://www.linkedin.com/company/lsp-kunststoffen',
    facebook: 'https://www.facebook.com/lspkunststoffen',
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
  image: string; // bestandsnaam (zonder extensie) in src/assets/galerij/
};

export const services: Service[] = [
  {
    slug: 'cnc-frezen',
    title: 'CNC-frezen',
    short: 'Nauwkeurig gefreesde kunststof onderdelen op onze 3-assige CNC-freesbank.',
    intro:
      'Op onze 3-assige CNC-freesbank frezen we kunststof onderdelen en plaatwerk exact volgens tekening. Van één prototype tot een serie: iedere keer dezelfde maatvoering.',
    points: [
      '3-assige CNC-freesbank',
      'Contouren, uitsparingen, gaten en verzinkingen',
      'Enkelstuks, prototypes en series',
      'Werken vanuit uw tekening of schets',
    ],
    image: 'cnc-freesbank-werkplaats',
  },
  {
    slug: 'draaien-en-frezen',
    title: 'Draaien & frezen',
    short: 'Bussen, ringen, tandwielen en ander draai- en freeswerk in kunststof.',
    intro:
      'Met onze conventionele draaibank en freesbank maken we ronde en maatvaste onderdelen zoals bussen, ringen, rollen en tandwielen. Ideaal voor vervangingsonderdelen en reparaties.',
    points: [
      'Conventionele draaibank',
      'Conventionele freesbank',
      'Bussen, rollen, ringen en tandwielen',
      'Vervangingsonderdelen nagemaakt op maat',
    ],
    image: 'zwarte-tandwielen-en-bussen',
  },
  {
    slug: 'kunststof-lassen',
    title: 'Kunststof lassen',
    short: 'Handlassen, stuiklassen en spiegellassen (stomp en mof).',
    intro:
      'Wij lassen kunststof platen, buizen en constructies tot sterke, dichte verbindingen. Daarvoor beschikken we over apparatuur voor handlassen, stuiklassen en spiegellassen, zowel stomp als mof.',
    points: [
      'Handlassen',
      'Stuiklassen',
      'Spiegellassen, stomp en mof',
      'Bakken, trechters, kanalen en constructies',
    ],
    image: 'pp-trechter-met-onderstel-gelast',
  },
  {
    slug: 'maatwerk',
    title: 'Maatwerk van ontwerp tot realisatie',
    short: 'Complete kunststof producten: wij denken mee, maken en leveren af.',
    intro:
      'Heeft u een idee of probleem waar een kunststof oplossing voor nodig is? We denken mee over ontwerp en materiaal, zagen het plaatmateriaal op onze wand- en tafelzagen en werken het product volledig af.',
    points: [
      'Meedenken over ontwerp en materiaalkeuze',
      'Zagen op wand- en tafelzaag',
      'Afwerken met diverse handbediende machines',
      'Eén aanspreekpunt van idee tot eindproduct',
    ],
    image: 'petg-plaat-gezet-transparant',
  },
];

export const machines = [
  '3-assige CNC-freesbank',
  'Conventionele draaibank',
  'Conventionele freesbank',
  'Wandzagen en tafelzagen',
  'Diverse handbediende bewerkingsmachines voor kunststof',
  'Lasapparatuur voor handlassen, stuiklassen en spiegellassen (stomp en mof)',
];

export const usps = [
  { title: 'Van ontwerp tot realisatie', text: 'Wij denken mee vanaf het eerste idee en leveren een afgewerkt product.' },
  { title: 'Eigen machinepark', text: 'CNC-frezen, draaien, zagen en lassen: alles onder één dak in Schijndel.' },
  { title: 'Direct contact', text: 'U spreekt rechtstreeks met Leon, de vakman die uw product maakt.' },
];
