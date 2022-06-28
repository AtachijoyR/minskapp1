
<script>
    import axios from 'axios';
    import { onMount } from "svelte";
    let usuarios = [];
    let Tokens = [];
    const getUsers = ()=>{
        axios.get('http://127.0.0.1:8000/Listar-Mascotas/')
        .then(res=>{
            usuarios = res.data;

            console.log(res);
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
            console.log(Tokens)
        })
    }
    onMount(postUsers);

</script>

{#await usuarios}
    Loading...
{:then usuarios}
    <ul>
        {#each usuarios as animal }
            <li>{animal.name}</li>
        {/each}
    </ul>
{:catch error}
    {error}
{/await}
