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

// $(document).ready(() => {
//     $('')
//     $.ajax({
//         type: 'POST',
//         url: "like_dislike/",
//         data: {
//             like: $(`#like_${id}`).val(),
//             photo_id: $(`#photo_id_${id}`).val(),
//             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//         },
//         success: function () {
//             let like = $(`#no_likes_${id}`)
//             like.text(parseInt(like.text()) + 1)
//         }
//     })
// })

// $(document).on('submit', '#form_dislike', function (e) {
//     e.preventDefault()
//
//     $.ajax({
//         type: 'POST',
//         url: "like_dislike/",
//         data: {
//             dislike: $('#dislike').val(),
//             photo_id: $('#photo_id').val(),
//             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//         },
//         success: function () {
//             let dislike = $('#no_dislikes')
//             dislike.text(parseInt(dislike.text()) + 1)
//         }
//     })
// })

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

// function toggle_like(id) {
//     $.ajax({
//         method: 'GET',
//         url: 'like_owners/' + id,
//         dataType: 'json',
//         success: function (data) {
//             if (data['message'] === 'already liked') {
//
//             }
//         }
//     })
// }

function show_edit() {
    $("#edit_profile_button").toggle()
    $("#edit_camera_button").toggle()
    $("#edit_lens_button").toggle()
}