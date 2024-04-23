function ShowHideItem(itemId) {
    const x = document.getElementById(String(itemId))
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
