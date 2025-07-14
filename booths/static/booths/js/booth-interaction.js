// booths/static/booths/js/booth-interaction.js

document.addEventListener("DOMContentLoaded", function () {
  const filterFloor = document.getElementById("filter-floor");
  const filterStatus = document.getElementById("filter-status");
  const sortBy = document.getElementById("sort-by");
  const boothCards = document.querySelectorAll(".booth-card");
  const modal = document.getElementById("booth-modal");
  const modalContent = document.getElementById("modal-content");
  const modalClose = document.querySelector(".modal-close");

  // Filter Function
  function filterAndSortBooths() {
    const floorValue = filterFloor.value;
    const statusValue = filterStatus.value;
    const sortValue = sortBy.value;

    const boothsArray = Array.from(boothCards);

    boothsArray.forEach((card) => {
      const boothFloor = card.getAttribute("data-floor");
      const boothStatus = card.getAttribute("data-status");

      const matchesFloor = !floorValue || boothFloor === floorValue;
      const matchesStatus = !statusValue || boothStatus === statusValue;

      if (matchesFloor && matchesStatus) {
        card.style.display = "block";
      } else {
        card.style.display = "none";
      }
    });

    // Optional Sorting
    if (sortValue) {
      boothsArray.sort((a, b) => {
        if (sortValue === "time") {
          return a.getAttribute("data-time").localeCompare(b.getAttribute("data-time"));
        }
        if (sortValue === "availability") {
          return a.getAttribute("data-status").localeCompare(b.getAttribute("data-status"));
        }
        return 0;
      });

      const container = document.querySelector(".booth-grid");
      boothsArray.forEach((card) => container.appendChild(card));
    }
  }

  // Modal Handling
  boothCards.forEach((card) => {
    card.addEventListener("click", () => {
      const boothDetails = card.querySelector(".booth-details").innerHTML;
      modalContent.innerHTML = boothDetails;
      modal.style.display = "flex";
    });
  });

  modalClose?.addEventListener("click", () => {
    modal.style.display = "none";
    modalContent.innerHTML = "";
  });

  window.addEventListener("click", (event) => {
    if (event.target === modal) {
      modal.style.display = "none";
      modalContent.innerHTML = "";
    }
  });

  // Bind filter events
  filterFloor?.addEventListener("change", filterAndSortBooths);
  filterStatus?.addEventListener("change", filterAndSortBooths);
  sortBy?.addEventListener("change", filterAndSortBooths);
});
