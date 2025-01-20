document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.querySelector('.toggle-btn');
    const menu = document.querySelector('.menu');

    toggleButton.addEventListener('click', function () {
        menu.classList.toggle('active');
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('.btn-delete');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            const confirmation = confirm('Are you sure you want to delete this task?');
            if (!confirmation) {
                e.preventDefault();
            }
        });
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const deleteButton = document.querySelector('.btn-delete');

    if (deleteButton) {
        deleteButton.addEventListener('click', function (e) {
            const confirmDelete = confirm('Are you sure you want to delete this task?');
            if (!confirmDelete) {
                e.preventDefault();
            }
        });
    }
});

// Add form validation for required fields
document.addEventListener("DOMContentLoaded", () => {
    const forms = ["#loginForm", "#registerForm"];
    forms.forEach(formId => {
        const form = document.querySelector(formId);
        if (form) {
            form.addEventListener("submit", (event) => {
                let isValid = true;
                form.querySelectorAll("input").forEach(input => {
                    if (!input.value.trim()) {
                        isValid = false;
                        input.classList.add("is-invalid");
                    } else {
                        input.classList.remove("is-invalid");
                    }
                });
                if (!isValid) {
                    event.preventDefault();
                    alert("Please fill in all required fields.");
                }
            });
        }
    });
});
document.addEventListener('DOMContentLoaded', function () {
    // Automatically hide messages after 5 seconds
    const messageElements = document.querySelectorAll('.messages');
    messageElements.forEach(message => {
        setTimeout(() => {
            message.style.display = 'none';
        }, 5000);
    });
});
document.addEventListener("DOMContentLoaded", function () {
    const paginationLinks = document.querySelectorAll(".pagination .page-link");

    paginationLinks.forEach(function (link) {
        link.addEventListener("click", function (event) {
            // Prevent default behavior
            event.preventDefault();

            // Fetch the href from the clicked link
            const url = this.getAttribute("href");

            // Scroll smoothly to the top
            window.scrollTo({ top: 0, behavior: "smooth" });

            // Update the URL to load the new page
            setTimeout(function () {
                window.location.href = url;
            }, 300);
        });
    });
});
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll to top when error link is clicked
    const errorLink = document.querySelector('.error-link');
    if (errorLink) {
        errorLink.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
            window.location.href = errorLink.href; // Go to Home
        });
    }
});
