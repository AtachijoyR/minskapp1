<script>
    import axios from 'axios';

    let listaAnimales = [];
    let datoAnimal = "";

    const sendData = () => {

        let formu = document.getElementById('formu').value;

        console.log(datoAnimal);
        
        axios.get('http://127.0.0.1:8000/Buscar-Mascotas/' + datoAnimal + '/')
            .then(res => {
                listaAnimales = res.data;
                console.log(res);
            })
    }

</script>

<main>
    <form id="formu">
        <input type = "text" id="id" name="id" bind:value={datoAnimal}>
        <button on:click|preventDefault = {sendData}> Enviar</button>
    </form>

    {#await listaAnimales}
        Loading...
    {:then ListaAnimales}
        <ul>
            {#each listaAnimales as animal}
                <li> {animal.name} </li>
            {/each}
        </ul>

    {:catch error}
        {error}
    {/await}

</main>