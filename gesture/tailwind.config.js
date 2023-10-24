/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js,jsx}", "./public/index.html"],
  theme: {
    extend: {
      fontFamily: {
        Pretendard: ["Pretendard-Regular"],
      },
      container: {
        center: true,
      },
    },
  },
  plugins: [],
};
