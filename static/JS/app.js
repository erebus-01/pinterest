let pin_image_blob = null;

document.querySelector('#upload_img').addEventListener('change', event => {
  if(event.target.files && event.target.files[0]){
    if(/image\/*/.test(event.target.files[0].type)){
      const reader = new FileReader();

      reader.onload = () => {
        const new_image = new Image();

        new_image.src = reader.result;
        pin_image_blob = reader.result;

        new_image.onload = () => {
          const modals_pin = document.querySelector('.add_pin_modal .modals_pin');
          const trash_btn = document.querySelector('#trash_btn');

          new_image.classList.add('pin_max_width');

          document.querySelector('.add_pin_modal .pin_image').appendChild(new_image);
          document.querySelector('#upload_img_label').style.display = 'none';

          console.log(new_image)

          modals_pin.style.display = 'block';

          if(new_image.getBoundingClientRect().width < new_image.parentElement.getBoundingClientRect().width || 
          new_image.getBoundingClientRect().height < new_image.parentElement.getBoundingClientRect().height)
          {
            new_image.classList.remove('pin_max_width');
            new_image.classList.add('pin_max_height');
          }
          modals_pin.style.opacity = 1;
          trash_btn.style.opacity = 1;
          trash_btn.style.display = 'flex';
        }
      }

      reader.readAsDataURL(event.target.files[0]);

    }
  }
  document.querySelector('#upload_img').value = '';
})

document.querySelector('#trash_btn').addEventListener('click', event => {
  const modals_pin_img = document.querySelector('.add_pin_modal .modals_pin img');
  const modals_pin = document.querySelector('.add_pin_modal .modals_pin');

  document.querySelector('#upload_img_label').style.display = 'block';
  modals_pin_img.remove(); 

  modals_pin.style.opacity = 0;
  modals_pin.style.display = 'none';

  trash_btn.style.opacity = 0;
  trash_btn.style.display = 'none';
})


var autoExpandingTextArea = (function(){
  var tag = document.querySelectorAll('textarea');
 
  for (var i=0; i<tag.length; i++){
    tag[i].addEventListener('paste',autoExpand);
    tag[i].addEventListener('input',autoExpand);
    tag[i].addEventListener('keyup',autoExpand);
  }
  
  function autoExpand(e,el){
    var el = el || e.target;
    var paddingTop = parseInt(window.getComputedStyle(el, null).getPropertyValue('padding-top'));
    var paddingBottom = parseInt(window.getComputedStyle(el, null).getPropertyValue('padding-bottom'));
    el.style.height = 'auto';
    console.log(el.scrollHeight);
    el.style.height = (el.scrollHeight - (paddingTop + paddingBottom)) + 'px';
  }
  
  window.addEventListener('load',expandAll);
  window.addEventListener('resize',expandAll);
  
  function expandAll(e){
    var tag = document.querySelectorAll('textarea');
    
    for (var i=0; i<tag.length; i++){
      autoExpand(e,tag[i]);
    }
  }
})();
