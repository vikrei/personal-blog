const toggleButton = document.querySelector("#toggle-comment-form");
const commentForm = document.querySelector("#comment-form");

if (toggleButton && commentForm) {
    toggleButton.addEventListener("click", () => {
        commentForm.classList.toggle("hidden");
    });
}

const postForm = document.querySelector("#post-form");

if (postForm) {
    postForm.addEventListener("submit", (event) => {
        event.preventDefault();

        alert("Post created successfully!");
    });
}