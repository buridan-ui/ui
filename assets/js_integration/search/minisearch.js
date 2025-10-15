let miniSearch;

// Initialize Minisearch with the loaded data
window.initializeMinisearch = function (data) {
  console.log("Initializing Minisearch with data:", data);

  // Create a new MiniSearch instance
  miniSearch = new MiniSearch({
    fields: ["title", "author.firstName", "author.lastName"], // fields to index for full-text search
    storeFields: ["title", "author"], // fields to return with search results
    searchOptions: {
      boost: { title: 2 }, // boost title matches
      fuzzy: 0.2, // enable fuzzy matching
      prefix: true, // enable prefix matching
      combineWith: "AND", // combine search terms with AND
    },
  });

  // Add IDs to documents if they don't have them
  const dataWithIds = data.map((item, index) => ({
    id: item.id || index, // Use existing ID or assign index as ID
    ...item,
  }));

  // Add all documents to the index
  miniSearch.addAll(dataWithIds);

  console.log("Minisearch initialized successfully");
};

// Search function that returns results in the same format as Fuse.js
window.searchMinisearch = function (searchQuery) {
  if (!miniSearch) {
    console.warn("Minisearch not initialized yet");
    return [];
  }

  if (!searchQuery || searchQuery.trim() === "") {
    return [];
  }

  console.log("Searching for:", searchQuery);

  try {
    // Perform the search
    const results = miniSearch.search(searchQuery, {
      fuzzy: 0.2,
      prefix: true,
      boost: { title: 2 },
    });

    console.log("Raw Minisearch results:", results);

    // Transform results to match Fuse.js format
    const transformedResults = results.map((result, index) => ({
      item: {
        title: result.title,
        author: result.author,
      },
      refIndex: result.id || index,
      score: 1 - result.score, // Invert score to match Fuse.js format (lower is better in Fuse)
    }));

    console.log("Transformed results:", transformedResults);
    return transformedResults;
  } catch (error) {
    console.error("Search error:", error);
    return [];
  }
};
