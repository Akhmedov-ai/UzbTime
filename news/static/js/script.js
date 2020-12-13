document.querySelector('.navbar-burger').addEventListener('click', function (event) {
    document.querySelector('.navbar-menu').classList.toggle('is-active');
    event.target.classList.toggle('is-active');
});

document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(link.getAttribute('href'))
            .scrollIntoView({ behavior: 'smooth', block: 'start'});
    });
});
