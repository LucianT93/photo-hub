function disableBtn(upBtn, upCount) {
    upBtn.classList.add('disabled')
    upCount.innerText = parseInt(upCount.innerText) + 1
}

const shownBtn = document.querySelectorAll('.read-more')
const hideBtn = document.querySelectorAll('.hide-desc-btn')
const readMore = document.querySelectorAll('.read-more')
const hiddenContent = document.querySelectorAll('.hidden-desc')

for (let i = 0; i < shownBtn.length; i++) {
    shownBtn[i].addEventListener('click', () => {
        hiddenContent[i].classList.add('shown')
        readMore[i].classList.add('hidden')
    })
    hideBtn[i].addEventListener('click', () => {
        hiddenContent[i].classList.remove('shown')
        readMore[i].classList.remove('hidden')
    })
}

let loadFile = function (event) {
    let image = document.querySelector('#output');
    image.src = URL.createObjectURL(event.target.files[0]);
};

$(document).on('submit', '#form_login', function (e) {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: "login/",
        data: {
            username: $('#username_login').val(),
            password: $('#password_login').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (data) {
            if (data['message'] === 'success') {
                location.reload()
            } else {
                $('#liveToast').toast('show')
            }
        }
    })
})

$(document).on('submit', '#form_register', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: 'register/',
        data: {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            username: $('#username_register').val(),
            email: $('#email_register').val(),
            password1: $('#pass1_register').val(),
            password2: $('#pass2_register').val(),
        },
        success: function (data) {
            if (data['message'] === 'success') {
                location.reload()
            } else {
                $('#liveToastRegister').toast('show')
            }
        }
    })
})

