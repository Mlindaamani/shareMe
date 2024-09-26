const form = document.querySelector("form");
form.addEventListener("submit", (Event) => {
  if (!form.checkValidity()) {
    Event.preventDefault();
    Event.stopImmediatePropagation();
  }
  form.classList.add("was-validated");
});
