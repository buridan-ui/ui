SideBarScript = """
function highlightActiveSidebarLink() {
  const currentPath = window.location.pathname.replace(/\\/+$|\\/$/g, ""); // Clean trailing slashes
  const activeItem = document.getElementById(currentPath);

  if (activeItem) {
    const link = activeItem.querySelector("a");
    if (link) {
      const label = link.querySelector("label, span, div") || link;

      document.querySelectorAll("[id^='/'] a").forEach(l => {
        const lbl = l.querySelector("label, span, div") || l;
        lbl.classList.remove("text-blue-600", "font-bold");
      });

      label.classList.add("text-blue-600", "font-bold");

      // Center the active item in the scroll area
      activeItem.scrollIntoView({ block: "center" });
    }
  }
}

// Run on page load after a short delay
setTimeout(highlightActiveSidebarLink, 50);

// Run on browser history navigation (back/forward)
window.addEventListener("popstate", () => {
  setTimeout(highlightActiveSidebarLink, 50);
});

// Run after clicking any sidebar link (client-side navigation)
document.querySelectorAll("a[href^='/']").forEach(link => {
  link.addEventListener("click", () => {
    setTimeout(highlightActiveSidebarLink, 800);
  });
});
"""
