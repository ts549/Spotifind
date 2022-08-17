/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        Lato: ['Lato']
      },
      colors: {
        'light_red': '#EE484D',
        'salmon': '#FF7F7F',
        'mulberry': '#601A3E',
        'plum': '#4C0212',
        'black': '#000000',
        'light_purple': '#EBE8FC',
        'white': '#FFFFFF'
      },
      padding: {
        '1/2': '50%',
        full: '100%',
      }
    }

  },
  plugins: [],
}
