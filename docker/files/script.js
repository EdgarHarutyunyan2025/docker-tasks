document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById("modal");
    const btn = document.getElementById("contactBtn");
    const span = document.getElementsByClassName("close")[0];

    // Открытие модального окна
    btn.onclick = function() {
        modal.style.display = "block";
    }

    // Закрытие модального окна
    span.onclick = function() {
        modal.style.display = "none";
    }

    // Закрытие модального окна при клике вне него
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});
