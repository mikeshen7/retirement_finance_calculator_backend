/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/*.html',
    './node_modules/flowbite/*.js',
  ],
  theme: {
    extend: {},
    screens: {
      xs: '300px',
      sm: '640px',
      md: '768px',
      lg: '1024px',
      xl: '1280px',
      '2xl': '1536px',
    },
  },
  plugins: [],
}

