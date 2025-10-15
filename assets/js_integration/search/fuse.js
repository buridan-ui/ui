// Fuse.js configuration (note: no require() since we load via CDN)
const fuseOptions = {
  keys: ["title", "author.firstName", "author.lastName"], // Added lastName
  includeScore: true,
  threshold: 0.3, // Adjust for search sensitivity
};

let fuse; // This will store the Fuse instance

// Initialize Fuse.js with data
function initializeFuse(list) {
  try {
    fuse = new Fuse(list, fuseOptions);
    console.log("Fuse.js initialized successfully with", list.length, "items");
  } catch (error) {
    console.error("Error initializing Fuse.js:", error);
  }
}

// Perform a search
function searchFuse(query) {
  console.log("searchFuse called with query:", query);
  if (!fuse) {
    console.warn("Fuse.js not initialized yet");
    return [];
  }

  if (!query || query.trim() === "") {
    return [];
  }

  try {
    const results = fuse.search(query);
    console.log('Search results for "' + query + '":', results);
    return results;
  } catch (error) {
    console.error("Error during search:", error);
    return [];
  }
}

window.initializeFuse = initializeFuse;
window.searchFuse = searchFuse;

console.log("Search functions defined and attached to window");
