<script>
    import axios from 'axios';
    import { Table } from 'sveltestrap';

    let animalList = [];
    let dataAnimal = "";

    /**
     * Función que retorna datos de un animal en específico,
     * según ID del animal puesto en el buscador y almacena
     * información en animalList.
    */
    const sendData = () => {

        axios.get('http://127.0.0.1:8000/Buscar-Mascotas/' + dataAnimal + '/')
            .then(res => {
                animalList = res.data;
            }
        )
    }
</script>
<h1>Buscador de mascotas</h1>
<main>
    <div id="main-container">
    <form id="formu">
        <input type="text" name="id" id="id" placeholder="Ingrese ID del animal" bind:value={dataAnimal}/>
        <button on:click|preventDefault = {sendData} class="btn btn-info"> Enviar</button>
        <Table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Raza</th>
                    <th>Edad (Meses)</th>
                    <th>Peso</th>
                    <th>Estado</th>
                    <th>Rut Dueño</th>
                </tr>
            </thead>
            <tbody>
                {#await animalList}
                        Loading...
                {:then animalList}
                    {#each animalList as animal}
                            <tr>
                                <td>{animal.id}</td>
                                <td>{animal.name}</td>
                                <td>{animal.breed}</td>
                                <td>{animal.age_months}</td>
                                <td>{animal.weight}</td>
                                <td>
                                {#if animal.status == "0"}
                                    {animal.status = "Sano"}
                                {/if}
                                {#if animal.status == "1"}
                                    {animal.status = "En pabellón"}
                                {/if}
                                {#if animal.status == "2"}
                                    {animal.status = "En observación"}
                                {/if}
                                {#if animal.status == "3"}
                                    {animal.status = "Otro"}
                                {/if}
                                </td>
                                <td>{animal.rut_owner}</td>
                            </tr>
                    {/each}
                {:catch error}
                    {error}
                {/await}
            </tbody>
        </Table>
    </form>
    </div>
</main>

<style>
    /**
    * Se editan los estilos de los documentos utilizados en la vista.
    */
    #main-container{
        margin:  20px auto;
        width: 1100px;
    }
    th, tr{
        text-align: center;
    }
    thead{
        background-color: #0050A0;
        border-bottom: solid 5px #0F362D;
        color: white;
    }
    tbody{
        background-color: white;
    }
    h1 {
        margin:  20px auto;
        color: #0050A0;
        font-family:'Lucida Sans';
        font-size: 2em;
        text-transform: uppercase;
        text-align: center;
        text-decoration: underline;
        text-shadow: 1px 1px 1px;
    }
    button {
        background-color: #0050A0;
    }
</style>