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
        'purpledge': '#6462c6',
      },
    }
  },
  plugins: [],
}
