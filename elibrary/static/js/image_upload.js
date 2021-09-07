const inputFile = document.getElementById("input_file");
const previewImage = document.getElementById("avatar_img");


inputFile.addEventListener("change", function () {
    const file = this.files[0];

    if (file) {
        const reader = new FileReader();
        reader.addEventListener("load", function () {
            console.log(this);
            previewImage.setAttribute("src", this.result)
        })
        reader.readAsDataURL(file);
    }
});