<script>
    import{user} from '../stores/store';
    import {navigate} from 'svelte-routing';
    import {onMount} from "svelte";

    function logout(){
        user.logoutUser();
        navigate('/');
        localStorage.clear();
    }
    onMount(() =>{
        if(!$user){
        navigate("/");
        }
    });

</script>


<h1>Cerrar Sesion</h1>

<button on:click={logout}>Salir</button>