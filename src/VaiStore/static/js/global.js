window.onload = function () {
    document.body.classList.add('loaded_hiding');
    
    // Remove hello popup
    if (localStorage.getItem('hello') == 'done' && location.pathname === '/') {
        document.getElementById('hi').classList.add('hide')
    }

    // Toggle admin button
    if (localStorage.getItem('admin') == 'true' && location.pathname === '/') {
        if ($('.mobile-nav').css('display') == 'none') {
            $('#nav-admin').toggleClass('hide');
        }

        else {
            $('#mnav-admin').toggleClass('hide');
        }
    }

    // Remove preloader
    window.setTimeout(function () {
        document.body.classList.add('loaded');
        document.body.classList.remove('loaded_hiding');
    }, 300);
}

function hello() {
    $('.hp_1').toggleClass('hide');
    $('.hp_2').toggleClass('show_element');
}

function removeHello() {
    $('body').css('overflow','scroll');
    $('.privetik').toggleClass('hide');
    localStorage.setItem('hello', 'done');
}

function activateAdmin() {
    localStorage.setItem('admin', 'true');
}

function deactivateAdmin() {
    localStorage.setItem('admin', 'false');
}