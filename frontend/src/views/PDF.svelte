<script>
    //import { jsPDF } from "jspdf";
    import axios from 'axios';
    import { onMount } from "svelte";
    import {Table} from "sveltestrap";
    var animalList = [];

    /*
    Esta función permite obtener el registro de una mascota
    */
    const searchAnimal = ()=>{
        axios.get('http://127.0.0.1:8000/Listar-Mascotas/')
        .then(res => {
            animalList = res.data;
        })
    }
    onMount(searchAnimal);
    //const { jsPDF } = require("jspdf"); // will automatically load the node version

    const doc = new jsPDF();
    doc.text("Hello world!", 10, 10);
    doc.save("a4.pdf"); // will save the file in the current working directory
    
    //var tex = "Prueba";
    //var doc = new jsPDF();        
    //doc.text("holi" + tex, 10, 10);
    //doc.save("a4.pdf");
</script>

<!--
<head>
    <title>Registro de mascotas</title>
    <script src="https://unpkg.com/jspdf@latest/dist/jspdf.umd.min.js"></script>
</head>
<body>
    {#await animalList}
                Loading...
    {:then animalList}
        {#each animalList as animal }
            {#if animal.status == "0"}
                <script>
                    doc.text(animal.ID);
                    doc.save("a4.pdf");
                </script>
            {/if}
        {/each}
    {:catch error}
    {error}
    {/await} 
</body>
-->