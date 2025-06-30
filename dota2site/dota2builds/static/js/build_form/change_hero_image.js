(() => {
const heroSelect = document.getElementById("id_hero");
const heroImg = document.getElementById("hero-img");

function changeHeroImg() {
    heroImg.classList.remove(heroImg.classList.item(1));
    const hero_slug = heroSelect.options[heroSelect.selectedIndex].text.toLowerCase().replace(" ", "");
    heroImg.classList.add(hero_slug);
}

changeHeroImg();
heroSelect.addEventListener("change", changeHeroImg);
})()
