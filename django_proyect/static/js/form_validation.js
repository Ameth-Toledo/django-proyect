document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.product-form');
    const imageField = document.querySelector('#id_image'); 

    form.addEventListener('submit', function (event) {
        const imageUrl = imageField.value;

        if (imageUrl.length > 255) {
            alert('La URL de la imagen no puede exceder los 255 caracteres.');
            event.preventDefault();
        }
    });
});
