declare module '@meiteimayek/mapping' {
  interface Mayek {
    mapping: Record<string, string>;
    mappingRev: Record<string, string>;
    MAPUM: string[];
    LONSUM: string[];
    CHEITAP: string[];
    CHEISING: string[];
    KHUDAM: string[];
    toUnicode: (text: string) => string;
    fromUnicode: (text: string) => string;
  }

  export default function mayek(type: 'epao' | 'ratha'): Mayek;
}
