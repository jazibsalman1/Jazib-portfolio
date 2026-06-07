// CONTACT FORM (FASTAPI CALL)
const form = document.getElementById("contactForm");
const msg = document.getElementById("responseMsg");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(form);

    const res = await fetch("/contact", {
        method: "POST",
        body: formData
    });

    const data = await res.json();

    msg.innerText = data.msg;
    msg.style.color = "lightgreen";

    form.reset();
});


// // DARK MODE TOGGLE
// const toggle = document.createElement("button");
// toggle.innerText = "🌙";
// toggle.className = "btn";
// document.body.appendChild(toggle);

// toggle.style.position = "fixed";
// toggle.style.bottom = "20px";
// toggle.style.right = "20px";

// toggle.addEventListener("click", () => {
//     document.body.classList.toggle("light-mode");
// });

// console.log("Pro Portfolio Loaded 🚀");
// AOS.init({
//     duration: 1000,
//     once: true
// });

// CONTACT FORM
document.getElementById("contactForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);

    const res = await fetch("/contact", {
        method: "POST",
        body: formData
    });

    const data = await res.json();

    document.getElementById("msg").innerText = data.msg;
    e.target.reset();
});


const text = [
    "Python Developer",
    "FastAPI Builder",
    "Backend Engineer",
    "API Architect"
];

let i = 0;
let j = 0;
let current = "";
let isDeleting = false;

function type() {
    current = text[i];

    if (!isDeleting) {
        j++;
        document.getElementById("typing").innerText = current.substring(0, j);

        if (j === current.length) {
            isDeleting = true;
            setTimeout(type, 1200);
            return;
        }
    } else {
        j--;
        document.getElementById("typing").innerText = current.substring(0, j);

        if (j === 0) {
            isDeleting = false;
            i = (i + 1) % text.length;
        }
    }

    setTimeout(type, isDeleting ? 50 : 100);
}

type();