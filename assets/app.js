const state = { category: "all", query: "" };

const ICON_COLORS = ["#8b5cf6", "#34d399", "#fb923c", "#60a5fa", "#f472b6", "#2dd4bf"];
const STAR_SVG = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l2.9 6.9L22 10l-5.5 4.8L18 22 12 18.5 6 22l1.5-7.2L2 10l7.1-.9L12 2z"/></svg>`;
const DL_SVG = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v12m0 0l4-4m-4 4l-4-4M4 17v2a2 2 0 002 2h12a2 2 0 002-2v-2"/></svg>`;
const KEY_SVG = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="8" cy="8" r="3"/><path d="M11 11l9 9"/></svg>`;

async function loadManifest() {
  const res = await fetch("data/skills.json");
  if (!res.ok) throw new Error("Failed to load skills.json");
  return res.json();
}

function iconColor(id, index) {
  let hash = 0;
  for (let i = 0; i < id.length; i++) hash = (hash + id.charCodeAt(i) * (i + 1)) % ICON_COLORS.length;
  return ICON_COLORS[(hash + index) % ICON_COLORS.length];
}

function initials(name) {
  return (name || "?").split("-").map((p) => p[0]).join("").slice(0, 1).toUpperCase();
}

function formatCount(n) {
  if (n >= 10000) return `${(n / 10000).toFixed(1)} 万`;
  return String(n);
}

function renderTabs(categories, activeId) {
  const root = document.getElementById("category-tabs");
  root.innerHTML = "";
  categories.forEach((cat) => {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = `tab-btn${cat.id === activeId ? " active" : ""}`;
    btn.textContent = cat.label;
    btn.setAttribute("role", "tab");
    btn.addEventListener("click", () => { state.category = cat.id; render(); });
    root.appendChild(btn);
  });
}

function matches(skill) {
  const q = state.query.trim().toLowerCase();
  const inCategory = state.category === "all" || (skill.categories || []).includes(state.category);
  if (!inCategory) return false;
  if (!q) return true;
  return [skill.name, skill.title, skill.description, ...(skill.tags || [])].join(" ").toLowerCase().includes(q);
}

function rowHtml(skill, index) {
  const detail = skill.detailUrl || `skills/${skill.id}/`;
  const color = skill.iconColor || iconColor(skill.id, index);
  const letter = skill.iconLetter || initials(skill.name);
  const stars = skill.stats?.stars ?? 0;
  const downloads = skill.stats?.downloads ?? 0;
  const source = skill.source || "Allen Skills";
  const apiBadge = skill.needsApiKey ? `<span class="badge-api">${KEY_SVG}需配置 API Key</span>` : "";

  return `<a class="skill-row" href="${detail}" role="listitem">
    <div class="skill-icon" style="background:${color}">${letter}</div>
    <div class="skill-body">
      <div class="skill-title-row"><h3 class="skill-title">${skill.title}</h3>${apiBadge}</div>
      <p class="skill-desc">${skill.description}</p>
    </div>
    <div class="skill-meta">
      <span class="meta-item">${STAR_SVG}${stars}</span>
      <span class="meta-item">${DL_SVG}${formatCount(downloads)}</span>
      <span class="meta-source">来自 ${source}</span>
    </div>
  </a>`;
}

function renderList(skills) {
  const list = document.getElementById("skills-list");
  const empty = document.getElementById("empty-state");
  const filtered = skills.filter(matches);
  list.innerHTML = filtered.map((s, i) => rowHtml(s, i)).join("");
  empty.classList.toggle("hidden", filtered.length > 0);
}

function render() {
  if (!window.__manifest) return;
  const { categories, skills, site } = window.__manifest;
  renderTabs(categories, state.category);
  renderList(skills);
  const visible = skills.filter(matches).length;
  document.getElementById("hero-count").textContent = `共 ${skills.length} 个技能 · 当前显示 ${visible} 个`;
  if (site?.subtitle) document.getElementById("hero-subtitle").textContent = site.subtitle;
}

async function init() {
  document.getElementById("year").textContent = String(new Date().getFullYear());
  window.__manifest = await loadManifest();
  document.getElementById("search-input").addEventListener("input", (e) => { state.query = e.target.value; render(); });
  document.getElementById("clear-filters").addEventListener("click", () => {
    state.category = "all"; state.query = ""; document.getElementById("search-input").value = ""; render();
  });
  render();
}

init().catch((err) => {
  console.error(err);
  document.getElementById("skills-list").innerHTML = "<p style='color:#ef4444;padding:24px 0'>无法加载 skills.json</p>";
});
