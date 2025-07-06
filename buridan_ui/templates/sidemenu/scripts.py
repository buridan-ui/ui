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

TableOfContentScript = """
function highlightActiveTOCLink() {
  const currentPath = window.location.pathname.replace(/\\/+$|\\/$/g, ""); // Clean trailing slashes
  const currentHash = window.location.hash; // Get the fragment identifier

  if (!currentHash) return; // If no hash, don't attempt to highlight anything

  // Combine the currentPath with the hash to make a full path (like /charts/bar-charts#bar-v7)
  const activeLinkId = currentPath + currentHash;

  const activeItem = document.getElementById(activeLinkId.slice(1)); // Remove the leading # from currentHash

  if (activeItem) {
    const link = activeItem.querySelector("a");
    if (link) {
      const label = link.querySelector("label, span, div") || link;

      // Remove the active classes from all links
      document.querySelectorAll("[id^='/charts'] a").forEach(l => {
        const lbl = l.querySelector("label, span, div") || l;
        lbl.classList.remove("text-blue-600", "font-bold");
      });

      // Add the active classes to the selected link
      label.classList.add("text-blue-600", "font-bold");
    }
  }
}

// Run on page load after a short delay
window.addEventListener("load", () => setTimeout(highlightActiveTOCLink, 200));  // Increase delay

// Run on browser history navigation (back/forward)
window.addEventListener("popstate", () => {
  setTimeout(highlightActiveTOCLink, 200);
});

// Run after clicking any TOC link (client-side navigation)
document.querySelectorAll("a[href^='/charts']").forEach(link => {
  link.addEventListener("click", () => {
    setTimeout(highlightActiveTOCLink, 800);  // Delay for navigation
  });
});


"""
