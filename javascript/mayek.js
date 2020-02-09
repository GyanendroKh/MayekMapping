const fs = require('fs');
const path = require('path');

const json = fs.readFileSync(path.join(__dirname, 'mayek.json'));
const data = JSON.parse(json);

const mapping = data
  .map(item => {
    return item['mayek'];
  })
  .reduce((acc, item) => {
    item.forEach(i => (acc[i['code']] = i['char']));
    return acc;
  }, {});

const mappingRev = data
  .map(item => {
    return item['mayek'];
  })
  .reduce((acc, item) => {
    item.forEach(i => (acc[i['char']] = i['code']));
    return acc;
  }, {});

const Mayek = {
  mapping,
  mappingRev,
  MAPUM: data[0]['mayek'].map(i => i['char']),
  LONSUM: data[1]['mayek'].map(i => i['char']),
  CHEITAP: data[2]['mayek'].map(i => i['char']),
  CHEISING: data[3]['mayek'].map(i => i['char']),
  KHUDAM: data[4]['mayek'].map(i => i['char']),
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
