
<script>
    import axios from 'axios';
    import { onMount } from "svelte";
import { navigate } from 'svelte-routing';
import { loop_guard } from 'svelte/internal';
    import { Table } from 'sveltestrap';
    import {FormGroup, 
		Input, 
		Label, 
		Toast, 
		ToastHeader, 
		ToastBody, 
		Icon
	} from 'sveltestrap';
import Register from './Register.svelte';
    let id;
    let status;
    let listaAnimales;
    let animals = [];
    let Tokens = [];
    const getUsers = ()=>{
        axios.get('http://127.0.0.1:8000/Listar-Mascotas/')
        .then(res=>{
            animals = res.data;
            
        })
    }
    onMount(getUsers);
    const postUsers = ()=>{
        axios.post('http://127.0.0.1:8000/generar_token/',{
            username: 'atachijoy',
            password: '123'
        })
        .then(res =>{
            Tokens = res.data;
            
        })
    }
    onMount(postUsers);
    function modifyStatus(){
        if(status == 'Sano'){
            status = '0';   
        }
        else if(status == 'En pabellón'){
            status = '1';
        }
        else if(status == 'En observación'){
            status = '2';
        }
        else if(status == 'Otro'){
            status = '3';
        }
        axios.patch("http://127.0.0.1:8000/Actualizar-Mascotas/"+id+"/",{
            "status": status,
        })
        navigate("/");
    }
</script>


<h1>Registro de mascotas</h1>
<div id="main-container">
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
            {#await animals}
                Loading...
            {:then animals}
                {#each animals as animal }
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

    <h2>Modificar estado:</h2>
    <label for="id">
        id:
        <input type="text" id="id" bind:value={id}/>
    </label>

        <Label for="status">Estado</Label>
        <Input bind:value={status} type="select" name="select" id="exampleSelect">
          <option>Sano</option>
          <option>En observación</option>
          <option>En pabellón</option>
          <option>Otro</option>
        </Input>
    <button on:click={modifyStatus}>Modificar estado</button>
 
</div>

<style>
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
    h2 {
        margin:  20px auto;
        color: #0050A0;
        font-family:'Lucida Sans';
        font-size: 1.5em;
        text-align:left;
    }
</style>
