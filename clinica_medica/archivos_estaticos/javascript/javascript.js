
const dropdownToggle = document.querySelector('#dropdown-toggle');
const dropdownMenu = document.querySelector('#dropdown-menu');

dropdownToggle.addEventListener('click', () => {
    dropdownMenu.classList.toggle('show-toggle');
});

const username = document.querySelector('.navbar__user-name');


document.addEventListener('click', function (event) {
    if (event.target !== dropdownMenu && !dropdownMenu.contains(event.target) &&
        event.target !== username && !username.contains(event.target)) {
        dropdownMenu.classList.remove('show-toggle');
    }
});