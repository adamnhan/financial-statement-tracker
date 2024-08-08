document.getElementById('fileInput').addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        const contents = e.target.result;
        // You can send contents to the backend or process them directly here
        console.log(contents);
      };
      reader.readAsText(file);
    }
  });
  