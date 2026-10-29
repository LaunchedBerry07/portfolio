/** Tailwind source configuration for rebuilding the committed static utility sheet. */
module.exports = {
  content: ['./**/*.html', './assets/js/**/*.js'],
  theme: { extend: {
    colors: { darkpink:'#D14D72', navy:'#13293D', bluegreen:'#087E8B', turquoise:'#149E92', seafoam:'#83E0D0', mist:'#EAF4F8', sky:'#5B96BD', ultramarine:'#304FFE' },
    fontFamily: { sans:['Inter','sans-serif'], serif:['Playfair Display','serif'], hand:['Caveat','cursive'] },
    boxShadow: { handdrawn:'4px 4px 0px 0px rgba(19,41,61,1)', 'handdrawn-pink':'4px 4px 0px 0px rgba(209,77,114,1)', 'handdrawn-seafoam':'4px 4px 0px 0px rgba(131,224,208,1)' }
  } }
};
