var settingsmenu = document.querySelector(".settings-menu");

function settingsMenuToggle() {
    settingsmenu.classList.toggle("settings-menu-height");
}

// Close the menu if the user clicks outside of it
document.addEventListener('click', function(event) {
    var isClickInsideMenu = settingsmenu.contains(event.target);
    var isClickOnUserIcon = document.querySelector('.nav-user-icon').contains(event.target);

    if (!isClickInsideMenu && !isClickOnUserIcon) {
        settingsmenu.classList.remove("settings-menu-height");
    }
});
