

<head>
    <title>Registro de mascotas</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/1.3.4/jspdf.min.js"></script>
    <script>import axios from 'axios';</script>
</head>

<body>
    <h1>holi</h1>
    <script>
        var listar;
        const searchAnimal(){
            axios.get('http://127.0.0.1:8000/Listar-Mascotas/')
            .then(res => {
                listar = res.data;
            })
        }
        searchAnimal();
        console.log(listar);
        var tex = "JASINTA";
        var doc = new jsPDF();        
        doc.text("holi" + tex, 10, 10);
        doc.save("a4.pdf");
    </script>
</body>