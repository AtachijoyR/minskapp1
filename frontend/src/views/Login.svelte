<script>
    import {setStorageUser, user} from "../stores/store";
    import {navigate} from "svelte-routing";
    import axios from "axios";
    let rut = "atachijoy";
    let password = "123";
    let tokens =[];
    let saveToken;

    /*
    Esta función retornará un Token del superusuario proveniente de
    la base de datos de Django Rest Framework  
    */
    const postUsers = ()=>{
        axios.post('http://127.0.0.1:8000/generar_token/',{
            username: rut,
            password: password
        })
        .then(res =>{
            tokens = res.data;
            saveToken= tokens.token;
        })
    }
    
    /**
     * Función inicia sesión de un determinado usuario.
     */
    function login(){
        postUsers();
        setTimeout(()=>{
            let userRegister = {
                username: rut,
                token: saveToken,
            };
            user.loginUser(userRegister);
            setStorageUser(userRegister);
            navigate('/')
        },1000);
    }

</script>

<h1>Login</h1>
<label for="name">
    Rut:
    <input type="text" id="name" bind:value={rut}/>

</label>

<label for="password">
    Password:
    <input type="password" id="password" bind:value={password}/>
</label>
<button on:click={login}>Login</button>
