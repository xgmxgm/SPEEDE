let btn__start = document.querySelector('.button__start');

btn__start.addEventListener('click', () => {
    btn__start.classList.toggle('button__loader')
    btn__start.innerHTML = "<h2> LOADING... </h2>"
})