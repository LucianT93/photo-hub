

function disableBtn(upBtn, upCount){
  upBtn.classList.add('disabled')
  upCount.innerText = parseInt(upCount.innerText) + 1
}

const shownBtn = document.querySelectorAll('.read-more')
const hideBtn = document.querySelectorAll('.hide-desc-btn')
const readMore = document.querySelectorAll('.read-more')
const hiddenContent = document.querySelectorAll('.hidden-desc')

for(let i=0;i<shownBtn.length;i++){
    shownBtn[i].addEventListener('click',()=>{
        hiddenContent[i].classList.add('shown')
        readMore[i].classList.add('hidden')
    })
    hideBtn[i].addEventListener('click',()=>{
        hiddenContent[i].classList.remove('shown')
        readMore[i].classList.remove('hidden')
    })
}

let loadFile = function(event) {
	let image = document.querySelector('#output');
	image.src = URL.createObjectURL(event.target.files[0]);
};