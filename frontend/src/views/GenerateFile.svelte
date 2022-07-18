<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/1.3.4/jspdf.min.js">
    var description;
    var name;
    
    /*
    Esta función permite crear la lógica para emitir un certificado, 
    para ello, se debe ingresar el nombre de la mascota, junto a un
    motivo por el cual se solicita el certificado.
    */
    function generate(){
            var doc = new jsPDF(); 
            doc.text("La mascota: " + name + "\n")       
            doc.text(description, 10, 10);
            doc.save("Certificado.pdf");
    }
</script>

<body>
    <label for="name">
        Nombre de mascota:
        <input type="text" id="name" bind:value={name}/>
    </label>
   <label for="description">
        Motivo:
        <input type="text" id="description" bind:value={description}/>
    </label>
    <button on:click={generate}>Emitir certificado</button>
</body>

