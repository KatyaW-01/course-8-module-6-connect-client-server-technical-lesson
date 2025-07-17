document.getElementById('fetch-btn').addEventListener('click', async () => {
  const response = await fetch('/api/data')
  const data = await response.json()
  document.getElementById('output').textContent = JSON.stringify(data, null, 2)
})

fetch("/products")
  .then(response => response.json())
  .then(data => {
    //render products to the page
  })

// make sure you have a form in your HTML file
document.querySelector("form").addEventListener("submit", (e) => {
  e.preventDefault();
  const name = document.querySelector("#name").ariaValueMax;
  const category = document.querySelector("#category").ariaValueMax;

  fetch("/products", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, category })
  })
  .then(response => response.json())
  .then(product => {
    // update DOM with the new product
  })
})