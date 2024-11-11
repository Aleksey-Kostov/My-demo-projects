function previewPhotos() {
    const fileInput = document.getElementById('photos');
    const photoPreview = document.getElementById('photo-preview');
    const fileHelp = document.getElementById('fileHelp');
    const files = fileInput.files;

    // Clear previous previews
    photoPreview.innerHTML = '';
    photoPreview.style.display = 'block';
    fileHelp.textContent = 'You can upload up to 10 photos.';

    // Limit to 10 photos
    if (files.length > 10) {
        fileInput.setCustomValidity('You can upload up to 10 photos.');
        fileInput.reportValidity();
    } else {
        fileInput.setCustomValidity('');
    }

    // Display selected photos
    Array.from(files).forEach((file, index) => {
        if (index < 10) {
            const reader = new FileReader();
            reader.onload = function(event) {
                const img = document.createElement('img');
                img.src = event.target.result;
                img.classList.add('img-thumbnail');
                img.style.width = '100px';
                img.style.marginRight = '10px';
                photoPreview.appendChild(img);
            };
            reader.readAsDataURL(file);
        }
    });
}

function togglePriceFields() {
    const priceSelect = document.getElementById('price');
    const pricePerUnitField = document.getElementById('price-per-unit');
    const priceAllQuantityField = document.getElementById('price-all-quantity');

    // Hide all price fields
    pricePerUnitField.style.display = 'none';
    priceAllQuantityField.style.display = 'none';

    // Show the appropriate price field based on the selected option
    if (priceSelect.value === 'per_quantity') {
        pricePerUnitField.style.display = 'block';
    } else if (priceSelect.value === 'all_quantity') {
        priceAllQuantityField.style.display = 'block';
    }
}
