document.querySelectorAll(".score-toggle").forEach((button) => {
  const score = document.getElementById(button.getAttribute("aria-controls"));
  button.addEventListener("click", () => {
    score.hidden = !score.hidden;
    button.setAttribute("aria-expanded", String(!score.hidden));
  });
});
