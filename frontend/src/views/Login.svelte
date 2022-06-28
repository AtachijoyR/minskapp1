<script>
    import {setStorageUser, user} from "../stores/store";
    import {navigate} from "svelte-routing";
    import axios from "axios";
    let rut = "atachijoy";
    let password = "123";
    let Tokens =[];
    let guardarToken;



    const postUsers = ()=>{
        axios.post('http://127.0.0.1:8000/generar_token/',{
            username: rut,
            password: password
        })
        .then(res =>{
            Tokens = res.data;
            guardarToken= Tokens.token;
        })
    }
    
    function login(){
        postUsers();
        console.log("holaaaaaaaaa");
        setTimeout(()=>{
            let userRegistrado = {
                username: rut,
                token: guardarToken,
            };
            user.loginUser(userRegistrado);
            setStorageUser(userRegistrado);
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
