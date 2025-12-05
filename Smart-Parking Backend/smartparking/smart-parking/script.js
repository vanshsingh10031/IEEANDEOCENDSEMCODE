let darkMode = true;

document.getElementById("themeToggle").onclick = () => {
    darkMode = !darkMode;
    document.body.classList.toggle("light");
    localStorage.setItem("theme", darkMode ? "dark" : "light");
};

// Load saved theme
if (localStorage.getItem("theme") === "light") {
    document.body.classList.add("light");
}
