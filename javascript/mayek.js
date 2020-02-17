const fs = require('fs');
const path = require('path');

const json = fs.readFileSync(path.join(__dirname, 'mayek.json'));
const data = JSON.parse(json);

const mapping = data
  .map(item => {
    return item['mayek'];
  })
  .reduce((acc, item) => {
    item.forEach(i => (acc[i['code'].trim()] = i['char'].trim()));
    return acc;
  }, {});

const mappingRev = data
  .map(item => {
    return item['mayek'];
  })
  .reduce((acc, item) => {
    item.forEach(i => (acc[i['char'].trim()] = i['code'].trim()));
    return acc;
  }, {});

const Mayek = {
  mapping,
  mappingRev,
  MAPUM: data[0]['mayek'].map(i => i['char'].trim()),
  LONSUM: data[1]['mayek'].map(i => i['char'].trim()),
  CHEITAP: data[2]['mayek'].map(i => i['char'].trim()),
  CHEISING: data[3]['mayek'].map(i => i['char'].trim()),
  KHUDAM: data[4]['mayek'].map(i => i['char'].trim()),
  toUnicode: string => {
    return string
      .split('')
      .map(c => {
        if (mapping[c] !== undefined) {
          return mapping[c];
        } else {
          return c;
        }
      })
      .join('');
  },
  fromUnicode: string => {
    return string
      .split('')
      .map(c => {
        if (mappingRev[c] !== undefined) {
          return mappingRev[c];
        } else {
          return c;
        }
      })
      .join('');
  }
};

module.exports = Mayek;
