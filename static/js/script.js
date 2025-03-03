document.addEventListener("DOMContentLoaded", function () {
    const floorSelect = document.getElementById("floor");
    const departmentSelect = document.getElementById("department");
    const labSelect = document.getElementById("lab");

    const labsByFloor = {
        1: ["Microbiology", "Biochemistry", "Hematology", "Genetics", "Pathology", "Pharmacology"],
        2: ["Molecular Biology", "Cellular Biology", "Immunology", "Clinical Chemistry", "Virology", "Neuroscience"],
        3: ["Toxicology", "Forensic Science", "Botany Research", "Marine Biology", "Geochemistry", "Astrobiology"],
        4: ["DNA Sequencing", "Proteomics", "Biophysics", "Quantum Biology", "Stem Cell Research", "Bioinformatics"],
        5: ["Nuclear Medicine", "Epidemiology", "Bacteriology", "Chemical Engineering", "Nano Biotech", "Zoology"],
        6: ["Genetic Engineering", "Computational Biology", "Synthetic Biology", "Bio-nanotechnology", "Microfluidics", "Biomedical Imaging"],
        7: ["Radiology", "Pathogen Research", "Virus Cultivation", "Antibiotic Development", "Ecosystem Research", "Biosecurity"],
        8: ["Agricultural Biotechnology", "Food Chemistry", "Industrial Biotech", "Environmental Biotech", "Bioremediation", "Neuropharmacology"],
        9: ["Paleobiology", "Biomechanics", "Bioethics", "Tissue Engineering", "Neurosurgery Labs", "Artificial Organs"],
        10: ["Human Anatomy", "Bio-inspired Engineering", "Medical Robotics", "Regenerative Medicine", "Endocrinology", "Biomechatronics"],
        11: ["Astrobiology", "Space Medicine", "Cryogenics", "Extremophile Research", "Lunar Farming", "Exoplanet Biology"],
        12: ["Biomechatronics", "Genetic Data Science", "CRISPR Labs", "Xenobiology", "Virtual Brain Modeling", "AI in Biomedicine"],
        13: ["Biocybernetics", "Human Enhancement", "Cybernetic Organisms", "Brain-Machine Interfaces", "Transhumanism Studies", "Longevity Research"]
    };

    const labsByDepartment = {
        "Biochemistry": ["Protein Analysis", "Metabolism Studies", "Chemical Synthesis"],
        "Genetics": ["Genome Editing", "DNA Replication", "Genomic Analysis"],
        "Neuroscience": ["Brain Mapping", "Neural Networks", "Cognitive Research"],
        "Microbiology": ["Bacterial Cultures", "Virus Research", "Pathogen Resistance"],
        "Biomedical": ["Medical Devices", "Artificial Tissues", "Pharmaceutical Research"],
        "Astrobiology": ["Space Adaptation", "Extraterrestrial Life", "Radiation Effects"]
    };

    function forceReflow(element) {
        element.style.display = "none"; // Hide element
        element.offsetHeight; // Trigger reflow
        element.style.display = "block"; // Show element again
    }

    function updateLabs() {
        console.log("Updating lab list...");

        const selectedFloor = floorSelect.value;
        const selectedDepartment = departmentSelect.value;

        console.log("Selected floor:", selectedFloor);
        console.log("Selected department:", selectedDepartment);

        labSelect.innerHTML = "<option value=''>Select Laboratory</option>";

        let labs = [];

        if (selectedFloor in labsByFloor) {
            console.log("Adding labs from floor:", labsByFloor[selectedFloor]);
            labs = labs.concat(labsByFloor[selectedFloor]);
        }

        if (selectedDepartment in labsByDepartment) {
            console.log("Adding labs from department:", labsByDepartment[selectedDepartment]);
            labs = labs.concat(labsByDepartment[selectedDepartment]);
        }

        if (labs.length === 0) {
            console.log("No labs found!");
        }

        labs.forEach(lab => {
            let option = document.createElement("option");
            option.value = lab;
            option.textContent = lab;
            labSelect.appendChild(option);
        });

        console.log("Final lab list:", labs);

        // 🟢 Force re-render
        forceReflow(labSelect);
    }

    floorSelect.addEventListener("change", updateLabs);
    departmentSelect.addEventListener("change", updateLabs);
    updateLabs();
});
