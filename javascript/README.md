# MayekMapping
Utility Functions for managing Meitei Mayek Characters and mapping to E-pao or Ratha Fonts.   

### Installation
`$ yarn add @meiteimayek/mapping`

`$ npm install @meiteimayek/mapping`

### Usage
```javascript
const mayek = require('@meiteimayek/mapping')('epao'); // 'ratha'

// This will print out all the Mapum Mayek
console.log(mayek.MAPUM)

// This will print out all the Lonsum Mayek
console.log(mayek.LONSUM)

// This will print out all the Cheitap Mayek
console.log(mayek.CHEITAP)

// This will print out all the Cheising Mayek
console.log(mayek.CHEISING)

// This will print out all the KHUDMA Mayek
console.log(mayek.KHUDAM)

// This will convert the character code of E-pao font to Unicode
console.log(mayek.toUnicode('mitE myeQ'))

// THis will convert from Unicode to E-pao font's character code
console.log(mayek.fromUnicode('ꯃꯤꯇꯩ ꯃꯌꯦꯛ'))
```
