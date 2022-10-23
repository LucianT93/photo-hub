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

// let loadFile = function (event) {
//     let image = document.querySelector('#output');
//     image.src = URL.createObjectURL(event.target.files[0]);
// };


$(document).ready(() => {
    $('#formFile').change(function () {
        const file = this.files[0];
        if (file) {
            let reader = new FileReader();
            reader.onload = function (event) {
                $('#output').attr('src', event.target.result);
            }
            reader.readAsDataURL(file);
        }
    });
    $('#profile_image').change(function () {
        const file = this.files[0];
        if (file) {
            let reader = new FileReader();
            reader.onload = function (event) {
                $('#profile-img').attr('src', event.target.result);
            }
            reader.readAsDataURL(file);
        }
    });
});
// TODO: make a function that calls the forms to eliminate redundancy
$(document).on('submit', '#form_like', function (e) {
    e.preventDefault()

    $.ajax({
        type: 'POST',
        url: "like_dislike/",
        data: {
            like: $('#like').val(),
            photo_id: $('#photo_id').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function () {
            let like = $('#no_likes')
            like.text(parseInt(like.text()) + 1)
            $("#likeBtn").prop("disabled", true)
        }
    })
})

$(document).on('submit', '#form_dislike', function (e) {
    e.preventDefault()

    $.ajax({
        type: 'POST',
        url: "like_dislike/",
        data: {
            dislike: $('#dislike').val(),
            photo_id: $('#photo_id').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function () {
            let dislike = $('#no_dislikes')
            dislike.text(parseInt(dislike.text()) + 1)
            $("#dislikeBtn").prop("disabled", true)
        }
    })
})

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
