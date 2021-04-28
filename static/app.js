function animatedForm(){
    const arrows = document.querySelectorAll('.bi-arrow-right');
    const covidForm = document.getElementById('covid-form');
    // const checkbox = document.querySelectorAll('input[type=checkbox]');

    arrows.forEach(arrow=>{
        arrow.addEventListener('click', ()=>{
            const input = arrow.previousElementSibling;
            const parent = arrow.parentElement;
            const nextForm = parent.nextElementSibling;
            
            console.log(input.type)

            //check for validation
            if(input.type === 'text' && validatePlace(input)){
                nextSlide(parent, nextForm);
            }else if(input.type === undefined){
                // nextSlide(parent, nextForm);
                covidForm.submit();
            }
        })
    });
}

function validatePlace(place){
    if(place.value.length < 1){
        console.log("not enough characters");
        error("rgb(189, 87, 87)");
    }else{
        error("rgb(87, 189, 130)");
        return true;
    }
}


function nextSlide(parent, nextForm){
    parent.classList.add('inactive');
    parent.classList.remove('active');
    nextForm.classList.remove('inactive');
    nextForm.classList.add('active');
}

function error(color){
    document.body.style.backgroundColor = color
}

animatedForm();