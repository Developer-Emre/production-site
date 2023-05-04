

const nav = document.querySelector('nav');
const navOffsetTop = nav.offsetTop;

window.addEventListener('scroll', () => {
    if (window.scrollY > navOffsetTop) {
        document.body.style.paddingTop = nav.offsetHeight + 'px';
        nav.classList.add('fixed-nav');
    } else {
        document.body.style.paddingTop = 0;
        nav.classList.remove('fixed-nav');
    }
});






