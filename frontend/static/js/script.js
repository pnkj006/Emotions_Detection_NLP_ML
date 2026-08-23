// ===============================
// Character Counter
// ===============================

const textarea = document.getElementById("text");
const charCount = document.getElementById("charCount");

if (textarea && charCount) {

    function updateCounter() {
        charCount.textContent = textarea.value.length;
    }

    updateCounter();

    textarea.addEventListener("input", updateCounter);

}


// ===============================
// Load Example Text
// ===============================

function loadExample(text) {

    if (!textarea) return;

    textarea.value = text;

    charCount.textContent = textarea.value.length;

    textarea.focus();

}


// ===============================
// Clear Text
// ===============================

function clearText() {

    if (!textarea) return;

    textarea.value = "";

    charCount.textContent = 0;

    textarea.focus();

}


// ===============================
// Button Loading Animation
// ===============================

const form = document.querySelector("form");

if (form) {

    form.addEventListener("submit", function () {

        const button = document.querySelector(".primary-btn");

        button.disabled = true;

        button.innerHTML =
            '<i class="fa-solid fa-spinner fa-spin"></i> Analyzing...';

    });

}


// ===============================
// Animate Progress Bars
// ===============================

window.addEventListener("load", () => {

    const bars = document.querySelectorAll(".progress-fill");

    bars.forEach(bar => {

        const width = bar.style.width;

        bar.style.width = "0";

        setTimeout(() => {

            bar.style.width = width;

        }, 300);

    });

});


// ===============================
// Fade-in Result Card
// ===============================

window.addEventListener("load", () => {

    const result = document.querySelector(".result-card");

    if (result) {

        result.style.opacity = "0";

        result.style.transform = "translateY(30px)";

        setTimeout(() => {

            result.style.transition =
                "all 0.8s ease";

            result.style.opacity = "1";

            result.style.transform =
                "translateY(0px)";

        }, 150);

    }

});


// ===============================
// Smooth Scroll to Result
// ===============================

window.addEventListener("load", () => {

    const result = document.querySelector(".result-card");

    if (result) {

        setTimeout(() => {

            result.scrollIntoView({

                behavior: "smooth",

                block: "start"

            });

        }, 500);

    }

});


// ===============================
// Card Hover Animation
// ===============================

const cards = document.querySelectorAll(".card");

cards.forEach(card => {

    card.addEventListener("mouseenter", () => {

        card.style.transform = "translateY(-6px)";

    });

    card.addEventListener("mouseleave", () => {

        card.style.transform = "translateY(0px)";

    });

});


// ===============================
// Auto Resize Textarea
// ===============================

if (textarea) {

    textarea.addEventListener("input", function () {

        this.style.height = "180px";

        this.style.height = this.scrollHeight + "px";

    });

}