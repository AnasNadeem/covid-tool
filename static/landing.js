const loadContent = () => {

    window.onload = () => {
        document.getElementById('loader').style.display = 'none';
        document.querySelector('main').style.display = 'block';        
    }
}

loadContent();