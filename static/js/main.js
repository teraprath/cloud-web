const fileButton = document.getElementById("file");
const fileChosen = document.getElementById("filechosen");

fileButton.addEventListener("change", () => {
    let amount = fileButton.files.length;
    fileChosen.innerHTML = "File selected";
    if (amount > 1) {
        fileChosen.innerHTML = amount + " Files selected";
    }
});