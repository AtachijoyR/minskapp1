<h1>Centro Veterinario CliniPet</h1>

<script lang="ts">
    import { navigate } from 'svelte-routing';

    import {
        Carousel,
        CarouselControl,
        CarouselIndicators,
        CarouselItem
    } from 'sveltestrap';

    import {user} from "../stores/store";
    function directView(){
        navigate('/visualize');
    }
    function directPet(){
        navigate('/searchPet');
    }
    function directRegister(){
        navigate('/register');
    }



    let isVeterinary = false;
    let isSecretary = false;
    try{
		let validation = $user.token

		if(validation == 'e17326d066fdc4820582422babe431c8cf1e65f2'){
			console.log("BIENVENIDO VETERINARIO");
            isVeterinary = true;
		}
        else if(validation == '8dcd6890b322daf80b2dc55e9fab83ddf2d6511f'){
            console.log("BIENVENIDA SECRETARIA");
            isSecretary = true;
        }
		}
	catch{
		console.log("ERROR");
	}

    const items = [
        {
        url: 'https://cloudfront-us-east-1.images.arcpublishing.com/infobae/Z2ZHWPOGBFAH7LPKCWLEU5XKCE.jpg',
        title: '',
        subTitle: ''
        },
        {
        url: 'https://smb.ibsrv.net/imageresizer/image/blog_images/1200x1200/23330/97482/0443241001547141937.jpg',
        title: '',
        subTitle: ''
        },
        {
        url: 'https://w0.peakpx.com/wallpaper/481/108/HD-wallpaper-happy-easter-rabbit-grass-easter-card-animal-cute-egg-green-bunny-rodent.jpg',
        title: '',
        subTitle: ''
        }
    ];
    let activeIndex = 0;
</script>
<div class="col-sm-6" style="width: 800px; margin-left: 50%; transform: translateX(-50%)">
    <Carousel {items} bind:activeIndex ride interval={2000}>
        <CarouselIndicators bind:activeIndex {items} />
            <div class="carousel-inner">
            {#each items as item, index}
                <CarouselItem bind:activeIndex itemIndex={index}>
                <img src={item.url} class="d-block w-100" alt={item.title} />
                </CarouselItem>
            {/each}
            </div>
        <CarouselControl direction="prev" bind:activeIndex {items} />
        <CarouselControl direction="next" bind:activeIndex {items} />
    </Carousel>
    {#if isVeterinary}
        <h1>BIENVENIDA VETERINARIO</h1>
        <button on:click={directView}>Lista de mascotas</button>
        <button on:click={directPet}>Buscar Mascotas</button>
        <button on:click={directRegister}>Registrar Mascota</button>
    {/if}

    {#if isSecretary}
        <h1>BIENVENIDA SECRETARIA</h1>
        <button on:click={directRegister}>Registrar Mascota</button>
    {/if}
</div>

<style>
    :global(body){
        background-image: url("https://cdn.discordapp.com/attachments/982444201558020116/988260548690976828/IMG_3446.png");
    }
    h1 {
        color: #0050A0;
        font-family:'Lucida Sans';
        font-size: 3em;
        text-transform: uppercase;
        text-align: center;
        text-decoration: underline;
        text-shadow: 1px 1px 1px;
    }
</style>