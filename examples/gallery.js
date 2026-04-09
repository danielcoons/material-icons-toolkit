const gallery = document.getElementById("gallery");
const searchInput = document.getElementById("search");
const sizeSelector = document.getElementById("sizeSelector");

let icons = [];

// 🔹 Load icon index (recommended)
async function loadIcons() {
  try {
    const res = await fetch("../icons/metadata/icons.json");
    icons = await res.json();
  } catch (e) {
    console.warn("No metadata file found. Using fallback.");
  }

  render();
}

// 🔹 Render icons
function render() {
  const size = sizeSelector.value;
  const query = searchInput.value.toLowerCase();

  gallery.innerHTML = "";

  const filtered = icons.filter(icon =>
    icon.name.toLowerCase().includes(query)
  );

  filtered.forEach(icon => {
    const card = document.createElement("div");
    card.className = "icon-card";

    const img = document.createElement("img");
    img.src = `../icons/png/${size}/${icon.name}.png`;
    img.width = size;
    img.height = size;

    const label = document.createElement("div");
    label.className = "icon-name";
    label.textContent = icon.name;

    card.appendChild(img);
    card.appendChild(label);
    gallery.appendChild(card);
    card.onclick = () => {
    navigator.clipboard.writeText(icon.name);
};

  });
}

// 🔹 Events
searchInput.addEventListener("input", render);
sizeSelector.addEventListener("change", render);

// Init
loadIcons();
